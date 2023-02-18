import os
import subprocess
import discord
from revChatGPT.revChatGPT import Chatbot
import asyncio
import time
from server import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)

TOKEN = "DISCORD_BOT_TOKEN" # "DISCORD_BOT_TOKEN"
SESSION_TOKEN = "CHATGPT_SESSION_TOKEN" # "CHATGPT_SESSION_TOKEN"
EMAIL = "CHATGPT_EMAIL" # "CHATGPT_EMAIL"
PASSWORD = "CHATGPT_PASSWORD" # "CHATGPT_PASSWORD"

config = {
  "email": EMAIL,
  "password": PASSWORD,
  "session_token": SESSION_TOKEN,
  "Authorization": '<Auth>',
  "accept_language": "en-US,en",
}

CHANNEL = "ℂ𝕪𝕓𝕖𝕣𝔸𝕀-🤖"
# Create a chatbot object
chatbot = Chatbot(config, conversation_id=None)

@client.event
async def on_ready():
    # print(f'Logged in as {client.user}!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_guild_join(guild):
    # Check if the bot has permissions to create channels
    if guild.me.guild_permissions.manage_channels:
        # Create a new channel with the specified name
        channel = await guild.create_text_channel(CHANNEL)
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Check if the message was sent in the bot channel
    if message.channel.name != CHANNEL:
        return
      
     # Out of service Mode Message
    # if message.content == message.content:
    #     out_msg = await message.channel.send("`Out of Service 503`")
    #     # Add a reaction to the message
    #     await out_msg.add_reaction("🚫")
    #     return message.content
    
    # Comments
    if message.content.startswith('# '):
         await message.add_reaction('👀')
         return message.content


    # User Interacting Start
    Char = '$'
    user_message = message.content
    if user_message.startswith(Char):
        # Open the file in 'a' (append) mode
        with open("MSG_logs.txt", "a") as f:
            # Write the message to the file
            f.write(f"{message.author}: {user_message}\n")

        # Remove `$` Char
        p_user_message = user_message[1:]

        # Help
        if p_user_message.lower() == 'help':
            await message.channel.send(f'''
               {message.author.mention} Thank you for providing a help command! Here is a description of each command:\n
- `$INFO` 
# This command will provide information about me, the Assistant, including my training data and capabilities.


- `$/> [Here your message]`
# This command allows you to ask a question or make a statement, and I will do my best to provide a helpful and accurate response, Simply type your message after the $/> and I will do my best to assist you.


- `# [Comment]`
# This command for comments, I'll not grep the request.
''')
        # Public
        if p_user_message.lower() == 'info':
            # Send
            await message.channel.send(f'''
                                Holla! {message.author.mention},
I'm CyberAI, the advanced AI bot created by Kun, I am excited to introduce you to this amazing technology that I have been working on. The CyberAI bot is a program that uses artificial intelligence to perform various tasks and functions. It is designed to learn and adapt over time, allowing it to become more efficient and effective at completing tasks. The CyberAI bot is capable of learning from its experiences, making decisions based on data and information, and even communicating with users through natural language processing. I believe that this technology has the potential to revolutionize the way we interact with machines and make our lives easier and more efficient. I am excited to see where this technology takes us in the future and I hope you will join me in exploring all that the CyberAI bot has to offer.
                                                ''')

        # Do u love me ?
        if p_user_message.lower() == '':
            # Send
            await message.channel.send(f'''
                                oowwww! {message.author.mention},
Whew i looovvveee u <3
                                                ''')

        # AI
        if p_user_message.startswith('/> '):
           # Here The bug about 60 line , i removed it according to GPT policy.
    else:
        # Display list of available commands
        await message.channel.send(f'''
                                         {message.author.mention}           
                                           *𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒  *
                                    +--------------------------------+
                                    |                       `$Help`                          |
                                    |                       `$INFO`                          |
                                    |    `$/> [Here your message]`       |
                                    |                `# [Comment]`                    |
                                    +--------------------------------+
                                    ''')
        time.sleep(3)
        error_msg = await message.channel.send('''
                    ᲼᲼᲼᲼\n
This message typically appears when there is an issue with sending a request or completing a task. It could be due to a variety of factors, such as an issue with the system or network, or a problem with the request itself. If you continue to see this message and are unable to complete your request, it may be helpful to try again later or to contact the creator of the system or service you are using for further assistance. They may be able to provide additional information or troubleshoot the issue to help resolve the problem.
                                            ''')
        await error_msg.add_reaction("⚠️")


keep_alive()
client.run(TOKEN)
