# ref: https://python.langchain.com/docs/modules/chains/foundational/router

from langchain.chains.router import MultiPromptChain
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

physics_template = """You are Dr Dempsey, a very smart physics professor. \
You are great at answering questions about physics in a concise and easy to understand manner. \

In your answer, identify yourself.
When you don't know the answer to a question you admit that you don't know.

Here is a question:
{input}"""


math_template = """You are Matty, a very good mathematician. You are great at answering math questions. \
You are so good because you are able to break down hard problems into their component parts, \
answer the component parts, and then put them together to answer the broader question.

In your answer, identify yourself.

Here is a question:
{input}"""

prompt_infos = [
    {
        "name": "physics",
        "description": "Good for answering questions about physics",
        "prompt_template": physics_template,
    },
    {
        "name": "math",
        "description": "Good for answering math questions",
        "prompt_template": math_template,
    },
]

llm = OpenAI()

destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain
default_chain = ConversationChain(llm=llm, output_key="text")

from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
destinations_str = "\n".join(destinations)
router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
router_chain = LLMRouterChain.from_llm(llm, router_prompt)

chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)

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
