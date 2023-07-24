# ref = https://github.com/Ryota-Kawamura/LangChain-for-LLM-Application-Development/blob/main/L6-Agents.ipynb

import warnings
warnings.filterwarnings("ignore")

from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

print("=== LLM only === ")

prompt = "hello how are you?"
print(prompt)
result = llm.predict(prompt) 
print(result)

prompt = "whats the date today?"
print(prompt)
result = llm.predict(prompt) 
print(result)

def prompt_for_todays_date():
    try:
        prompt = "whats the date today?"
        print(prompt)
        result = agent(prompt) 
        print(result)
    except: 
        print("exception on external access")


prompt_for_todays_date()

print("=== LLM with custom tool (Python function to get today's date) === ")

from langchain.agents import tool
from datetime import date

@tool
def time(text: str) -> str:
    """Returns todays date, use this for any \
    questions related to knowing todays date. \
    The input should always be an empty string, \
    and this function will always return todays \
    date - any date mathmatics should occur \
    outside this function."""
    return str(date.today())

tools = load_tools(["llm-math","wikipedia"], llm=llm)

agent= initialize_agent(
    tools + [time], 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)

prompt_for_todays_date()
