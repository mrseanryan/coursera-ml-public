# ref = https://github.com/Ryota-Kawamura/LangChain-for-LLM-Application-Development/blob/main/L6-Agents.ipynb

import warnings
warnings.filterwarnings("ignore")

from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

print("Python Agent")

agent = create_python_agent(
    llm,
    tool=PythonREPLTool(),
    verbose=True
)

customer_list = [["Harrison", "Chase"], 
                 ["Lang", "Chain"],
                 ["Dolly", "Too"],
                 ["Elle", "Elem"], 
                 ["Geoff","Fusion"], 
                 ["Trance","Former"], # sorts this in-correctly (but in the lesson video it DID work ...)
                 ["Jen","Ayai"]
                ]

prompt = f"""Sort these customers by \
last name and then first name \
and print the output: {customer_list}"""
print(prompt)
rsp = agent.run(prompt) 
print(rsp)

print("=== customer_list_text ===")

customer_list_text = """
- Chase Harrison
- Lang Chain
- Dolly Too
- Elem En-Tarry
- Geoff Fusion
- Trance Former
- Jen Ayai
"""
# answers INcorrectly (Trance Former) - it seems to have difficulty recognising the input is FirstName LastName
# Bizarely, the Python code it writes is correct. It seems to change the output afterwards ...
prompt = f"""Sort these customers by \
last name and then first name \
and print the output: {customer_list_text}"""
print(prompt)
rsp = agent.run(prompt) 
print(rsp)

print("=== customer_list_text - with more detailed prompt ===")

prompt = f"""Sort these customers by \
last name and then first name \
and print the output: \
The input is in format: - FirstName LastName. \
IMPORTANT: After executing the Python, do NOT alter the output. \
customers: {customer_list_text}"""
print(prompt)
rsp = agent.run(prompt) 
print(rsp)

print(" === detailed outputs of the chains ===")

import langchain
langchain.debug=True
agent.run(f"""Sort these customers by \
last name and then first name \
and print the output: {customer_list}""") 
langchain.debug=False
