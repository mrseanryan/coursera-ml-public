from util_chat import send_prompt

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""

send_prompt(prompt)


prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie.

BUT if you are not sure, then add a warning to the output.
"""

send_prompt(prompt)

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie.

First find the relevant information.
Then answer the question based on the relevant information.

Include links to the sources of the information.
"""

send_prompt(prompt)
