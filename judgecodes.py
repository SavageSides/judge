import discord
import time
import asyncio
import random
from discord.ext import commands

TOKEN = 'NDg5OTM1MzgzMTI4MzA5Nzcw.Dn9P8Q.EJKoGdlyUodp0bxtyao1HyISfyM'

client = commands.Bot(command_prefix='j!')
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in!')
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} Users - >help"))


extensions = ['moderation']
extensions = ['welcomeleave']
if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def install(extension):
    try:
        client.load_extension(extension)
        print(f'Loaded {extension}')
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def uninstall(extension):
    try:
        client.unload_extension(extension)
        print(f'Unloaded {extension}')
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.kick_members:
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.set_author(name='There is a known error!')
            embed.add_field(name=' :no_entry_sign: **Error**', value='The error was you did not specify a user!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Kick - Information')
            embed.add_field(name='**Server**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='**{}**'.format(author.name), inline=False)
            await client.send_message(user, embed=embed)
            await client.kick(user)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Kick - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':no_entry_sign: **Error**', value='You could not use this command because: Missing Permissions; ``Kick Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.ban_members:
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.set_author(name='There is a known error!')
            embed.add_field(name=' :no_entry_sign: **Error**', value='The error was you did not specify a user!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Ban - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='**{}**'.format(author.name), inline=False)
            await client.send_message(user, embed=embed)
            await client.ban(user)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Ban - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)

    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':no_entry_sign: **Error**', value='You could not use this command because: Missing Permissions; ``Ban Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.mute_members:
        MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.set_author(name='There is a known error!')
            embed.add_field(name=' :no_entry_sign: **Error**', value='The error was you did not specify a user!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.add_roles(user, MutedRole)
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Mute - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='{0}'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Mute - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':no_entry_sign: **Error**', value='You could not use this command because: Missing Permissions; ``Mute Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None, *, reason=None):
    author = ctx.message.author
    server = ctx.message.server
    if ctx.message.author.server_permissions.mute_members:
        MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
        if user is None:
            embed = discord.Embed(color=0xff0000)
            embed.set_author(name='There is a known error!')
            embed.add_field(name=' :no_entry_sign: **Error**', value='The error was you did not specify a user!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.remove_roles(user, MutedRole)
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Unmute - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='{0}'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='``{}``'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.send_message(user, embed=embed)
            #Sends the user a message when he is kicked!
            embed = discord.Embed(color=0xff00e6)
            embed.set_author(name='Unmute - Information')
            embed.add_field(name='**Server:**', value='**{}**'.format(server.name), inline=False)
            embed.add_field(name='**Reason:**', value='**{0}**'.format(reason), inline=True)
            embed.add_field(name='**Author:**', value='**{}**'.format(author.name), inline=False)
            embed.set_thumbnail(url=user.avatar_url)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':no_entry_sign: **Error**', value='You could not use this command because: Missing Permissions; ``Mute Members``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def nick(ctx, member:discord.User=None, *, newnick=None):
    author = ctx.message.author
    if ctx.message.author.server_permissions.manage_nicknames:
        if member is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the user you want me to change the nickname of!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            await client.change_nickname(member, newnick)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='{} Nickname has been changed.'.format(member.name))
            embed.add_field(name='Changed:', value='You have changed the nickname to: **{}**'.format(newnick), inline=True)
            await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Nicknames``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def clear(ctx, amount=None):
    if ctx.message.author.server_permissions.manage_messages:
        if amount is None:
            embed = discord.Embed(color=0xff0000)
            embed.add_field(name=':interrobang: **Error**', value='Oops! Please define the amount of messages you want me to delete!', inline=False)
            embed.set_footer(text='You need permission to continue if you dont have!')
            await client.say(embed=embed)
        else:
            channel = ctx.message.channel
            author = ctx.message.author
            messages = []
            async for message in self.client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            embed = discord.Embed(color=0x36393E)
            embed.set_author(name='Clear - Information')
            embed.add_field(name='Amount:', value='**I have deleted {} messages**'.format(amount), inline=False)
            embed.add_field(name='Author:', value='**{}**'.format(author.name), inline=False)
            msg = await client.say(embed=embed)
            await asyncio.sleep(5)
            await client.delete_message(msg)
    else:
        embed = discord.Embed(color=0xff0000)
        embed.add_field(name=':interrobang: **Error**', value='Oops! You cant use this command. Permission Required: ``Manage Messages``', inline=False)
        embed.set_footer(text='You cant use this command!')
        await self.client.say(embed=embed)

@client.command(pass_context=True)
async def crole(ctx, *, role):
    server = ctx.message.server
    author = ctx.message.author
    await client.create_role(server=server, name=role)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Creation!', value=f"**{role}** Has been created!", inline=False)
    embed.add_field(name='Author:', value=f"**{author}**", inline=True)
    await client.say(embed=embed)


@client.command(pass_context=True)
async def drole(ctx, *, name):
    author = ctx.message.author
    server = ctx.message.server
    role = discord.utils.get(ctx.message.server.roles, name=name)
    await client.delete_role(server=server, role=role)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Deletean!', value=f"**{name}** Has been deleted!", inline=False)
    embed.add_field(name='Author:', value=f"**{author}**", inline=True)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def channel(ctx, *, name):
    author = ctx.message.author
    server = ctx.message.server
    channel = discord.utils.get(ctx.message.server.channels, name=name)
    await client.create_channel(server=server, name=name)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Creation!', value=f"**{name}** Has been created!", inline=False)
    embed.add_field(name='Author:', value=f"**{author}**", inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def delchannel(ctx, *, name):
    author = ctx.message.author 
    server = ctx.message.server
    channel = discord.utils.get(ctx.message.server.channels, name=name)
    await client.delete_channel(server=server, name=name)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Deletion!', value=f"**{name}** Has been deleted!", inline=False)
    embed.add_field(name='Author:', value=f"**{author}**", inline=True)
    await client.say(embed=embed)





@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.set_author(name='Judge Help!')
    embed.add_field(name='Main Commands', value='1. Sevrerinfo: __Usage__: ``j!serverinfo`` \n 2. Info: __Usage__: ``j!info @Savage``', inline=False)
    embed.add_field(name=':tada: | Fun Commands :', value='1. Ping: __Usage__: ``j!ping`` \n 2. Jail: __Usage__: ``j!jail @Savage`` \n 3. Guilty: __Usage__: ``j!guilty @Savage`` \n 4. 8ball: __Usage__: ``j!8ball or eightball``', inline=True)
    embed.add_field(name=':game_die: | Mini Games : ', value='1. Roll: __Usage__: ``j!roll`` \n 2. Card: __Usage__: ``j!card`` \n 3. Slots: __Usage__: ``j!slots``', inline=False)
    embed.add_field(name=':map: | Legend :', value=':key: Is the Short Cut to the other page of the help command!', inline=True)
    embed.set_footer(text='Page 1/2')
    await client.say(embed=embed)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name=':tools: | Moderation Commands :', value='1. Kick: __Usage__: ``j!kick @Savage`` **Reason But you do not have to!** \n 2. Ban: __Usage__: ``j!ban @Savage`` **Reason But you do not have to!** \n 3. Mute: __Usage__: ``j!mute @Savage`` **Reason But you do not have to!** \n 4. Unmute: __Usage__: ``j!unmute @Savage`` \n 5. Clear: __Usage__: ``j!clear 5`` \n 6. Nick: __Usage__: ``j!nick @Savage Dad``', inline=False)
    embed.add_field(name=':lock:  | Utility Commands :', value='1. Invite: __Usage__: ``j!invite``', inline=False)
    embed.add_field(name=':warning: | Administration :', value='1. Welcome and Leave message! \n 2. Crole: __Usage__: ``j!crole <name>`` \n 3: Drole: __Usage__: ``j!crole <name>`` \n 4. Channel: __Usage__: ``j!channel <name>``', inline=True)
    embed.set_footer(text='Page 2/2')
    await client.say(embed=embed)



@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0xff00e6)
    embed.set_author(name="Server info")
    embed.add_field(name="**Name**", value=ctx.message.server.name, inline=True)
    embed.add_field(name="**ID**", value=ctx.message.server.id, inline=True)
    embed.add_field(name="**Roles**", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="**Members**", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0x36393E)
        embed.add_field(name=':interrobang: **Error**', value='Oops! Please specify a user for me to give info about!', inline=False)
        await client.say(embed=embed)
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x36393E)
    embed=discord.Embed(color=0xff00e6)
    embed.add_field(name="**Users Name Is:**", value="{}".format(user.name), inline=False)
    embed.add_field(name="**Highest Role Is:**", value="{}".format(user.top_role), inline=False)
    embed.add_field(name="**Users ID Is:**", value="{}".format(user.id), inline=False)
    embed.add_field(name="**Users Nickname Is:**", value="{}".format(user.nick), inline=False)
    embed.add_field(name="**Users Status Is:**", value="{}".format(user.status), inline=False)
    embed.add_field(name="**Users Game Is:**", value="{}".format(user.game), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)


@client.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.add_field(name='Incorrect Command!', value='```css\nThere was an error!\nWe will get the error ASAP```', inline=True)
        await client.send_message(channel, embed=embed)
    if isinstance(error, commands.NoPrivateMessage):
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.add_field(name='Unknown Error', value='```We beilive that you do not let random people text you!\nPlease enable your PM messages so you can see this amazing\nMessage!```', inline=True)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        embed = discord.Embed(title=":hourglass_flowing_sand:  Ping has been summoned:", description='**Latency: {}ms**'.format(round((t2-t1)*1000)), color=0x36393E)
        await client.say(embed=embed)

@client.command()
async def invite():
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.title = '**__Judge Bot Invite Link!__**'
    embed.url = 'https://discordapp.com/oauth2/authorize?client_id=489935383128309770&permissions=8&scope=bot'
    await client.say(embed=embed)


@client.command(pass_context=True)
async def guilty(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0xff0000)
        embed.set_author(name='There is a known error!')
        embed.add_field(name=' :no_entry_sign: **Error**', value='The error was you did not specify a user!', inline=False)
        await client.say(embed=embed)
    else:
        choices = [
        'You are guilty! **{}** Senteced 50 Years in Jail!'.format(user.name),
        'You are not guilty! **{}** You will be given a $10,000 For your actions!'.format(user.name),
        'You are sentenced to the electric chair! **{}**'.format(user.name),
        ]
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Court Dutie!', value=(random.choice(choices)), inline=False)
        embed.set_footer(text='GUILTY or NOT?!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def jail(ctx, user: discord.Member = None):
    if user is None:
        embed = discord.Embed(color=0xff0000)
        embed.set_author(name='There is a known error!')
        embed.add_field(name=' :no_entry_sign: **Error**', value='The error was you did not specify a user!', inline=False)
        await client.say(embed=embed)
    else:
        choices = [
        'NO! :hammer: **{}** is not guilty. How ever you are guilty of murduering his wife! :o'.format(user.name),
        'Guilty! Quite, Quite, Down! **{}** is put to jail for 60 Years for your rape and sexual assult!'.format(user.name)
        ]
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Jail Time Decisions!', value=(random.choice(choices)), inline=False)
        embed.set_footer(text='JAIL or NOT?!')
        await client.say(embed=embed)

@client.command(pass_context=True)
async def poll(ctx, channel_name = None, *, text):
    author = ctx.message.author
    channel = discord.utils.get(ctx.message.server.channels, name=channel_name)
    if channel_name is None:
        await client.say('Please Provide a channel!')
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Poll of the day by: **{}**'.format(author.name), value='{}'.format(text), inline=False)
        embed.set_footer(text='Poll!')
        message = await client.send_message(channel, embed=embed)
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Sucess!', value='Poll: **{}**'.format(text), inline=True)
        msg = await client.say(embed=embed)
        await asyncio.sleep(2)
        await client.delete_message(msg)

#Games
@client.command(pass_context=True)
async def roll(ctx):
    author = ctx.message.author
    choices = [
    'You rolled a ``6``!',
    'You rolled a ``2``!',
    'You rolled a ``3``!',
    'You rolled a ``5``!',
    'You rolled a ``4``!',
    'You rolled ``Snake Eyes``',
    ]
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.set_author(name='Rolling..')
    msg = await client.say(embed=embed)
    await asyncio.sleep(3)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='{} Has Rolled!'.format(author.name), value=(random.choice(choices)), inline=False)
    await client.edit_message(msg, embed=embed)

@client.command(pass_context=True)
async def card(ctx):
    author = ctx.message.author
    cards = [
    'You pulled a ``Hearts (red)``',
    'You pulled a ``Spades (black)``',
    'You pulled a ``Clubs (green)``',
    'You pulled a ``Clubs (green)``',
    'You pulled a ``Diamonds (yellow)``',
    ]
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.set_author(name='Picking..')
    msg = await client.say(embed=embed)
    await asyncio.sleep(3)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='{} has pulled'.format(author.name), value=(random.choice(cards)), inline=False)
    await client.edit_message(msg, embed=embed)

@client.command()
async def slots():
    slots = [
    ':cherries: :lemon: :cherries: :arrow_left:',
    ':lemon: :cherries: :lemon: :arrow_left:',
    ':lemon: :bell: :bell:  :arrow_left:',
    ':bell: :lemon: :grapes:  :arrow_left:',
    ':bell: :grapes: :bell: :arrow_left:',
    ':cherries: :bell: :bell: :arrow_left:',
    ':bell: :bell: :bell: :arrow_left:',
    ':grapes: :grapes: :grapes: :arrow_left:',
    ':lemon: :lemon: :lemon: :arrow_left:',
    ':cherries: :cherries: :cherries: :arrow_left:',
    ]
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Slotting', value='Almost there!', inline=False)
    msg = await client.say(embed=embed)
    await asyncio.sleep(.50)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name=':slot_machine: Slots - End :slot_machine:', value='You Got:', inline=False)
    embed.add_field(name='Slot Machine:', value='', inline=True)
    embed.set_footer(text='Slot Machine!')
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name=':slot_machine: Slots - End :slot_machine:', value='You Got:', inline=False)
    embed.add_field(name='Slot Machine:', value=(random.choice(slots)), inline=True)
    embed.set_footer(text='Slot Machine!')
    await client.edit_message(msg, embed=embed)
    await asyncio.sleep(.50)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name=':slot_machine: Slots - End :slot_machine:', value='You Got:', inline=False)
    embed.add_field(name='Slot Machine:', value=(random.choice(slots)), inline=True)
    embed.set_footer(text='Slot Machine!')
    await client.edit_message(msg, embed=embed)
    await asyncio.sleep(.50)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name=':slot_machine: Slots - End :slot_machine:', value='You Got:', inline=False)
    embed.add_field(name='Slot Machine:', value=(random.choice(slots)), inline=True)
    embed.set_footer(text='Slot Machine!')
    await client.edit_message(msg, embed=embed)
    await asyncio.sleep(.50)
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name=':slot_machine: Slots - End :slot_machine:', value='You Got:', inline=False)
    embed.add_field(name='Slot Machine:', value=(random.choice(slots)), inline=True)
    embed.add_field(name='Winning Number!', value=(random.choice(winner)), inline=False)
    embed.set_footer(text='Slot Machine!')
    await client.edit_message(msg, embed=embed)
    winner = [
    ':cherries: :lemon: :cherries: :arrow_left:',
    ':lemon: :cherries: :lemon: :arrow_left:',
    ':lemon: :bell: :bell:  :arrow_left:',
    ':bell: :lemon: :grapes:  :arrow_left:',
    ':bell: :grapes: :bell: :arrow_left:',
    ':cherries: :bell: :bell: :arrow_left:',
    ':bell: :bell: :bell: :arrow_left:',
    ':grapes: :grapes: :grapes: :arrow_left:',
    ':lemon: :lemon: :lemon: :arrow_left:',
    ':cherries: :cherries: :cherries: :arrow_left:',
    ]



@client.command(aliases=['8ball'])
async def eight_ball():
    choices = [
    'Does not look possible at all!',
    'Are you out of your mind? Never.',
    'Maybe, in 10000 Years.',
    'It looks like a good chance!',
    'Yup it is!',
    ]
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='8ball-Command :8ball: ', value=(random.choice(choices)), inline=False)
    embed.set_footer(text='--Judge Bot!--')
    await client.say(embed=embed)

@client.command(pass_context=True)
async def chelp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Command Help!', value='Please read through this help command and you will know alot!', inline=False)
    embed.add_field(name='Quick Description', value='Since my advanced help command isnt providing summaries of each **Command** \n I will tell you all of the meanings!', inline=True)
    embed.add_field(name='Slot Machine!', value='This is a working slot machine! Sadly we do not give money yet!', inline=True)
    embed.add_field(name='Card', value='Still in development!', inline=False)
    embed.add_field(name='Roll', value='This command will say a random number between \n 1-6!', inline=True)
    embed.add_field(name='8ball', value='The command will say 5 answers! Just see what it has to offer!', inline=False)
    embed.add_field(name='Jail & Guilty', value='This command will just say Guilty or no and Jail or  Not!', inline=True)
    await client.send_message(author, embed=embed)


@client.command(pass_context=True)
async def profile(ctx, user: discord.Member = None):
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Hi! You asked for an avatar!', value='{}s avatar!', inline=True)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text='The avatar!')
    await client.say(embed=embed)

@client.command()
async def add(left : int, right : int):
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Math Equations!', value='**{} + {} = {}**'.format(left, right, left + right), inline=True)
    await client.say(embed=embed)

@client.command()
async def sub(left : int, right : int):
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Math Equations!', value='**{} - {} = {}**'.format(left, right, left - right), inline=True)
    await client.say(embed=embed)

@client.command()
async def mul(left : int, right : int):
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Math Equations!', value='**{} x {} = {}**'.format(left, right, left * right), inline=True)
    await client.say(embed=embed)

@client.command()
async def div(left : int, right : int):
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Math Equations!', value='**{} / {} = {}**'.format(left, right, left / right), inline=True)
    await client.say(embed=embed)














#Welcome and Leave messages!

client.run(TOKEN)
