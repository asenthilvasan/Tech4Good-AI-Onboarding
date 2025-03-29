from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class GratitudeAnalysis(BaseModel):
    groups_of_people: list[str]
    description: list[str]
    where_to_find: list[str]

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
                {"role": "system",
                 "content": '"You are a helpful a program that looks at and analyzes gratitude notes.The text delimited by triple quotes is in response to a question, "What do you feel grateful for about at the University of California, Santa Cruz?". '
                            'Can you extract the groups of people that contributed to what the author was grateful for along with a description of what the people did? '
                            'For example, the Environmental Maintenance Staff for maintaining the beautiful open fields and redwoods surrounding the campus buildings, ensuring a serene and natural ambiance. Please list 2 to 3 groups of people that contributed to what the author is grateful for. '
                            'Also include a description of where to find these people at University of California, Santa Cruz."'},
                {
                    "role": "user",
                    "content": "'''I am immensely grateful for my time at UCSC, as it has been a truly unforgettable experience. The breathtaking ocean view that greeted me daily was a constant source of inspiration and tranquility, making every day on campus feel like a gift. The winding trails nestled in the lush redwood forests allowed for moments of reflection and a connection with nature that was simply magical. But above all, it was the caring and supportive faculty and staff that made my journey exceptional.'''"
                },
                {
                    "role": "assistant",
                    "content": [{"type": "text", "text": '''{"groups_of_people":"Caring and supportive faculty and staff","description":"The caring and supportive faculty and staff at UCSC provided guidance and encouragement throughout the author's academic journey, which contributed significantly to their positive experiences on campus.","where_to_find":["Faculty offices in academic buildings","Administrative offices","Career services center"]}'''}]
                },
                {
                    "role": "user",
                    "content": [{"type": "text", "text": "Make it follow the format in the example given better."}]
                }

            ],
    response_format=GratitudeAnalysis,
)

event = completion.choices[0].message.parsed
print(event.model_dump_json())