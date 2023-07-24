import json
from util_chat import send_prompt
from util_json import save_json_to_file

text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""

send_prompt(prompt)

prompt = f"""
Generate a list of top 50 sci-fi book titles along \ 
with their authors and genres. 
Provide a summary.
Provide the result in JSON format with the following keys: 
book_id, title, author, genre, summary.
"""

rsp = send_prompt(prompt)
save_json_to_file(json.loads(rsp), "./data/top-sci-fi-books.json")
