import sys
from util_chat import send_prompt

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} <genre>")
    exit(666)

genre = sys.argv[1]

prompt = f"""
Your task is to provide the first 80 words of a short story.

The story must be in the {genre} genre.
The style must be minimalist and low context.
"""

send_prompt(prompt)
