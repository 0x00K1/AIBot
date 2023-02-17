# AIBot

# #Setup

This assumes you have a Discord account, server and a role in that server with priviliges to set up a bot.

## Create a Discord bot

1. Go to https://discord.com/developers/applications create an application.
2. And build a bot under the application.
3. Get the token from Bot setting.
4. Store the token in Secrets as an environment variable with the name `DISCORD_BOT_TOKEN`
5. Turn MESSAGE CONTENT INTENT `ON`
6. Invite your bot through OAuth2 URL Generator

## Get your session token
Go to https://chat.openai.com/chat from the Chrome browser and log in
1. Open Chrome DevTools 
2. Open `Application` tab > Cookies
   ![image](https://user-images.githubusercontent.com/36258159/205494773-32ef651a-994d-435a-9f76-a26699935dac.png)
3. Copy the value for `__Secure-next-auth.session-token` and add it to Secrets as an environment variable with the name `CHAT_GPT_SESSION_TOKEN`

## DM CyberAI bot in Discord

# #Enjoy :)
