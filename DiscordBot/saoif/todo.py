import random

from discord.ext import commands

# from japanese import JapaneseHelpCommand
# from constants import TOKEN

# PREFIX = '$'
NUMBER_TO_FULLWIDTH = dict((0x0030 + ch, 0xFF10 + ch) for ch in range(10))

# bot = commands.Bot(
#         command_prefix=PREFIX,
#         help_command=JapaneseHelpCommand(prefix=PREFIX))


class ToDo(commands.Cog):
    """何する？・寝れま１０！・ギルイベコマンドを実装するクラス

    Args:
        bot(class): commands.Bot()

    Memo:
        commands (module): discord.ext.commandsのモジュール
        commands.Cog (class): すべての歯車が継承する必要のある基本クラス
        カテゴリを追加する際はcommands.Cogクラスの継承が必須
    """
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.area_list = [
            '１', '２', '３', '４', '５', '６', '７', '８', '９', '１０',
            '１１', '１２', '１３', '１４', '２０', '２２', '２５', '２７',
            '３５', '３７', '４０', '４７',
            '掲示板', '黒鉄宮']
        self.todo_list = [
            '熟練', 'ボス周回', 'ナンパ（ギルド勧誘）', '瓶集め', 'ポテチ食べる', '寝る！']
        self.task_list = [
            '小瓶', '中瓶', 'mod開放の欠片Ⅱ・SS', '赤冥晶の欠片', '橙冥晶の欠片',
            '大瓶', 'mod開放の欠片Ⅲ', '黄冥晶の欠片', '緑冥晶の欠片',
            '武装石', 'コアメタル', '混沌の赤冥晶', '混沌の橙冥晶', '混沌の黄冥晶', '混沌の緑冥晶', '熟練度']
        self.weapon_list = [
            '片手直剣', '片手細剣', '片手棍', '短剣', '両手斧', '両手槍', '弓', '盾']

    def set_todo(self, floor: str):
        if floor == '黒鉄宮':
            todo = '黒カオス周回'
        elif floor == '２２':
            todo = '釣り'
        else:
            todo = random.choice(self.todo_list)
        return todo

    def set_quota(self, quantity: int):
        if quantity == 11:
            task = '釣り'
        elif quantity > 5:
            task = self.task_list[random.randint(0, 4)]
        elif quantity > 1:
            task = self.task_list[random.randint(0, 8)]
        else:
            task = random.choice(self.task_list)

        # self.area_listの全角数字の'１'～'１０'を流用
        quantity = self.area_list[quantity-1]
        if task == '釣り':
            quota = f"{task}１００回"
        elif task == 'mod開放の欠片Ⅲ':
            quota = f"{task}・{random.choice(self.weapon_list[:-1])}を{quantity}個ドロップ"
        elif task == '熟練':
            quota = f"{random.choice(self.weapon_list)}の{task}{quantity}up"
        else:
            quota = f"{task}を{quantity}個ドロップ"
        return quota

    @commands.command(name='何する？')
    async def show_what_to_do(self, ctx, floor=None):
        """今日やることを表示する

        Args: 引数self, ctxは指定しない
            floor (str): 階層or掲示板（デフォルト: None）

        Example: 空白・数字は全角でも半角でもOK！
            <prefix>何する？ <floor>: $何する？
            <prefix>何する？ <floor>: $何する？ 40
            <prefix>何する？　<floor>: $何する？　４０
            <prefix>何する？ <floor>: $何する？ 掲示板
            <prefix>何する？ <floor>: $何する？ 黒鉄球

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        # if floor is None:
        #     floor = random.choice(self.area_list)
        # else:
        #     # 半角で入力されたfloorを全角数字に変換する
        #     # 掲示板・黒鉄球・全角の数字はそのまま
        #     floor = floor.translate(NUMBER_TO_FULLWIDTH)
        floor = random.choice(self.area_list) if floor is None else floor.translate(NUMBER_TO_FULLWIDTH)
        if floor not in self.area_list:
            floor_list = str(list(range(1, 101))).translate(NUMBER_TO_FULLWIDTH)
            if floor in floor_list:
                floor += '層'
            await ctx.send(f"```{floor} は存在しないよ```")
        else:
            todo = self.set_todo(floor)
            if len(floor) < 3:
                floor += '層'
            greet = f"乙カレー  {ctx.author.name}！\n"
            await ctx.send(f"```{greet}今日は{floor}で{todo}```")

    @commands.command(name='寝れま１０！')
    async def quota(self, ctx):
        """今日のノルマを表示する

        Args: 引数self, ctxは指定しない

        Example:
            <prefix>寝れま１０！: $寝れま１０！

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        quantity = random.randint(1, 11)
        quota = self.set_quota(quantity) + "するまで寝れま１０！"
        greet = f"乙カレー  {ctx.author.name}！\n"
        await ctx.send(f"```{greet}今日のノルマ：{quota}\nファイト！```")

    @commands.command(name='ギルイベ')
    async def guild_event(self, ctx):
        """ギルイベの日程・招き猫ギルドの予定を表示する

        Args: 引数self, ctxは指定しない

        Example: 空白は全角でも半角でもOK！
            <prefix>ギルイベ: $ギルイベ

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
# if __name__ == '__main__':
#     bot.add_cog(ToDo(bot=bot))
#     bot.run(TOKEN)
