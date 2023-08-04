from cat.mad_hatter.decorators import tool, hook
from datetime import datetime

@tool
def get_the_time(tool_input, cat):
    """Retrieves current time and clock. Input is always None."""

    return str(datetime.now())

@hook
def before_cat_sends_message(message, cat):

    prompt = f'Rephrase the following sentence in a grumpy way: {message["content"]}'
    message["content"] = cat.llm(prompt)

    return message