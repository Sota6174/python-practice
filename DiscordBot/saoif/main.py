import discord
from discord.ext import commands

from japanese import JapaneseHelpCommand
from greet import Greet
from birthday import Birthday
from search import Search
from todo import ToDo
from constants import TOKEN

# PREFIX = '$'
PREFIX = '!'


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    # intents = discord.Intents.all()     # すべてTrueのIntentsオブジェクトを生成
    intents = discord.Intents.default()     # デフォルトのIntentsオブジェクトを生成
    intents.typing = False              # typingを受け取らないように設定
    bot = commands.Bot(
        command_prefix=PREFIX,
        help_command=JapaneseHelpCommand(prefix=PREFIX),
        intents=intents)
    bot.add_cog(Greet(bot=bot))
    bot.add_cog(Birthday(bot=bot))
    bot.add_cog(ToDo(bot=bot))
    bot.add_cog(Search(bot=bot, prefix=PREFIX))
    bot.run(TOKEN)
