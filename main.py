# Imports
import discord
from ascii import Ascii

# Classe do bot
class Client(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('&'):
            mensagem = message.content[1:]
            match mensagem:
                case 'pintogames':
                    await message.channel.send(Ascii.PINTO)


    async def on_member_remove(member):
        main_channel_id = 1420531838845194312
        main_channel = Client.get_channel(main_channel_id)

        print(member.name)
        await member.mention(f"ola {member.name} seu viadao bonitao!!!!!")
        await main_channel.send(f"olá amigo {member.id} você é um viadão de qualidade hein! fiu fiu!! safado to de olho em você hein")

# Inicializando
intents = discord.Intents.default()
intents.message_content = True

key = open("key.txt").read()

client = Client(intents=intents)
client.run(key)