# Building Systems with ChatGPT

Course at https://learn.deeplearning.ai/chatgpt-building-system/lesson/2/language-models,-the-chat-format-and-tokens.

## LLM (Large Language Model)

An LLM is built by using _supervised_ learning (x -> y) to repeatedly predict the next word.

e.g. "My favourite food is an" -> "apple".

| Input X                           | Output Y |
| --------------------------------- | -------- |
| My favourite food is a            | bagel    |
| My favourite food is a bagel      | with     |
| My favourite food is a bagel with | cream    |

... and so on ...

Can create a massive training set, by dividing up a text with a "sliding window" as above.

### Two types of LLMs

1. Base LLM

Predicts next word, based on text training data.

Problem: it may for example answer a question with a question, depending on what texts it trained on.

2. Instruction Tuned LLM

- train a Base LLM (can take months!)
OR take a base model, pre-trained

- fine-turne on examples of where the output follows an input instruction
e.g. can hire contractors to write such instructions

- obtain human-ratings of the quality of different LLM outputs
-- criteria may include: helpful, honest, harmless ...
- tune the LLM to increase the probability that it generates the more highly rated outputs
-- using RLHF (Reinforcement Learning from Human Feedback)
-- takes days (rather than months for the base LLM!)

### Applications - un-structured data (like large bodies of text) NOT tabular data

## Using LLM - Tokens

LLM predicts the next token (not exactly a word)
- token = commonly occuring sequence of characters
-> so, asking  LLM to reverse a word OR input mis-spelling may cause issues with the output quality

- trick: can spell word like l-o-l-l-i-p-o-p and THEN ask it to reverse that -> since LLM can now see the 'tokens' (the individual letters, in this case)

- English: 1 x token = 4 characters, or about 3/4 or a word

- input = the context
- output = the completion

gtp3.5-turbo - has about 4000 tokens (input AND output)

### Using - Roles and Messages

```
# can have roles - also 'assistant'
# see the prompt-enginnering course notes
# - ../ML-Andrew-Ng--ChatGPT-Prompt-Engineering-2023/chat-bot-with-messges-context-and-system-and-assistant-roles.py
messages = [
    # System - overall  tone/behaviour of assistant
    { 'role': 'system', 'content': 'You are an assistant who responds in the style of Dr Seuss' },
    # Assistant
    # - if want what was previously said
    # (and the user also?)
    # User - prompt
    # the current prompt:
    { 'role': 'user', 'content': 'Write me a very short poem about vegetables' }
]
```

### Using - Chat-GPT Response

Counts of tokens:

```
- response['usage']['prompt_tokens']
- response['usage']['completion_tokens']
- response['usage']['total_tokens']
```

## Next READMEs

[README.2.classification.md](README.2.classification.md)

[README.3.moderation.md](README.3.moderation.md)

[README.4.reasoning.md](README.4.reasoning.md)

[README.5.chaining-prompts.md](README.5.chaining-prompts.md)

[README.6.CheckOutputs.md](README.6.CheckOutputs.md)

[README.7.Evaluation-process.md](README.7.Evaluation-process.md)
