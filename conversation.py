from openai import OpenAI
client = OpenAI()

#sends a follow-up prompt that builds on the initial prompt and system response
#also uses the image_url to satisfy testing another part of Chat Completions API
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful baking assistant."},
        {
            "role": "user",
            "content": "How do I make an apple pie?"
        },
        {
            "role": "system",
            "content": [{"type": "text", "text": '{"steps":[{"explanation":"Prepare the pie crust by mixing flour, butter, salt, and water until a dough forms. Chill it in the refrigerator for about 30 minutes.","minutes_taken":30},{"explanation":"Preheat your oven to 425°F (220°C).","minutes_taken":15},{"explanation":"Roll out the dough on a floured surface and place it in a pie dish. Trim the edges.","minutes_taken":15},{"explanation":"Peel, core, and slice the apples. Mix them with sugar, cinnamon, flour, and lemon juice.","minutes_taken":20},{"explanation":"Fill the pie crust with the apple mixture, and dot with butter.","minutes_taken":10},{"explanation":"Roll out the second dough for the top crust, and place it over the apple filling. Cut slits for steam to escape, and crimp the edges to seal.","minutes_taken":15},{"explanation":"Brush the top crust with an egg wash and sprinkle some sugar on top.","minutes_taken":5},{"explanation":"Bake in the preheated oven for 15 minutes at 425°F, then reduce the temperature to 350°F (175°C) and bake for an additional 30 to 35 minutes until the apples are soft and the crust is golden brown.","minutes_taken":50},{"explanation":"Let the pie cool for at least an hour before slicing and serving.","minutes_taken":60}],"ingredient_cost":"Approximately $10","total_time":210}'}]
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Does this image look right?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url" : "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Apple_pie_14.jpg/200px-Apple_pie_14.jpg"
                    }
                },
            ],
        }
    ],
    max_tokens = 300,
)

print(completion.choices[0].message)