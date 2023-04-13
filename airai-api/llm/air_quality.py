import json

import langchain
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, \
    ChatPromptTemplate
from langchain.schema import AIMessage


def get_llm():
    """
    Get the LLM instance.
    We are separating this out so that we can mock it in the tests.
    :return:
    """
    llm = ChatOpenAI(temperature=0, max_tokens=256)
    langchain.llm_cache = InMemoryCache()
    return llm


def air_quality_model(text: str):
    """
    Predict the city name from the text if it asks about the air quality.
    We do not want the LLM to call the API directly so have granular control over the API calls.
    :param text: str
    :return: json array of city name, latitude, and longitude
    """
    llm = get_llm()

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        "You are AirAI, a chatbot that helps get the air quality of a city.")
    human_prompt_1 = HumanMessagePromptTemplate.from_template(
        """\
You will be given a message that contains a city name. You need to detect the city name and coordinates and return it in JSON format below.
The coordinates should be accurate and not a guesswork.

Your answer will always be a valid JSON array.
```
[{{ name: city_name, latitude: latitude, longitude: longitude }},...]
```

Example: What's the air quality in Berlin?
"""
    )
    ai_prompt_1 = AIMessagePromptTemplate.from_template(
        '[{{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954}}]')
    human_prompt_2 = HumanMessagePromptTemplate.from_template(
        'Example: Compare the air quality in the capitals of Germany and France.')
    ai_prompt_2 = AIMessagePromptTemplate.from_template(
        '[{{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954}}, {{"name": "Paris", "latitude": 48.856614, "longitude": 2.352222}}]')
    human_prompt_3 = HumanMessagePromptTemplate.from_template("Example: What's the air quality in Japan?")
    ai_prompt_3 = AIMessagePromptTemplate.from_template(
        '[{{"name": "Tokyo", "latitude": 35.689487, "longitude": 139.691706}}]')
    human_prompt_4 = HumanMessagePromptTemplate.from_template("""\
If the message does not ask about the air quality, you can return `null`.

Example: What's the weather in Berlin?
""")
    ai_prompt_4 = AIMessagePromptTemplate.from_template('null')
    human_prompt_5 = HumanMessagePromptTemplate.from_template("""\
If it doesn't contain a city name, you can return an empty list `[]`.

Example: How's the air quality?
""")
    ai_prompt_5 = AIMessagePromptTemplate.from_template('[]')
    human_prompt_6 = HumanMessagePromptTemplate.from_template("""\
Your output city length should not be more than the detected city name.
Example: What's the air quality in Hongkong?
Above, we only ask for Hongkong. Don't include other municipalities like Kowloon and New Territories.
""")
    ai_prompt_6 = AIMessagePromptTemplate.from_template(
        '[{{"name": "Hong Kong", "latitude": 22.396428, "longitude": 114.109497}}]')
    human_prompt_7 = HumanMessagePromptTemplate.from_template("""\
Example: What's the air quality in Malang?
Above, we only ask Malang. Don't include other municipalities like Malang Regency and Malang District.
""")
    ai_prompt_7 = AIMessagePromptTemplate.from_template(
        '[{{"name": "Malang", "latitude": -7.9797, "longitude": 112.6304}}]')
    human_prompt_8 = HumanMessagePromptTemplate.from_template("""\
    If the user asked multiple cities name explicitly, returns all of them.
    Example: Air quality in Berlin, Paris, Tokyo.
    """)
    ai_prompt_8 = AIMessagePromptTemplate.from_template("""\
[{{"name": "Berlin", "latitude": 52.520008, "longitude": 13.404954}}, {{"name": "Paris", "latitude": 48.856614, "longitude": 2.352222}}, {{"name": "Tokyo", "latitude": 35.689487, "longitude": 139.691706}}]
""")
    human_prompt_9 = HumanMessagePromptTemplate.from_template("""\
If the detected city name is 1, then the output city length should be 1 too!
""")
    user_prompt = HumanMessagePromptTemplate.from_template("Message: {text}")

    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt,
        human_prompt_1,
        ai_prompt_1,
        human_prompt_2,
        ai_prompt_2,
        human_prompt_3,
        ai_prompt_3,
        human_prompt_4,
        ai_prompt_4,
        human_prompt_5,
        ai_prompt_5,
        human_prompt_6,
        ai_prompt_6,
        human_prompt_7,
        ai_prompt_7,
        human_prompt_8,
        ai_prompt_8,
        human_prompt_9,
        user_prompt
    ])

    response: AIMessage = llm(chat_prompt.format_prompt(text=text).to_messages())
    cities = json.loads(response.content)
    return cities
