import pandas as pd

df = pd.read_csv('data/product-reviews.csv')
df.head()

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(temperature=0.9) #high!
prompt = ChatPromptTemplate.from_template("What is the best name to describe a company that makes the product {product}?")

chain = LLMChain(llm=llm, prompt=prompt)

product = "Queen size sheet set"
# repeat, see if different answers:
for x in range(3):
    rsp = chain.run(product)
    print(rsp)

from langchain.chains import SequentialChain

prompt_1 = prompt
chain_1 = LLMChain(llm=llm, prompt=prompt_1, output_key="company_name")

prompt_2 = ChatPromptTemplate.from_template("Identify the language of {company_name}")
chain_2 = LLMChain(llm=llm, prompt=prompt_2, output_key="language")

prompt_3 = ChatPromptTemplate.from_template("Write a 20 word description for the company {company_name}. Mention the {language}")
chain_3 = LLMChain(llm=llm, prompt=prompt_3, output_key="summary")

chain = SequentialChain(chains=[chain_1, chain_2, chain_3],
                              input_variables=["product"],
                              output_variables=["company_name", "summary"],
                              verbose=True)

rsp = chain(product)
print(rsp)
