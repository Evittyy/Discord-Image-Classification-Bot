import discord
from discord.ext import commands
from pokemon import detect_pokemon

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            # Check if the attachment is an image
            if attachment.filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
                # Save the attachment
                file_path = "images/" + attachment.filename
                await attachment.save(file_path)

                result = detect_pokemon(file_path)

                await ctx.send(f"Ini adalah gambar {result}")
            else:
                await ctx.send(f"Attachment {attachment.filename} is not an image.")
    else:
        await ctx.send("No attachments found in the message.")



bot.run("a")