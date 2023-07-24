from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch

file = 'data/OutdoorClothingCatalog_1000.csv'
print(f"Reading local file {file}")
loader = CSVLoader(file_path=file)

from langchain.indexes import VectorstoreIndexCreator

index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

query ="Please list all your shirts with sun protection \
in a table in markdown and summarize each one."

print(query)
response = index.query(query)
print(response)

loader = CSVLoader(file_path=file)

docs = loader.load()

print(docs[0])

from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

embed = embeddings.embed_query("Hi my name is Harrison")

print(f"{len(embed)} embeddings")
print(embed[:5])

db = DocArrayInMemorySearch.from_documents(
    docs, 
    embeddings
)

query = "Please suggest a shirt with sunblocking"
print(query)

docs = db.similarity_search(query)
print(f"{len(docs)} docs")
print(docs[0])

print("=== === === === ===")
retriever = db.as_retriever()
llm = ChatOpenAI(temperature = 0.0)

docs_count = min(len(docs), 3)
qdocs = "".join([docs[i].page_content for i in range(docs_count)])

response = llm.call_as_llm(f"{qdocs} Question: Please list all your \
shirts with sun protection in a table in markdown and summarize each one.") 
print(response)

qa_stuff = RetrievalQA.from_chain_type(
    llm=llm, 
    # 'stuff' is the simplest method. Stuffs all data into the prompt as context to pass to the LLM.
    #
    # pros: single call to LLM. LLM has access to all data at once.
    # cons: limited by the max context length.
    chain_type="stuff",
    retriever=retriever, 
    verbose=True
)

query =  "Please list all your shirts with sun protection in a table \
in markdown and summarize each one."

response = qa_stuff.run(query)
print(response)

response = index.query(query, llm=llm)
print(response)

print("=== customized with embeddings ===")
# Can customize:
# - the kind of vector store
# - the embeddings
index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch,
    embedding=embeddings,
).from_loaders([loader])
response = index.query(query, llm=llm)
print(response)
