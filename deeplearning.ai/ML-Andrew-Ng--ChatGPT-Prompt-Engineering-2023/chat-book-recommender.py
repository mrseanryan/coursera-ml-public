import json

from util_json import save_json_to_file
from util_chat import send_prompt

prompt = f"""
Your task is to analyze the given list of books,
and generate a list of 20 similar books.

The list of books is delimited by triple \
backticks. 

Try to pick books that are by similar author or are in a similar genre.

The output must be in JSON format, with fields: title, author, year, genre, summary.

books: ```Dragon's Egg, Children of Time, Red Dwarf, 2001 A Space Oddysey, Necromancer```
"""

rsp = send_prompt(prompt)
save_json_to_file(json.loads(rsp), "./data/similar-books.json")
