from discord.ext import commands

from japanese import JapaneseHelpCommand
from birthday import birth
from constants import TOKEN

PREFIX = '$'


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot = commands.Bot(
        command_prefix=PREFIX,
        help_command=JapaneseHelpCommand())
    bot.add_command(birth)
    bot.run(TOKEN)
