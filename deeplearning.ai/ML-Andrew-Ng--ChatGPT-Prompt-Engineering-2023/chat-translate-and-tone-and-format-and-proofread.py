import json
from redlines import Redlines

from util_chat import send_prompt
from util_json import save_json_to_file
import util_wait

def translate_and_save():
  text = f"""
  In a charming village, siblings Jack and Jill set out on \ 
  a quest to fetch water from a hilltop \ 
  well. As they climbed, singing joyfully, misfortune \ 
  struck—Jack tripped on a stone and tumbled \ 
  down the hill, with Jill following suit. \ 
  Though slightly battered, the pair returned home to \ 
  comforting embraces. Despite the mishap, \ 
  their adventurous spirits remained undimmed, and they \ 
  continued exploring with delight.
  """
  prompt = f"""
  Your task is to perform the following actions: 
  1 - Summarize the following text delimited by 
    <> with 1 sentence.
  2 - Translate the summary into Dutch.
  3 - List each name in the translated summary.
  4 - Output a json object that contains the 
    following keys: translated_summary, names, language_code.

  Output in JSON format.

  Text: <{text}>
  """

  rsp = send_prompt(prompt)
  save_json_to_file(json.loads(rsp), "./data/translated-NL.json")

def translate_multiple():
  user_messages = [
    "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
    "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
    "Il mio mouse non funziona",                                 # My mouse is not working
    "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
    "我的屏幕在闪烁"                                               # My screen is flashing
  ]

  for issue in user_messages:
      prompt = f"Tell me what language this is: ```{issue}```"
      send_prompt(prompt)

      prompt = f"""
      Translate the following  text to English \
      and Korean: ```{issue}```
      """
      send_prompt(prompt)

  prompt = f"""
  Translate the following text to Spanish in both the \
  formal and informal forms: 
  'Would you like to order a pillow?'
  """
  send_prompt(prompt)

def transform_tone():
  prompt = f"""
  Translate the following from slang to a business letter: 
  'Dude, This is Joe, check out this spec on this standing lamp.'
  """
  send_prompt(prompt)

  prompt = f"""
  Translate the following from slang to a business letter, using a respectful tone: 
  'Hey mofo, what is your problem? Send the money or else...'
  """
  send_prompt(prompt)

def transform_format():
  data_json = { "resturant employees" :[ 
      {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
      {"name":"Bob", "email":"bob32@gmail.com"},
      {"name":"Jai", "email":"jai87@gmail.com"}
  ]}

  prompt = f"""
  Translate the following python dictionary from JSON to an HTML \
  table with column headers and title: {data_json}
  """
  send_prompt(prompt)

def proofread():
  text = [ 
    "The girl with the black and white puppies have a ball.",  # The girl has a ball.
    "Yolanda has her notebook.", # ok
    "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
    "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
    "Your going to need you’re notebook.",  # Homonyms
    "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
    "This phrase is to cherck chatGPT for speling abilitty"  # spelling
  ]
  for t in text:
      prompt = f"""Proofread and correct the following text
      and rewrite the corrected version. If you don't find
      any errors, just say "No errors found". Don't use 
      any punctuation around the text:
      ```{t}```"""
      send_prompt(prompt)

  text = f"""
  Got this for my daughter for her birthday cuz she keeps taking \
  mine from my room.  Yes, adults also like pandas too.  She takes \
  it everywhere with her, and it's super soft and cute.  One of the \
  ears is a bit lower than the other, and I don't think that was \
  designed to be asymmetrical. It's a bit small for what I paid for it \
  though. I think there might be other options that are bigger for \
  the same price.  It arrived a day earlier than expected, so I got \
  to play with it myself before I gave it to my daughter.
  """
  prompt = f"proofread and correct this review: ```{text}```"
  response = send_prompt(prompt)

  diff = Redlines(text,response)
  print(diff.output_markdown)

  prompt = f"""
  proofread and correct this review. Make it more compelling. 
  Ensure it follows APA style guide and targets an advanced reader. 
  Output in markdown format.
  Text: ```{text}```
  """
  send_prompt(prompt)

translate_and_save()
util_wait.wait_seconds(3)
translate_multiple()
util_wait.wait_seconds(3)
proofread()
util_wait.wait_seconds(3)
transform_tone()
util_wait.wait_seconds(3)
transform_format()
