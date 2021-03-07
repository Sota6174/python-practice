# DiscordBot/pracitce

- Discode内で使えるBotを作ってみる

# 環境

- pthon 3.9.1
- 外部ライブラリ：requirements.txtに記載
- TOKENやCLIENT_IDなどは.envファイルに記載し、constants.pyでまとめて呼び出し、変数に格納している
- Botのコードではconstants.pyから変数を呼び出し、TOKENなどを利用している

# メモ

### test.py
- [discord.pyの公式ドキュメント](https://discordpy.readthedocs.io/en/stable/quickstart.html)のクイックスタートから引用

### test2.py
- [qiitaの記事](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)から引用

### test3-*.py
- discord.pyのext.commandsフレームワークで表示されるhelpコマンドを日本語で表示する
- ext.commandsフレームワークは、helpコマンドを自動で実装してくれる
- helpコマンドは、"""～"""で囲まれた部分をコマンドの説明として採用（複数行のコメントがある場合は一行目のみ）
- プレフィックスなどの細かい設定はcommands.DefaultHelpCommandで定義されているデフォルト値を変更して行う
- commands.DefaultHelpCommandの値はcommands.Bot()でクラスを初期化した時に設定される
- commands.Bot()クラスを先に定義して、その後にイベントハンドラを@bot.command()デコレータで定義すると、そのbotクラスのイベントハンドラとして自動で追加していってくれる
- クラス内でイベントハンドラを定義しないと、helpコマンドの説明を表示した時に、自作したイベントハンドラが全てNo Category:で表示されてしまう
- [参考](https://cod-sushi.com/discord-py-help-command-japanese/)
- [discord.ext.commandsの公式ドキュメント](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html)


### Discode Bot作業記録
- [Issueのリンク](https://github.com/Sota6174/python-practice/issues/30)
