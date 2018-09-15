import discord
import time
import asyncio
import random
from discord.ext import commands


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
    embed = discord.Embed(color=0xff00e6)
    embed.set_author(name='Judge Help!')
    embed.add_field(name=':hammer_pick: | Moderation :', value='Nick: __Usage__: j!nick @Savage Nickname \n Mute: __Usage__: j!mute @Savage \n Unmute: __Usage__: j!unmute @Savage \n Clear: __Usage__: j!clear 5 \n Ban: __Usage__: j!ban @Savage \n Kick: __Usage__: j!kick @Savage', inline=False)
    embed.add_field(name=':tada: | Party/Fun :', value='Ping', inline=True)
    embed.add_field(name=':third_place: | Court :', value='Guilty: __Usage__: j!guilty @Savage \n Jail: __Usage__: j!jail @Savage', inline=False)
    embed.add_field(name=':thinking: | Message Sending :', value='Poll: __Usage__: j!poll <channel> <poll>', inline=True)
    msg = await client.send_message(author, embed=embed)
    await client.add_reaction(msg, "↔️")



@client.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name='Incorrect Command!', value='Please use a command next time! \n Type ``>help`` For real commands!', inline=True)
        await client.send_message(channel, embed=embed)

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

@client.event
async def on_member_join(member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')
    await client.send_message(channel, 'Hey {} Welcome to {}!'.format(member.mention, server.name))

@client.event
async def on_member_remove(member):
    await client.change_presence(game=discord.Game(name=f"over {len(set(client.get_all_members()))} users - >help"))
    server = member.server
    channel = discord.utils.get(server.channels, name='welcome')
    await client.send_message(channel, '{} Has just left {} :('.format(member.mention, server.name))

if not os.environ.get('TOKEN'):
    print("no token found!")
client.run(os.environ.get('TOKEN').strip('"'))
