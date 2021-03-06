from discord.ext import commands

# from japanese import JapaneseHelpCommand
# from constants import TOKEN

# PREFIX = '$'
BIRTHDAY_dict = {
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

# bot = commands.Bot(
#         command_prefix=PREFIX,
#         help_command=JapaneseHelpCommand(prefix=PREFIX))


class Birthday(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name='birthday')
    async def birth(self, ctx, character_name='all'):
        """キャラの誕生日を表示する

        Args:
        character_name (str): キャラ名（デフォルト: 'all'）

        Example:
        <prefix>birthday <character_name>: $birthday
        <prefix>birthday <character_name>: $birthday コハル
        """
        if character_name == 'all':
            msg = "```<キャラ名:   誕生日>\n"
            for key, value in BIRTHDAY_dict.items():
                msg += f"{key}:     {value}\n"
            await ctx.send(msg + "```")
        elif character_name in BIRTHDAY_dict:
            await ctx.send(f"```{BIRTHDAY_dict[character_name]}```")
        else:
            await ctx.send(character_name + 'は未登録です\n')


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
# if __name__ == '__main__':
#     bot.add_cog(Birthday(bot=bot))
#     bot.run(TOKEN)
