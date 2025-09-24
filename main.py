import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"Oi amigos lixo, eu, {self.user}, cheguei!!!")
    async def on_message(self, message):
        if message.content == "penis":
            print(f"{message.author} é um viadão!")
        
intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run()