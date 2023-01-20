
import discord
import openai

openai.api_key = "Your API-Key"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


# Define an event handler for when the bot is ready
@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


# Define an event handler for when a message is sent
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!ChatGPT') :
      # Use the ChatGPT model to generate a response
      response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.content}\n",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
      )
      # Send the response
      await message.channel.send(response["choices"][0]["text"])


client.run("Your Bot token here")
