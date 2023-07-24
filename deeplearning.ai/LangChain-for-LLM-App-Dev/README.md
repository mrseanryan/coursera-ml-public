# LangChain for LLM App Development README

ref code + data here! = https://github.com/Ryota-Kawamura/LangChain-for-LLM-Application-Development

## Set up

```
pip3 install --upgrade langchain openai tiktoken pandas docarray wikipedia
```

OR

```
python3 -m pip install langchain openai tiktoken pandas docarray wikipedia
```

Set environment variable with your OpenAI key:

```
export OPENAI_API_KEY="xxx"
```

Add that to your shell initializing script (`~/.zprofile` or similar)
Load in current terminal:

```
source ~/.zprofile
```

## 1. Models, Prompts and parsers

- langchain helps to reuse complex prompts, and parse the output
- also it supplies some standard reusable prompts
- can query SQL database

- Thought, Action, Observation
-- Observation - what was learned from that Action
-- keywords for Chain-of-Thought Reasoning (ReAct)
- repeats: TAO, TAO, TAO... Finish

## 2. Memory

- memory via 'history' of messages

```
llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory = memory,
    verbose=False # set to True to see the prompts that langchain generates
)

conversation.predict(input="Hi, my name is Bob")

conversation.predict(input="What is 1 + 2 ?")

conversation.predict(input="What is my name?")
# bot 'remembers' !

print(memory.buffer)
print(memory.load_memory_variables({}))

```

### Additional Memory Types

- Vector data memory
-- can retrieve the most relevant blocks of text

- Entity memories
-- using an LLM, it remembers details about specific entities

You can use multiple memories at once.
e.g. Conversation + Entity memory to recall individuals.

You can also use conventional stores such as a key-value store or SQL database.

---
## 3. Chains

- pandas as data source
- LLMChain class

## 4. Q&A (on your data/documents)

challenge: LLMs can only inspect a few thousand words at a time! (ChatGPT3.5 Turbo = 4000 tokens ~= 2500 words)

solution:
- embeddings = numerical encoding of text
-- embedding vector (like word vectors?)
-- can compare pieces of text

- vector DB - to store the embedding vectors
-- create an index

- input: uses the index to find similar answers

# Calling the LLM
## Single-call to LLM ('Stuff' method)

'stuff' is the simplest method. Stuffs all data into the prompt as context to pass to the LLM.
- pros: single call to LLM. LLM has access to all data at once.
- cons: limited by the max context length.

## other ways:
### Map/Reduce
map/reduce: map to pass to LLM in chunks -> reduce (use final LLM call to summarise the combined results)
- pros: can call LLM in parallel, speeding up
- con: the document chunks are treated independently

### Refine
- refine: chunks, to LLM, but each subsequent call contains the output from the previous call.
- pro: the document chunks are processed together
- pro?: can get longer answer
- con: must call LLM in sequence of calls

### Map_rerank:
- first, call LLM once for each document (!)
-- get a score for each doc response
-- take the highest score, as the answer
- pro: can batch
- con: many calls
- con: assumes docs are independent

Stuff and Map/Reduce are the most common.

## 5. Evaluation of Q+A (evaluate the answers)

- langchain has module to help
- it can use LLM to generate Q+A pairs, with 'known good' answer

online tool: LangChain Evaluation Platform
- fancy UI to genreate Q+A and evaluate actual ansswers.

## 6. Agents

- can be sources (Wikipedia) or tools (Python code-writer(!) + executor) or custom tools (a Python function)
