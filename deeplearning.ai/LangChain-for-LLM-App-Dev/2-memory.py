from langchain.chat_models import ChatOpenAI

import langchain

# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
print("Opening Chat ...")
llm = ChatOpenAI(temperature=0.0)
llm

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory = memory,
    verbose=True # set to True to see the prompts that langchain generates
)

conversation.predict(input="Hi, my name is Bob")

conversation.predict(input="What is 1 + 2 ?")

conversation.predict(input="What is my name?")
# bot 'remembers' !

print(memory.buffer)
print(memory.load_memory_variables({}))

memory = langchain.memory.ConversationBufferWindowMemory(k=1)
memory.save_context({"input": "hi"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
print(memory.load_memory_variables({}))

print("= = = = = new memory = = = = = = =")

# (the actual LLM is not stateful)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory = memory,
    verbose=True # set to True to see the prompts that langchain generates
)
conversation.predict(input="what is my name?")
# AI LLM has 'forgotten', since new memory !
conversation.predict(input="Hi, my name is Bob")
conversation.predict(input="What is my name?") # AI does remember
conversation.predict(input="What is 1 + 2 ?")
conversation.predict(input="What is my name?") # AI has forgotten again, but this time because buffer size k=1

print("= = = memory size by token = = =")
# ChatGPT - 1 x token = 4 letters
memory = langchain.memory.ConversationTokenBufferMemory(llm=llm, max_token_limit = 14)
memory.save_context({"input": "hi"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
print(memory.load_memory_variables({}))

print("= = = memory size by summary = = =")
# best one? reduces memory loss
# The 'system' part contains an LLM generated summary.
# The remainder is what 'last non summarised' will fit in the buffer.
memory = langchain.memory.ConversationSummaryBufferMemory(llm=llm, max_token_limit = 20)
memory.save_context({"input": "hi"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
memory.save_context({"input": "do you like the hot weather?"}, {"output": "well hot weather is not always ideal, as it can be a strain on systems, both biological and mechanical"})
print(memory.load_memory_variables({}))
