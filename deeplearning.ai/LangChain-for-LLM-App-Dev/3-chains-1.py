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

from langchain.chains import SimpleSequentialChain

prompt_1 = ChatPromptTemplate.from_template("What is the best name to describe a company that makes the product {product}?")
chain_1 = LLMChain(llm=llm, prompt=prompt_1, output_key="company_name")

# company_name is output from promp_1, and input to prompt_2:
prompt_2 = ChatPromptTemplate.from_template("Write a 20 word description for the company {company_name}")
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

chain = SimpleSequentialChain(chains=[chain_1, chain_2], verbose=True)

rsp = chain.run([product])
print(rsp)
