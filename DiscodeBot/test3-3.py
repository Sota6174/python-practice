from discord.ext import commands

from japanese import JapaneseHelpCommand
from constants import TOKEN

PREFIX = '$'
bot = commands.Bot(
        command_prefix=PREFIX,
        help_command=JapaneseHelpCommand())


@bot.command()
async def hello(ctx):
    """出会いのあいさつをする

    Args:
    ctx (commands.Context): コマンドを入力した人

    Example:
    <prefix>hello: $hello
    """
    await ctx.send(f"どうも、{ctx.author.name}さん!")


@bot.command()
async def goodbye(ctx):
    """別れの挨拶をする

    Args:
    ctx (commands.Context): コマンドを入力した人

    Example:
    <prefix>goodbye: $goodbye
    """
    await ctx.send(f"じゃあね、{ctx.author.name}さん!")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot.run(TOKEN)
