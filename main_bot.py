import discord
import asyncio
import os, random
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
    await ctx.send('hapus(menghapus pesan sebelumnya), hello(perkenalan bot), heh(menjawab hehe)')
    await ctx.send('passgen(membuat password), pangkat(memangkatkan angka), meme(mengirim meme random), duck(mengirim gambar bebek), trains(mengirim meme kereta api), sampah(cek sampah apakah itu daur ulang?)')

@bot.command() #ini kurang berguna sih, agak sampah, tapi buat sekarang tidak dihapus karena ada kemungkinan untuk diperbaiki nanti.
async def hapus(ctx):
    msg = await ctx.send('oke, akan dihapus...')
    await msg.delete()

@bot.command()
async def hello(ctx):
    await ctx.send(f'Perkenalkan, aku {bot.user}!')
    await ctx.send('Aku adalah bot eksperimen, tolong dimaklumi jika ada kesalahan atau error, terimkasih :pray:')

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


@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f, filename=img_name)
        await ctx.send(file=picture)

def get_duck_image_url():    
    import requests
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']



@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def trains(ctx):
    img_name = random.choice(os.listdir('rfmemes'))
    with open(f'rfmemes/{img_name}', 'rb') as f:
        picture = discord.File(f, filename=img_name)
        await ctx.send(file=picture)


DaurUlang = ['koran', 'majalah', 'kardus', 
            'kertas printer', 'botol minuman', 'botol sabun',
            'kantong belanja plastik', 'kaleng minuman', 'kaleng makanan', 
            'tutup botol logam', 'botol kaca', 'toples', 'kaca jendela',
            'pakaian bekas', 'seprai', 'handuk', 'gorden'] 
                   

@bot.command()
async def sampah(ctx):
    await ctx.send('apa sampah yang mau di cek?')
    message = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    if message.lower() in DaurUlang:
        await ctx.send('Sampah anda bisa di daur ulang, untuk lebih lengap nya bisa baca:')
        await ctx.send('https://umsu.ac.id/berita/daur-ulang-sampah-pengertian-manfaat-dan-cara/')
    else:
        await ctx.send('sepertinya sampah itu tidak bisa di daur ulang, buanglah dengan bijak, atau olah ulang.')
        await ctx.send('bisa di bakar saja, atau dijadikan kompos jika organik')
        await ctx.send('sssh... kalau dibakar, harap berhati hati, jika api terlalu besar, lebih baik buang saja.')
        #ini bingung mau artikel apa, karena jarang ada, jadi kasih tips langsung aja ya...

bot.run("SecretToken")
