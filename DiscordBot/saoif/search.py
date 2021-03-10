from discord.ext import commands
import requests
from bs4 import BeautifulSoup as bs4

# from japanese import JapaneseHelpCommand
# from constants import TOKEN
from constants import CORONA_URL

# PREFIX = '$'
PREFECTURE_DICT = {
    '北海道': 'hokkaido',
    '青森県': 'aomori',
    '岩手県': 'iwate',
    '宮城県': 'miyagi',
    '秋田県': 'akita',
    '山形県': 'yamagata',
    '福島県': 'fukushima',
    '茨城県': 'ibaraki',
    '栃木県': 'tochigi',
    '群馬県': 'gunma',
    '埼玉県': 'saitama',
    '千葉県': 'chiba',
    '東京都': 'tokyo',
    '神奈川県': 'kanagawa',
    '新潟県': 'niigata',
    '富山県': 'toyama',
    '石川県': 'ishikawa',
    '福井県': 'fukui',
    '山梨県': 'yamanashi',
    '長野県': 'nagano',
    '岐阜県': 'gifu',
    '静岡県': 'shizuoka',
    '愛知県': 'aichi',
    '三重県': 'mie',
    '滋賀県': 'shiga',
    '京都府': 'kyoto',
    '大阪府': 'osaka',
    '兵庫県': 'hyogo',
    '奈良県': 'nara',
    '和歌山県': 'wakayama',
    '鳥取県': 'tottori',
    '島根県': 'shimane',
    '岡山県': 'okayama',
    '広島県': 'hiroshima',
    '山口県': 'yamaguchi',
    '徳島県': 'tokushima',
    '香川県': 'kagawa',
    '愛媛県': 'ehime',
    '高知県': 'kochi',
    '福岡県': 'fukuoka',
    '佐賀県': 'saga',
    '長崎県': 'nagasaki',
    '熊本県': 'kumamoto',
    '大分県': 'oita',
    '宮崎県': 'miyazaki',
    '鹿児島県': 'kagoshima',
    '沖縄県': 'okinawa',
}


def remove_empty(a: list):
    return list(filter(None, a))


def set_corona_message(value: str, data: list):
    if len(data[0]) == 3:
        if value == '感染者数':
            msg = f"感染者数：\n\t累計 {data[0][0]}人\n\t{data[0][1]}人\n\t{data[0][2]}人\n"
        elif value == '回復者数':
            msg = f"回復者数：\n\t累計 {data[1][0]}人\n\t{data[1][1]}人\n\t{data[1][2]}人\n"
        elif value == '死亡者数':
            msg = f"死亡者数：\n\t累計 {data[2][0]}人\n\t{data[2][1]}人\n\t{data[2][2]}人\n"
        else:
            msg = f"感染者数：\n\t累計 {data[0][0]}人\n\t{data[0][1]}人\n"
            msg += f"回復者数：\n\t累計 {data[1][0]}人\n\t{data[1][1]}人\n"
            msg += f"死亡者数：\n\t累計 {data[2][0]}人\n\t{data[2][1]}人\n"
    else:
        if value == '感染者数':
            msg = f"感染者数：\n\t累計 {data[0][0]}人\n\t{data[0][1]}人\n"
        elif value == '回復者数':
            msg = f"回復者数：\n\t累計 {data[1][0]}人\n\t{data[1][1]}人\n"
        elif value == '死亡者数':
            msg = f"死亡者数：\n\t累計 {data[2][0]}人\n\t{data[2][1]}人\n"
        else:
            msg = f"感染者数：\n\t累計 {data[0][0]}人\n\t{data[0][1]}人\n"
            msg += f"回復者数：\n\t累計 {data[1][0]}人\n\t{data[1][1]}人\n"
            msg += f"死亡者数：\n\t累計 {data[2][0]}人\n\t{data[2][1]}人\n"

    return msg

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
    async def corona(self, ctx, prefecture=None, value='all'):
        """コロナの最新情報を表示する

        Args: 引数self, ctxは指定しない
            prefecture (str): 県名（デフォルト: None）
            value (str): 欲しい値：感染者数・回復者数・死亡者数（デフォルト: all）

        Example: 空白は全角でも半角でもOK！
            <prefix>corona <prefecture>: $corona tokyo
            <prefix>corona <prefecture>: $corona　東京都
            <prefix>corona <prefecture>: $corona　東京都　感染者数
            <prefix>corona <prefecture>: $corona　東京都　死亡者数

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        if prefecture in PREFECTURE_DICT:
            # 日本語でkeyに存在する
            prefecture = PREFECTURE_DICT[prefecture]

        if prefecture in PREFECTURE_DICT.values():
            # アルファベットでvalueに存在する
            # 情報を取得し、送信する
            html = requests.get(CORONA_URL + prefecture)
            soup = bs4(html.content, 'html.parser')
            updated_time = soup.find('p').text.replace('更新時間', '更新日時')
            data = [tag.text.splitlines() for tag in soup(class_='dialog')]
            data = list(map(remove_empty, data))
            prefecture = [k for k, v in PREFECTURE_DICT.items() if v == prefecture][0]
            msg = f"<{prefecture}のコロナ状況>\n\n{updated_time}\n\n"
            msg += set_corona_message(value, data)
            await ctx.send(f"```{msg}```")
        elif prefecture is None:
            # 引数prefectureが入力されていない
            await ctx.send(f"```県名も入力してね\nコマンドの説明：{self.prefix}help corona```")
        else:
            await ctx.send(f"```{prefecture} は存在しないよ```")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
# if __name__ == '__main__':
#     bot.add_cog(Search(bot=bot, prefix=PREFIX))
#     bot.run(TOKEN)
