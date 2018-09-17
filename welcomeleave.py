import discord
from discord.ext import commands

class Welcomeleave:
    def __init__(self, client):
        self.client = client

    async def on_member_join(self, member):
        await self.client.change_presence(game=discord.Game(name=f"over {len(set(self.client.get_all_members()))} users - >help"))
        server = member.server
        channel = discord.utils.get(server.channels, name='welcome')
        embed = discord.Embed(color=0xdaff00)
        embed.add_field(name='Welcome **{}**'.format(member.name), value='You have joined **{}** Please notify and follow the channels and rules of this server!'.format(server.name), inline=False)
        await self.client.send_message(channel, embed=embed)

    async def on_member_remove(self, member):
        await self.client.change_presence(game=discord.Game(name=f"over {len(set(self.client.get_all_members()))} users - >help"))
        server = member.server
        channel = discord.utils.get(server.channels, name='welcome')
        embed = discord.Embed(color=0xdaff00)
        embed.add_field(name='Goodbye **{}**'.format(member.name), value='You will be missed!', inline=False)
        await self.client.send_message(channel, embed=embed)

def setup(client):
    client.add_cog(Welcomeleave(client))
