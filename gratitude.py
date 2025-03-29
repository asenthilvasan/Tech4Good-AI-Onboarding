from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system",
         "content": '"You are a helpful a program that looks at and analyzes gratitude notes.The text delimited by triple quotes is in response to a question, "What do you feel grateful for about at the University of California, Santa Cruz?". '
                    'Can you extract the groups of people that contributed to what the author was grateful for along with a description of what the people did? '
                    'For example, the Environmental Maintenance Staff for maintaining the beautiful open fields and redwoods surrounding the campus buildings, ensuring a serene and natural ambiance. Please list 2 or more groups of people that contributed to what the author is grateful for. '
                    'Also include a description of where to find these people at University of California, Santa Cruz."'},
        {
            "role": "user",
            "content": "'''I'm very grateful for Santa Cruz, it's given me so much. I'm grateful for so many things but some that stick out are all the amazing people like my professors, friends, and all the incredible people I've met through Tech4Good. Santa Cruz has a beautiful environment, with amazing views and scenic routes that make me feel at ease, calm, and happy. The downtown life is very fun and engaging, as well as the campus life with its activities, events, clubs, and sports. Almost everyone I have met here in Santa Cruz has been very nice, kind, and just amazing. There have been many people who have made an impact on me some include Professor David Lee for believing in me and giving me a chance, my housemates and friends who I share similar values and culture with, my other friends, and last of all my friends in Tech4Good who I get the pleasure of working with every day and get the chance to build this lab with. The city of Santa Cruz and UCSC will forever hold a special place in my heart because of all the fond memories and experiences I have here, my time doing school here, and all the friends, family, and people I know here.'''"
        },
        {
            "role": "assistant",
            "content": [{"type": "text", "text": '''{"thanks":[{"groups_of_people":"Environmental Maintenance Staff","description":"The Environmental Maintenance Staff for maintaining the breathtaking ocean view and the lush redwood forests. They ensured that the natural surroundings of UCSC provided beauty, inspiration, and places for reflection.","where_to_find":"These individuals can typically be found working around the campus grounds, keeping the natural scenery pristine and welcoming."},
                                                    {"groups_of_people":"Faculty and Staff","description":"The caring and supportive faculty and staff contributed to the exceptional journey of the author at UCSC. They provided academic guidance and a supportive learning environment, enhancing the overall university experience.","where_to_find":"These people can be found across various departments and offices on the UCSC campus, assisting students in their educational and personal growth."}]}'''}]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Make it follow the format in the example given better."}]
        }

    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "gratitude_response",
            "schema": {
                "type": "object",
                "properties": {
                    "thanks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "groups_of_people": {"type": "string"},
                                "description": {"type": "string"},
                                "where_to_find": {"type": "string"},
                            },
                            "required": ["groups_of_people", "description", "where_to_find"],
                            "additionalProperties": False
                        }
                    }
                },
                "required": ["thanks"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
)

print(completion.choices[0].message.content)