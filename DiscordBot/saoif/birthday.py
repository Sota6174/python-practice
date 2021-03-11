from discord.ext import commands

# from japanese import JapaneseHelpCommand
# from constants import TOKEN

# PREFIX = '$'

# bot = commands.Bot(
#         command_prefix=PREFIX,
#         help_command=JapaneseHelpCommand(prefix=PREFIX))


class Birthday(commands.Cog):
    """birthdayコマンドを実装するクラス

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
        self.birthday_dict = {
            'コハル': '2月23日',
            'フィリア': '3月31日',
            'アリス': '4月9日',
            'ユージオ': '4月10日',
            'リーファ': '4月19日',
            'リズベット': '5月18日',
            'ユウキ': '5月23日',
            'ユナ': '7月29日',
            'シノン': '8月21日',
            'アスナ': '9月30日',
            'シリカ': '10月4日',
            'キリト': '10月7日',
            'ストレア': '11月6日',
        }

    @commands.command()
    async def birthday(self, ctx, character_name='all'):
        """キャラの誕生日を表示する

        Args: 引数self, ctxは指定しない
            character_name (str): キャラ名（デフォルト: 'all'）

        Example:
            <prefix>birthday <character_name>: $birthday
            <prefix>birthday <character_name>: $birthday コハル

        Memo:
            ctx (object): discord.ext.commands.context.Context object
        """
        if character_name == 'all':
            msg = "```<キャラ名:   誕生日>\n"
            for key, value in self.birthday_dict.items():
                msg += f"{key}:     {value}\n"
            await ctx.send(msg + "```")
        elif character_name in self.birthday_dict:
            await ctx.send(f"```{self.birthday_dict[character_name]}```")
        else:
            await ctx.send(f"```{character_name}は未登録です\n```")


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
# if __name__ == '__main__':
#     bot.add_cog(Birthday(bot=bot))
#     bot.run(TOKEN)
