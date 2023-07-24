from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

physics_expert_template ="""
You are a very smart physics professor.

If you don't know the answer to the question, you admit that.

Here is a question:
{input}
"""

maths_expert_template ="""
You are a very good mathematician.

If you don't know the answer to the question, you admit that.

Here is a question:
{input}
"""

history_expert_template ="""
You are a very good history teacher.

If you don't know the answer to the question, you admit that.

Here is a question:
{input}
"""

prompt_details = [
    {
        "name": "physics",
        "description": "Good for answering questions about physics",
        "prompt_template": physics_expert_template
    },
    {
        "name": "history",
        "description": "Good for answering questions about history",
        "prompt_template": history_expert_template
    },
    {
        "name": "maths",
        "description": "Good for answering questions about maths",
        "prompt_template": maths_expert_template
    },
]

from langchain.chains import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0.9) #high!

destination_chains = {}
for detail in prompt_details:
    name = detail["name"]
    prompt_template = detail["prompt_template"]
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

destinations = [f"{p['name']}: {p['description']}" for p in prompt_details]
destinations_str = "\n".join(destinations)

default_prompt = ChatPromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=default_prompt)

MULTI_PROMPT_ROUTER_TEMPLATE = """
Given a raw text input, decide the best destinaion prompt.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted like this:
```json
{{{{
    "destination": string, \ name of the prompt to use or "Default"
    "next_inputs": string \ a potentially modified version of the input
}}}}
```

REMEMBER: "destination" MUST be one of the candidate prompts.
REMEMBER: "next_inputs" can just be the original input if you do not know the output

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT (remember to include the ```json) >>"""

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(
    destinations = destinations_str
)

print("router_template:")
print(router_template)
print("====")

from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser

router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser()
)

router_chain = LLMRouterChain.from_llm(llm, router_prompt)

chain = MultiPromptChain(router_chain=router_chain,
                 destination_chains=destination_chains,
                 default_chain=default_chain, verbose=True)

user_prompts = [
    "What is black body radiation?",
    "what is 2 + 5 divided by 10 ?",
    "Who won the battle of Agincourt, and why was it fought?",
    "What is my favourite color?",
    "Why does every cell in our body contain DNA?"
    ]

for user_prompt in user_prompts:
    print("---")
    print(user_prompt)
    # should route to the right 'expert' chain!
    rsp = chain.run(user_prompt)
    print(rsp)
