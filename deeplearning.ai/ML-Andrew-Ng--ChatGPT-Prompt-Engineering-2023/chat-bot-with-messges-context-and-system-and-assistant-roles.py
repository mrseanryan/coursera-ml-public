import util_chat

messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]

print(messages)
util_chat.send_prompt_messages(messages, temperature=1)

def print_separator():
    print("=== === === === === === === === ===")
    print("=== === === === === === === === ===")
    print("=== === === === === === === === ===")

print_separator()

messages =  [  
{'role':'system', 'content':'You are a friendly chatbot.'},
{'role':'user', 'content':'Hi, my name is Isa'},
{'role':'assistant', 'content': "Hi Isa! It's nice to meet you. Is there anything I can help you with today?"},
{'role':'user', 'content':'I have lost my dog.'},
{'role':'assistant', 'content': "Oh that is a shame - I hope they turn up soon."},
{'role':'user', 'content':'Can remind me, What is my name?'}  ]

print(messages)
util_chat.send_prompt_messages(messages, temperature=1)

print_separator()

messages_copy =  messages.copy()
messages_copy.append(
{'role':'system', 'content':'create a summary of all the previous messages, in casual English, in formal English and in Spanish. The summary must include details from all of the messages. Output the summaries and a total count of the messages.'},  
)
print(messages_copy)
util_chat.send_prompt_messages(messages_copy, temperature=1)

print_separator()

messages_copy =  messages.copy()
messages_copy.append(
{'role':'system', 'content':'You are an unfriendly, unhelpful chatbot. You only speak Dutch. Create a new reply to the previous messages, expressing your irritation.'},
)
print(messages_copy)
util_chat.send_prompt_messages(messages_copy, temperature=1)
