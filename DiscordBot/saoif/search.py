from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs4

# from japanese import JapaneseHelpCommand
# from constants import TOKEN
from constants import CORONA_URL

# PREFIX = '$'
PREFECTURE_DICT = {
    '北海道': 'hokkaido',
}


def remove_empty(a: list):
    return list(filter(None, a))


# bot = commands.Bot(
#         command_prefix=PREFIX,
#         self_bot=True,
#         help_command=JapaneseHelpCommand(prefix=PREFIX))


class Search(commands.Cog):
    """coronaや漢字の読みなど検索に関する機能を実装するクラス

    Args:
        bot(class): commands.Bot()

    Memo:
        commands (module): discord.ext.commandsのモジュール
        commands.Cog (class): すべての歯車が継承する必要のある基本クラス
        カテゴリを追加する際はcommands.Cogクラスの継承が必須
    """
    def __init__(self, bot, prefix):
        super().__init__()
        self.bot = bot
        self.prefix = prefix

    @commands.command()
    async def corona(self, ctx, prefecture=None):
        """コロナの最新情報を表示する

        Args: 引数self, ctxは指定しない
            prefecture (str): 県名（デフォルト: None）

        Example: 空白は全角でも半角でもOK！
            <prefix>corona <prefecture>: $corona nara
            <prefix>corona <prefecture>: $corona　奈良県

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        tmp = prefecture
        if prefecture in PREFECTURE_DICT:
            # 日本語でkeyに存在する
            prefecture = PREFECTURE_DICT[prefecture]

        if prefecture in PREFECTURE_DICT.values():
            # アルファベットでvalueに存在する
            # 情報を取得し、送信する
            print(prefecture)
        elif tmp is None:
            # 引数prefectureが入力されていない
            await ctx.send(f"```県名も入力してね```\n{self.prefix}help corona")
        else:
            await ctx.send(f"```{tmp} は存在しないよ```")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
# if __name__ == '__main__':
#     bot.add_cog(Search(bot=bot, prefix=PREFIX))
#     bot.run(TOKEN)
