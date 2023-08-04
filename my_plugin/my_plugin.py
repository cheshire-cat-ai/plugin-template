from cat.mad_hatter.decorators import tool, hook
from pydantic import BaseModel
from datetime import datetime, date

class MySettings(BaseModel):
    required_int: int
    optional_int: int = 69
    required_str: str
    optional_str: str = "meow"
    required_date: date
    optional_date: date = 1679616000

@hook
def plugin_settings_schema():   
    return MySettings.schema()

@tool
def get_the_time(tool_input, cat):
    """Retrieves current time and clock. Input is always None."""

    return str(datetime.now())

@hook
def before_cat_sends_message(message, cat):

    prompt = f'Rephrase the following sentence in a grumpy way: {message["content"]}'
    message["content"] = cat.llm(prompt)

    return message