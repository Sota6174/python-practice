import re

import discord
from discord.ext import commands

from japanese import JapaneseHelpCommand
from constants import TOKEN

PREFIX = '$'

intents = discord.Intents.default()     # デフォルトのIntentsオブジェクトを生成
intents.typing = False                  # typingを受け取らないように設定
intents.members = True
bot = commands.Bot(
    command_prefix=PREFIX,
    help_command=JapaneseHelpCommand(prefix=PREFIX),
    intents=intents)


class Greet(commands.Cog):
    """挨拶・callコマンドを実装するクラス

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
        self.member_list = []
        self.member_count = 0

    def set_member_list(self, ctx):
        if self.member_count < int(ctx.guild.member_count):
            print(self.bot..member.name)
            print(ctx.member.id)
            print(ctx.member.bot)
            print(ctx.member.nick)
            self.member_list = [str(i) for i in ctx.guild.members]
            self.member_count = int(ctx.guild.member_count)

    @commands.command()
    async def hello(self, ctx):
        """botが挨拶をする

        Args: 引数self, ctxは指定しない

        Example: textに空白が入ってもアルファベットでもOK！
            <prefix>goodbye <text>: $goodbye

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        msg = f"こんにちは、{ctx.author.name}さん！\n招き猫専属botだよ。よろしくね！"
        await ctx.send(f"```{msg}```")

    @commands.command()
    async def goodbye(self, ctx):
        """botが別れの挨拶をする

        Args: 引数self, ctxは指定しない

        Example: textに空白が入ってもアルファベットでもOK！
            <prefix>goodbye <text>: $goodbye

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        msg = f"じゃあね、{ctx.author.name}さん！\nいつでもディスコードで待ってるよ"
        await ctx.send(f"```{msg}```")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """新しいメンバーが入ってきたときに挨拶する

        Memo:
            ctx (object): discord.ext.commands.context.Context object
            新しいメンバーが入ってきたときにこのイベントハンドラが呼ばれる
        """
        channel = member.guild.system_channel
        if channel is not None:
            msg = f"ギルド招き猫にようこそ！{member.mention} さん！"
            await channel.send(f"```{msg}```")

    @commands.command(aliases=['summon', '召喚', 'call', '呼び出し'])
    async def summon_member(self, ctx, *args):
        """指定された人全員にメンション付きのメッセージを送る

        Args: 引数self, ctxは指定しない
            args (member & message): 召喚メンバーと召喚メッセージ

        Example: 空白は半角でも全角でもOK！
            <prefix>summon <args>: $summon マイン
            <prefix>summon <args>: $summon マイン Lucifer ディスコに来て！
            <prefix>summon <args>: $summon マイン Lucifer "ディスコ　来て！"

        Memo:
            コマンドは'summon'以外にも'summon_member', '召喚', 'call', '呼び出し'が使える
            ctx (object): discord.ext.commands.context.Context object
            メンバー名、メッセージ名同士の間は空白を空ける（全角・半角OK！）
            メッセージは最後に書く
            メッセージに空白を入れたい場合はメッセージを半角の'(シングルクォーテーション)か"(ダブルクォーテーション)で囲む
        """
        self.set_member_list(ctx)
        member_taple = args[:-1]
        message = args[-1]


        # @commands.Cog.listener()
        # async def on_voice_state_update(self):
        #     """VCに人が出入りしたときに挨拶を表示する

        #     Memo:
        #         ctx (object): discord.ext.commands.context.Context object
        #         VCに人が出入りしたときにこのイベントハンドラが呼ばれる
        #     """

# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    bot.add_cog(Greet(bot=bot))
    bot.run(TOKEN)
