import discord
from ascii import Ascii


class Client(discord.Client):
    def __init__(self):
        main_channel_id = 1420531838845194312
        main_channel = Client.get_channel(main_channel_id)
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('&'):
            mensagem = message.content[1:]
            match mensagem:
                case 'pintogames':
                    await message.channel.send(Ascii.PINTO)
    async def on_member_join(member):
        await main_channel.send(f"olá amigo {member} você é um viadão de qualidade hein! fiu fiu!! safado to de olho em você hein")
    async def on_reaction_add(self, reaction, user):
        
        if reaction == ':eggplant:':
            main_channel.send(Ascii.PINTO)
        
    
        
        
        
intents = discord.Intents.default()
intents.message_content = True

key = open("key.txt").read()

client = Client(intents=intents)
client.run(key)