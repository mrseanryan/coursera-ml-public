from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import DocArrayInMemorySearch

file = 'data/OutdoorClothingCatalog_1000.csv'
loader = CSVLoader(file_path=file)
data = loader.load()

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

llm = ChatOpenAI(temperature = 0.0)
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", # all docs in the 1 context to LLM
    retriever=index.vectorstore.as_retriever(), 
    verbose=True,
    chain_type_kwargs = {
        "document_separator": "<<<<>>>>>"
    }
)

#hard-coded example:

examples = [
    {
        "query": "Do the Cozy Comfort Pullover Set\
        have side pockets?",
        "answer": "Yes"
    },
    {
        "query": "What collection is the Ultra-Lofty \
        850 Stretch Down Hooded Jacket from?",
        "answer": "The DownTek collection"
    }
]

print("LLM-generated examples:")
from langchain.evaluation.qa import QAGenerateChain # generates questions and answers, to later test against
example_gen_chain = QAGenerateChain.from_llm(ChatOpenAI())

new_examples = example_gen_chain.apply_and_parse(
    [{"doc": t} for t in data[:5]]
)
print(new_examples[0])

print("Combine the hard-coded with the LLM generated examples")
examples += new_examples

qa.run(examples[0]["query"])

print("MANUAL Evaluation (langchain debug)")
import langchain
langchain.debug = True # can see context: the selected docs that were sent (sometimes wrong docs sent?)

qa.run(examples[0]["query"])

print("LLM assisted evaluation")
# Turn off the debug mode
langchain.debug = False

predictions = qa.apply(examples)

from langchain.evaluation.qa import QAEvalChain
llm = ChatOpenAI(temperature=0)
eval_chain = QAEvalChain.from_llm(llm)

graded_outputs = eval_chain.evaluate(examples, predictions)

print(graded_outputs)

def calc_percentage(numerator, total):
    return round(numerator / total * 100.0)

count_correct = 0
for i, eg in enumerate(examples):
    print(f"Example {i}:")
    print("Question: " + predictions[i]['query'])
    print("Real Answer: " + predictions[i]['answer'])
    print("Predicted Answer: " + predictions[i]['result'])
    grade = graded_outputs[i]['results']
    print("Predicted Grade: " + grade)
    if grade == "CORRECT":
        count_correct += 1
print(f"{calc_percentage(count_correct, len(examples))}% correct predictions (total {len(examples)})")
