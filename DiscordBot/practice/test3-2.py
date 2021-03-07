from discord.ext import commands

from japanese import JapaneseHelpCommand
from constants import TOKEN

PREFIX = '$'


class Greet(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """出会いのあいさつをする

        Args:
        ctx (commands.Context): コマンドを入力した人

        Example:
        <prefix>hello: $hello
        """
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @commands.command()
    async def goodbye(self, ctx):
        """別れの挨拶をする

        Args:
        ctx (commands.Context): コマンドを入力した人

        Example:
        <prefix>goodbye: $goodbye
        """
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot = commands.Bot(
        command_prefix=PREFIX,
        help_command=JapaneseHelpCommand())
    bot.add_cog(Greet(bot=bot))
    bot.run(TOKEN)
