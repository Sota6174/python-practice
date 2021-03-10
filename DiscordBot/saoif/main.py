from discord.ext import commands

from japanese import JapaneseHelpCommand
from birthday import Birthday
from search import Search
from todo import ToDo
from constants import TOKEN

# PREFIX = '$'
PREFIX = '!'


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot = commands.Bot(
        command_prefix=PREFIX,
        help_command=JapaneseHelpCommand(prefix=PREFIX))
    bot.add_cog(Birthday(bot=bot))
    bot.add_cog(ToDo(bot=bot))
    bot.add_cog(Search(bot=bot, prefix=PREFIX))
    bot.run(TOKEN)
