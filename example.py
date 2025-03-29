from openai import OpenAI
client = OpenAI()

# writes a prompt that produces a JSON object - ensure through schema and strict=True
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful baking assistant."},
        {
            "role": "user",
            "content": "How do I make an apple pie?"
        }
    ],
    response_format = {
        "type":"json_schema",
        "json_schema": {
            "name":"baking_response",
            "schema": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type":"array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "explanation": {"type": "string"},
                                "minutes_taken": {"type": "number"},
                            },
                            "required": ["explanation", "minutes_taken"],
                            "additionalProperties": False
                        }
                    },
                    "ingredient_cost": {"type": "string"},
                    "total_time": {"type": "number"}
                },
                "required": ["steps", "ingredient_cost", "total_time"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
)

print(completion.choices[0].message.content)
