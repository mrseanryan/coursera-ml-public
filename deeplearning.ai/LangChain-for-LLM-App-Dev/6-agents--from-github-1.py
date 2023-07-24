# ref = https://github.com/Ryota-Kawamura/LangChain-for-LLM-Application-Development/blob/main/L6-Agents.ipynb

import warnings
warnings.filterwarnings("ignore")

from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0)

# wikipedia as a source!
tools = load_tools(["llm-math","wikipedia"], llm=llm)

agent= initialize_agent(
    tools, 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, # zero shot: NO context (no previuos messages or history)
    handle_parsing_errors=True, # helps improve output ('reasoning')
    verbose = True)

agent("What is the 25% of 300?")

question = "Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?"
result = agent(question) 
