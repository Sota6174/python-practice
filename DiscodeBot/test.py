import discord

from constants import TOKEN

# clientのインスタンス生成（Discodeへの接続に必要）
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('We have logged in as {0.user}'.format(client))


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # client.user(Bot自身)からのメッセージは無視
    if message.author == client.user:
        return

    # $hello で始まるメッセージが来たら Hello! を送信する
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    client.run(TOKEN)
