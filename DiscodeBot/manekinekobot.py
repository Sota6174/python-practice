from discord.ext import commands

from japanese import JapaneseHelpCommand
from birthday import Birthday
from constants import TOKEN

PREFIX = '$'

bot = commands.Bot(
        command_prefix=PREFIX,
        help_command=JapaneseHelpCommand(prefix=PREFIX))


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot.add_cog(Birthday(bot=bot))
    bot.run(TOKEN)
