import discord
import asyncio
import ast
import datetime
import os
import aiohttp
import random
import traceback
from discord.ext import commands

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)

class Ext:
    def __init__(self):
        self.channels = []
        self.starttime = self.timeset()

    def timeset(self):
        start_time = datetime.datetime.utcnow()
        return start_time

    async def reply(self, ctx, msg):
        await ctx.channel.send(f'{ctx.author.mention}, {msg}')
    
    def uptime(self):
        return datetime.datetime.utcnow() - self.starttime

    async def eval(self, ctx, bot, cmd):
        _cmd = cmd
        try:
            fn_name = "_eval_expr"
            cmd = cmd.strip("` ")
            cmd_in = cmd
            cmd = "\n".join(f"    {i}" for i in cmd.splitlines())
            body = f"async def {fn_name}():\n{cmd}"
            parsed = ast.parse(body)
            body = parsed.body[0].body
            insert_returns(body)
            env = {
                'bot': bot,
                'discord': discord,
                'commands': commands,
                'ctx': ctx,
                '__import__': __import__,
                'self.bot' : bot,
                'message' : ctx.message
            }
            exec(compile(parsed, filename="<ast>", mode="exec"), env)
            result = eval(f"{fn_name}()", env)
            embed = discord.Embed(title = 'Value')
            embed.add_field(name='📥 Input', value=f'```py\n{_cmd}```', inline=False)
            embed.add_field(name='📤 Output', value=f'```{result}```', inline=False)
            embed.add_field(name="🔧 Type 🔧",value=f"```py\n{type(result)}```",inline=False)
            embed.add_field(name="🏓 Latency 🏓",value=f'```py\n{str((datetime.datetime.now()-ctx.message.created_at)*1000).split(":")[2]}\n```',inline=False)
            return embed
        except:
            embed = discord.Embed(title = 'Value')
            embed.add_field(name='📥 Input', value=f'```py\n{_cmd}```', inline=False)
            embed.add_field(name='📤 Output', value=f'```{traceback.format_exc()}```', inline=False)
            embed.add_field(name="🔧 Type 🔧",value=f"```py\nError!```",inline=False)
            embed.add_field(name="🏓 Latency 🏓",value=f'```py\n{str((datetime.datetime.now()-ctx.message.created_at)*1000).split(":")[2]}\n```',inline=False)
            return embed

    async def aioreq(self, url: str, header = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url = url, header = header) as r:
                data = await r.json()
            return data