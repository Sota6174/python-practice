# インストールした discord.py を読み込む
import discord

from constants import TOKEN, TEXT_CHANNEL_ID

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    # テキストチャンネルの方でBotがおはよう！という
    channel = client.get_channel(int(TEXT_CHANNEL_ID))
    await channel.send('おはよう！')


# メッセージ受信時に動作する処理
# 話しかけた人にBotが返事をする機能
async def reply(message):
    # 返信する非同期関数
    reply = f'{message.author.mention} 呼んだ?'
    await message.channel.send(reply)


# コマンドに対応するリストデータを取得する関数を定義
def get_data(message):
    command = message.content
    data_dict = {
        '/neko': 'にゃーん',
        '/members': message.guild.members,                  # メンバーのリスト
        '/roles': message.guild.roles,                      # 役職のリスト
        '/text_channels': message.guild.text_channels,      # テキストチャンネルのリスト
        '/voice_channels': message.guild.voice_channels,    # ボイスチャンネルのリスト
        '/category_channels': message.guild.categories,     # カテゴリチャンネルのリスト
    }
    return data_dict.get(command, '無効なコマンドです')


# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message, channel_name):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # # 「/neko」と発言したら「にゃーん」が返る処理
    # if message.content == '/neko':
    #     await message.channel.send('にゃーん')

    # メッセージのメンションにBotの名前があった時
    if client.user in message.mentions:
        await reply(message)

    # 「/mkch」と発言したらnewという名前のテキストチャンネルを作成する処理
    if message.content.startswith('/mkch'):
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name='new')

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)

    # 管理者権限を持つ人が「/cleanup」と発言したらそのテキストチャンネルのメッセージログを削除する処理
    if message.content == '/cleanup':
        # 管理者権限を持つ人が入力した場合
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        # 管理者権限を持たない人が入力した場合
        else:
            await message.channel.send('何様のつもり？')

    # data_dict内のkeyと一致したら、keyに対応する値を返す
    # 一致しなかったら、'無効なコマンドです'と返す
    await message.channel.send(get_data(message))


# Botの起動とDiscordサーバーへの接続（このファイルが実行されたとき）
if __name__ == '__main__':
    client.run(TOKEN)
