import discord
import asyncio
from discord.ext import commands
from botlogic import pass_gen


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event #Member Baru
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Selamat datang {member.mention} di {guild.name}! :wave:'
        await guild.system_channel.send(to_send)

@bot.event #Hapus!
async def on_message_delete(message):
    msg = f'{message.author} Baru saja menghapus teks berisi: {message.content} :face_with_monocle:'
    await message.channel.send(msg)

@bot.event #Edit
async def on_message_edit(before, after):
    msg = f'**{before.author}** Baru saja mengubah teks menjadi:\n{before.content} :arrow_right: {after.content} :face_with_monocle:'
    await before.channel.send(msg)

@bot.event #kode ini saya temukan dari pencarian
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(":question: Perintah tidak ada, ketik ($list) atau ($help) untuk informasi lebih lanjut. :question:")

@bot.command()
async def list(ctx):
    await ctx.send('List perintah ($):')
    await ctx.send('hapus, hello, heh, passgen, pangkat')

@bot.command() #ini kurang berguna sih, agak sampah, tapi buat sekarang tidak dihapus karena ada kemungkinan untuk diperbaiki nanti.
async def hapus(ctx):
    msg = await ctx.send('oke, akan dihapus...')
    await msg.delete()

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passgen(ctx):
    await ctx.send("Oke, password nya: ")
    await ctx.send(pass_gen(10))

@bot.command()
async def pangkat(ctx):
    await ctx.send("Anka yang mau dipangkat? ")
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    await ctx.send(f"Hasil pangkat duanya adalah {(int(message.content)**2)} ")

bot.run("SecretToken")
