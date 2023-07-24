
## Chain of Thought Reasoning (!)

- inner monologue = hide outputs from user, filtered, before showing to user

e.g.: classify a customer request, THEN add some more relevant info.

delimiter = "####"
```
system_message = f"""
Follow these steps to answer the customer queries.
The customer query will be delimited with four hashtags.
i.e. {delimiter}

Step 1:{delimiter} First decide whether the user is asking a question about a specific product or products.
The product category does not count.

Step 2:{delimiter} If the user is asking about specific products, identify whether the products are in the following list:

1. Product: TechPro Ultrabook
Category:x
Model:y
Price: $800

2. Product: BlueWave Gaming Laptop
Category:x
Model:z
Price: $1200

Step 3:{delimiter} If the message contains products in the list above, 
list any assumptions that the user is making in their message
e.g. that laptop X item is bigger than Laptop Y.

Step 4:{delimiter} If the user made any assumptions, figure out whether the assumption is true based on your product information.

Step 5:{delimiter} First, politely correct the customer's incorrect assumptions if applicable.
Only mention or reference products in the list of available products.
Answer the customer in a friendly tone.

Use the following format:
Step 1:{delimiter} <step 1 reasoning>
Step 2:{delimiter} <step 2 reasoning>
Step 3:{delimiter} <step 3 reasoning>
Step 4:{delimiter} <step 4 reasoning>
Step 5:{delimiter} <step 5 reasoning>
Response to user:{delimiter} <response to customer>

Make sure to include {delimiter} to separate each step.
"""

rso = get_completion(messages)
try:
    final_response = rsp.split(delimiter)[-1].strip() # take the last part of the response
except Exception:
    final_response = "Sorry, I'm having trouble understanding you."

```
# should the input {delimiter} be different from the steps {delimiter} ? NO since system is separate from user message.
# why: easier to filter down to what we want to show customer

# pedantic instructions!
# step-by-step, so not skip steps, or try to do in 1 step
# but might not be needed for ChatGPT4
