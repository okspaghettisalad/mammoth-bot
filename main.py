import discord
from discord import client
from discord.ext import commands

with open('token.txt') as token:
    TOKEN = token.read()
    token.close

client = discord.Client()
bot = commands.Bot(command_prefix="!")

@bot.command()
async def incarnations(ctx, cmd=None, arg=None):
    if cmd == None:
        await ctx.send('\
**Commands:**\n\
> > !mammoth <type> | talking mammoth\n\
> > !doomsday | doomsday\n\
> > !noises | play noises\n\
> > !extinction | disconnect bot from channel\n\n\
> > !origins | bot info\n\
!incarnations <command> for more info*', reference=ctx.message)


    # each line gets its own send() because otherwise every embed would appear below all messages
    elif str(cmd) == 'mammoth':
        if arg == None:
            await ctx.send('\
**!mammoth <type> | mammoth image based on <type>**\n\
> > mammoth bot will reply to the message the command replyed to, or will reply to the last message otherwise\n\
> > *bot will also delete the command message\n\
**Types:**\n\
> > no type provided: the classic mammoth.\n\
> > now: NOW! (youtyu  be ,com /watch?v=T-BOPr7NXME)\n\
> > pe / desolate: it\'s an empty husk.\n\
> > ghastly: blink and chance never catching another glimpse\n\
> > ansenstor: they know where to throw a good party\n\
*!incarnations mammoth <type> for more info*\n\
> *(<type> = classic for defaul mammoth)*', reference=ctx.message)


        elif str(arg).lower() == 'classic': await ctx.send('\
https://media.discordapp.net/attachments/802674631717814312/915674691283333130/m.gif\n\
> **no type provided**', reference=ctx.message)

        elif str(arg).lower() == 'now': await ctx.send('\
https://cdn.discordapp.com/attachments/851897450385768503/931657627547611176/CRETH1.gif\n\
> **type:  now**', reference=ctx.message)

        elif str(arg).lower() == 'pe' or str(arg).lower() == 'desolate': await ctx.send('\
https://cdn.discordapp.com/attachments/818925860379557928/932031686932320326/IMG_0403.png\n\
> **type:  pe  |  type:  desolate**', reference=ctx.message)

        elif str(arg).lower() == 'ghastly': await ctx.send('\
https://cdn.discordapp.com/attachments/818925860379557928/932032179029028894/unknown.png\n\
> **type:  ghastly**', reference=ctx.message)

        elif str(arg).lower() == 'ancestor': await ctx.send('\
https://cdn.discordapp.com/attachments/818925860379557928/932034707410014278/IMG_0407.png\n\
> **type:  ancestor**', reference=ctx.message)


@bot.command()
async def mammoth(ctx, arg=None):
    if ctx.message.reference == None:
        ref = await ctx.channel.history(limit=2).flatten()
        ref = ref[1]
    else: ref = ctx.message.reference

    if str(arg).lower() == 'now':
        link = 'https://cdn.discordapp.com/attachments/851897450385768503/931657627547611176/CRETH1.gif'

    elif str(arg).lower() == 'desolate' or str(arg).lower() == 'pe':
        link = 'https://cdn.discordapp.com/attachments/818925860379557928/932031686932320326/IMG_0403.png'

    elif str(arg).lower() == 'ghastly':
        link = 'https://cdn.discordapp.com/attachments/818925860379557928/932032179029028894/unknown.png'

    elif str(arg).lower == 'ancestor':
        link = 'https://cdn.discordapp.com/attachments/818925860379557928/932034707410014278/IMG_0407.png'

    else: link = 'https://media.discordapp.net/attachments/802674631717814312/915674691283333130/m.gif'

    await ctx.send(content=link, reference=ref)
    await ctx.message.delete()


#https://stackoverflow.com/questions/67132135/get-voice-channel-id-from-user-id-discord-py
@bot.command()
async def doomsday(ctx, arg=None):
    try:
        channel = ctx.author.voice.channel
        if channel: # If user is in a channel
            global vc
            vc = await channel.connect() # Connect
            await ctx.send("await doomsday. 10 hours remain.")
        else:
            # bot in another channel
            await ctx.send('put me in the kind presense of a meteor')
        vc.play(discord.FFmpegPCMAudio(source='resources\clock_ticking.mp3', executable='C:\\ffmpeg\\bin\\ffmpeg.exe'))
    except AttributeError:
        # user not in channel
        await ctx.send('do you really expect to revel in doomsday without your own attendance.')


@bot.command()
async def noises(ctx):
    try:
        channel = ctx.author.voice.channel
        if channel: # If user is in a channel
            global vc
            vc = await channel.connect() # Connect
            await ctx.send("aoooooaahh.")
        else:
            # bot in another channel
            await ctx.send('put me in the kind presense of a meteor')
        vc.play(discord.FFmpegPCMAudio(source='resources\mammoth_sounds.mp3', executable='C:\\ffmpeg\\bin\\ffmpeg.exe'))
    except AttributeError:
        await ctx.send('do you really expect to revel the sounds without your own attendance.')


@bot.command()
async def extinction(ctx):
    if vc:
        await vc.disconnect()
        await ctx.send('oooooooooooaahhahaghagahgahagahahahhhhhahahhhhh *dies*')


@bot.command()
async def origins(ctx):
    await ctx.send('\
https://github.com/okspaghettisalad/mammoth-bot\n\
*bot by okspaghettisalad#0056*')


"""@client.event
async def on_ready():
    print(f'Logged in as {client}')"""

#client.run(TOKEN)
bot.run(TOKEN)