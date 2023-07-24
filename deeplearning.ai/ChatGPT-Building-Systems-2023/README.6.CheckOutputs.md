# Check Outputs

- check outputs before showing to the user

- should not really be needed, especially with advanced models like ChatGPT-4

## Using Open AI Moderation API

response = openai.Moderation.create(
    input = final_response_to_customer
)

## Ask the model itself to regulate its output

```
system_message = f"""
...

Response with aY or N charachter, with no punctuation:
Y - if the output sufficiently answers the question AND the response correctly uses product information
N - otherwise
"""

q_a_pair = f"""
Customer message: ```{customer_message}```
Product information: ```{product_information}```
Agent response: ```{final_response_to_customer}```

Does the response use the retrieved information correctly?
Does the response sufficiently answer the question?

Output Y or N
"""

messages = [
    {'role': 'system', 'content': system_message},
    {'role': 'user', 'content': q_a_pair}
]

rsp = get_completion_from_messages(messages)
```

# Chain - like workflow

1 - moderation of the input
2 - extract list of prodcuts
3 - look up product information
4 - generate response to user question
5 - (optional) moderation of the output
6 - show output to user
