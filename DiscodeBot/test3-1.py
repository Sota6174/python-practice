from discord.ext import commands

from constants import TOKEN

PREFIX = '$'


class Greet(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """出会いのあいさつをする"""
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @commands.command()
    async def goodbye(self, ctx):
        """別れの挨拶をする"""
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot = commands.Bot(command_prefix=PREFIX)
    # ヘルプコマンドの表示を簡易化したいとき
    # bot = commands.Bot(command_prefix=PREFIX, help_command=commands.MinimalHelpCommand())
    bot.add_cog(Greet(bot=bot))
    bot.run(TOKEN)
