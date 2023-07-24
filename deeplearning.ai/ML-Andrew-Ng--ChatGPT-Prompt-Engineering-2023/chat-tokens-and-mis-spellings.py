from util_chat import send_prompt

# tokens mean that LLM does not really know words, it knows N-letter tokens. For ChatGPT, N is typically 4.
#
# so it has difficulty writing words backwards!
prompt = f"""
Your task is to analyze the given list of words,
and output each word, written backwords.

The list of books is delimited by triple \
backticks. 

The output must be in JSON format.

words: ```Dragon, Egg, Children, of, Time, Red, Dwarf, 2001, Space, Oddysey, Necromancer```
"""

send_prompt(prompt)

# bot does well on mis-spelled words, where just 1 letter missing
prompt = f"""
Your task is to analyze the given list of words,
checking for mis-spelling.

The list of books is delimited by triple \
backticks. 

For each word, do the following:
Step 1: check is the word spelled correctly
Step 2: if the word is not correctly spelled, generate the corrected word

The output must be in JSON format, with fields: input_word, is_spelled_correctly, correct_word.

words: ```Dragon, Eg, Childen, of, Tme, Red, Dwrf, 2001, Spce, Odysey, Necrmancer```
"""

send_prompt(prompt)
