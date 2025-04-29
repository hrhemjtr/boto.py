import discord
from discord.ext import commands

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Correct Role and Channel IDs
ROLE_ID_TO_REMOVE = 1366318201213812828  # <-- Updated role ID you just gave
CHANNEL_ID = 1352758058551611433          # <-- The channel ID where bot listens

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot is active"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Debug: print detected message
    print(f"Detected a message from {message.author} in {message.guild.name}")

    # Only react to messages in the target channel
    if message.channel.id != CHANNEL_ID:
        return

    role = message.guild.get_role(ROLE_ID_TO_REMOVE)
    if role is None:
        print(f"Role with ID {ROLE_ID_TO_REMOVE} not found in {message.guild.name}")
        return

    if role in message.author.roles:
        try:
            await message.author.remove_roles(role)
            print(f"Removed role '{role.name}' from {message.author}")
            await message.channel.send(f"{message.author.mention}, your role '{role.name}' was removed.")
        except discord.Forbidden:
            print(f"Missing permissions to remove role from {message.author}")
        except discord.HTTPException as e:
            print(f"Failed to remove role from {message.author}: {e}")

    await bot.process_commands(message)

# Run the bot directly with your token
import os
bot.run(os.getenv("MTM2NjMzMjgyNTU3NzQ1OTczMw.GHT3GB.tXxCe4VUkXIU_2x4TkdE_87xrVauZ4-4vLeSkU"))
