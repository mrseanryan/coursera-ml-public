# Classification

## LLM in use

### Classification

```
DELIMITER = "####"

system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited by {DELIMITER} characters.

Classify each query into a primaary and secondary catgegory.
Provide your output in JSON format with the keys: primary and secondary.

Prinmary categories: Billing, Technical Support

Billing secondary categories: Unsubsribe or upgrade, Add a payment method, Explanation for a charge

Technical Support secondary categories: General troubleshooting, Device compatibility
"""

# the prompt from end-user
user_message= f"""
I want you to delete my profile and all of my user data
"""

messages = [
{'role':'system', 'content': system_message },
{'role':'user', 'content': DELIMITER + user_message + DELIMITER },
]

rsp = get_completion_from_messages(messages)

```
