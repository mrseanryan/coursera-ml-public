# Chaining Prompts

- like cooking a complex meal, in stages
-- else, end up with soup, or porridge...

Chaining Prompts: can maintain the state of the system at any given point.
(a bit like a state machine?)

Approach:
- externally from the LLM, keep track of the state
- reduce number of tokens used in a prompt
- skip some chains of the workflow, when not needed for that particular task

Suitable for complex tasks.

Advantages:
- lower costs (since you pay per token!)
- less tokens needed -> get around the token limit!
- can be less errors (more 'step by step') [but ChatGPT4 might need this less]
- helps manage the overall complexity
- easier to test
- easier to have a human in the loop
- can use external tools at points in the workflow (web search, database, REST API ...)

Related:
- ChatGPT plugins
- Text embeddings (for fuzzy or semantic search, not need exact keywords)
-- might be another course!

# Prompt

## Prompt that ONLY identifies Products and Categories

- one part of a bigger workflow
- specialised purpose

A bit like in [README.4.reasoning](README.4.reasoning.md)
BUT more limited:

```
system_message = f"""
...

Where the categories and products must be found in 
the customer service query.
If a product is mentioned, it must be associated with 
the correct category in the allowed products list below.
If no products or categories are found, output an empty list.

Allowed producs:

Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase

Only output the list of products, with nothing else.
"""

```

## Retrieve data from data store, using the Product identified by the LLM

#### Helper functions - Python dictionary use:
```
products = {
    "FotoSnap Instant Camera": {
        "name": "FotoSnap Instant Camera",
        "category": "Cameras and Camcorders",
        "price": 79.81
    }
}

def get_product_by_name(name):
    return products.get(name, None)

def get_products_by_category(category):
    return [product for product in products.get_values() if product["category"] == category]
```

retrieved_product_info = get_products_by_category(rsp.category)

## Send further prompt to LLM, using the retrieved product info

- include the user's original question

```
system_message = f"""
You are a customer service assistant for a large electronic store.
Respond in a friendly and helpful tone, with very concise answers.
Make sure to ask the user relevant follow up questions.
"""

user_message_original = f"""
tell me about the smartx pro phone and
the fotosnap camera, the dslr one.
also tell me about your tvs.
"""

messages = [
    {
        {'role': 'system', 'content': system_message},
        {'role': 'assistant', 'content': "Relevant product information:" + retrieved_product_info},
        {'role': 'user', 'content': user_message_original}
    }
]

```
