# インストールした discord.py を読み込む
import discord

from constants import TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
# @client.event
# async def on_message(message):
#     # メッセージ送信者がBotだった場合は無視する
#     if message.author.bot:
#         return
#     # 「/neko」と発言したら「にゃーん」が返る処理
#     if message.content == '/neko':
#         await message.channel.send('にゃーん')


# 話しかけた人にBotが返事をする機能
async def reply(message):
    # 返信する非同期関数
    reply = f'{message.author.mention} 呼んだ?'
    await message.channel.send(reply)   # 返信メッセージを送信


@client.event
async def on_message(message):
    # メッセージのメンションにBotの名前があった時
    if client.user in message.mentions:
        await reply(message)


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    client.run(TOKEN)
