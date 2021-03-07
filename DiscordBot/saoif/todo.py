import random

from discord.ext import commands

# from japanese import JapaneseHelpCommand
# from constants import TOKEN

PREFIX = '$'
FLOOR_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '20', '25', '27', '35', '37', '40', '47', '掲示板', '黒鉄宮']
TODO_list = ['熟練', 'ボス周回', 'ナンパ（ギルド勧誘）', '瓶集め', 'ポテチ食べる', '寝る！']
CONVERT_NUMBER_TABLE = dict((0xFF10 + ch, 0x0030 + ch) for ch in range(10))


def set_todo(floor):
    if floor == '黒鉄宮':
        todo = '黒カオス周回'
    else:
        todo = random.choice(TODO_list)
    return todo


# bot = commands.Bot(
#         command_prefix=PREFIX,
#         help_command=JapaneseHelpCommand(prefix=PREFIX))


class ToDo(commands.Cog):
    """何する？コマンドを実装するクラス

    Args:
        commands (module): module discord.ext.commands
        commands.Cog (class): The base class that all cogs must inherit from
    """
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='何する？')
    async def show_what_to_do(self, ctx, floor=None):
        """今日やることを表示する

        Args:
        ctx (context.Context): discord.ext.commands.context.Context object
        floor (str): 階層or掲示板（デフォルト: None）

        Example: 空白・数字は全角でもOK！
        <prefix>何する？ <floor>: $何する？
        <prefix>何する？ <floor>: $何する？ 40
        <prefix>何する？　<floor>: $何する？　40
        <prefix>何する？ <floor>: $何する？ 掲示板
        <prefix>何する？ <floor>: $何する？ 黒鉄球
        """
        if floor is None:
            floor = random.choice(FLOOR_list)
        else:
            # 全角で入力されたfloorを半角数字に変換する
            # 半角の数字・掲示板・黒鉄球はそのまま
            floor = floor.translate(CONVERT_NUMBER_TABLE)
        todo = set_todo(floor)

        if floor not in FLOOR_list:
            await ctx.send(f"{floor} は存在しないよ")
        else:
            if len(floor) < 3:
                floor += '層'
            greet = f"乙カレー  {ctx.author.name}！\n"
            await ctx.send(f"```{greet}今日は{floor}で{todo}```")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
# if __name__ == '__main__':
#     bot.add_cog(ToDo(bot=bot))
#     bot.run(TOKEN)
