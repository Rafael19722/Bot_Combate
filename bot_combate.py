import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True #o que o bot usa pra ler as mensagens

bot = commands.Bot(command_prefix='!', intents =intents)

mensagem_temporaria = None #onde a mensagem fica guardada

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está online!')

@bot.command()
async def setar(ctx, *, mensagem): #comando pra setar a mensagem
    global mensagem_temporaria
    mensagem_temporaria = mensagem
    await ctx.send("Mensagem definida com sucesso!")

@bot.event
async def on_message(message): #evento pra soltar o resultado
    await bot.process_commands(message)

    global mensagem_temporaria

    if message.author == bot.user:
        return

    if message.content.lower() == "resultado":
        if mensagem_temporaria:
            await message.channel.send(f"{mensagem_temporaria}")
            mensagem_temporaria = None
        else:
            await message.channel.send("Não há nenhuma mensagem guardada.")

async def run_bot():
    await bot.start("*********")

asyncio.run(run_bot())
