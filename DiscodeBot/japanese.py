from discord.ext import commands

# from constants import TOKEN

# PREFIX = '$'


class JapaneseHelpCommand(commands.DefaultHelpCommand):
    """Botのhelpコマンドを日本語表示にする

    Args:
        commands.DefaultHelpCommand (クラス名): botのhelpコマンドのデフォルト値が設定されている
                                                HelpCommandクラスを継承したクラス
    """
    def __init__(self, prefix):
        super().__init__()
        self.PREFIX = prefix
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示する"

    def get_ending_note(self):
        return (f"コマンドの説明を個別に取得したい場合:\n"
                f"各コマンドの説明: {self.PREFIX}help <コマンド名>\n"
                f"各カテゴリの説明: {self.PREFIX}help <カテゴリ名>\n")


# if __name__ == '__main__':
#     bot = commands.Bot(
#         command_prefix=PREFIX,
#         help_command=JapaneseHelpCommand())
#     bot.run(TOKEN)
