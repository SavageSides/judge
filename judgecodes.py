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
            await client.add_roles(user, MutedRole)
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
            async for message in client.logs_from(channel, limit=int(amount)):
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
        await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.set_author(name='Judge Help!')
    embed.add_field(name='Main Commands', value='1. Sevrerinfo: __Usage__: ``j!serverinfo`` \n 2. Info: __Usage__: ``j!info @Savage``', inline=False)
    embed.add_field(name='Fun Commands', value='1. Ping: __Usage__: ``j!ping`` \n 2. Jail: __Usage__: ``j!jail @Savage`` \n 3. Guilty: __Usage__: ``j!guilty @Savage``', inline=True)
    embed.add_field(name='Legend', value=':key: Is the Short Cut to the other page of the help command!', inline=True)
    embed.set_footer(text='Page 1/2')
    msg = await client.say(embed=embed)
    await client.add_reaction(msg, "\U0001f511")
    await client.add_reaction(msg, "\U0001f3c1")
    await client.wait_for_reaction("\U0001f511")
    embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
    embed.add_field(name='Moderation Commands', value='1. Kick: __Usage__: ``j!kick @Savage`` **Reason But you do not have to!** \n 2. Ban: __Usage__: ``j!ban @Savage`` **Reason But you do not have to!** \n 3. Mute: __Usage__: ``j!mute @Savage`` **Reason But you do not have to!** \n 4. Unmute: __Usage__: ``j!unmute @Savage`` \n 5. Clear: __Usage__: ``j!clear 5`` \n Nick: __Usage__: ``j!nick @Savage Dad``', inline=False)
    embed.add_field(name='Utility Commands')
    embed.set_footer(text='Page 2/2')
    await client.edit_message(msg, embed=embed)


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
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Incorrect Command!', value='```There was an error!\nWe will get the error ASAP```', inline=True)
        await client.send_message(channel, embed=embed)
    if isinstance(error, commands.NoPrivateMessage):
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Unknown Error', value='```We beilive that you do not let random people text you!\nPlease enable your PM messages so you can see this amazing\nMessage!```', inline=True)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        embed=discord.Embed(title=":hourglass_flowing_sand:  Ping has been summoned:", description='**Latency: {}ms**'.format(round((t2-t1)*1000)), color=0x36393E)
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

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

#Welcome and Leave messages!


@client.event
async def on_member_join(member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')
    embed = discord.Embed(color=0xdaff00)
    embed.add_field(name='Welcome **{}**'.format(member.name), value='You have joined **{}** Please notify and follow the channels and rules of this server!'.format(server.name), inline=False)
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')
    embed = discord.Embed(color=0xdaff00)
    embed.add_field(name='Goodbye **{}**'.format(member.name), value='You will be missed!', inline=False)
    await client.send_message(channel, embed=embed)

client.run(TOKEN)
