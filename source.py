import os
import discord

# Bot のアクセストークン
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# 接続に必要な設定/オブジェクト
intents = discord.Intents.all()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

# ネガティブな単語のリスト
negative_words = ["悲しい", "辛い", "もうだめだ"]

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルに通知する
    print("YOUR DISCORD BOT is ACTIVE now!")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # Bot からのメッセージは無視する
    if message.author == client.user:
        return

    # Hello と送られたら Hi! と返す
    if message.content.lower() == "hello":
        await message.channel.send("Hi!")

    # ネガティブな単語がメッセージに含まれているかチェックする
    for word in negative_words:
        if word in message.content:
            # ネガティブな単語が含まれている場合、返信を送信する
            await message.channel.send("ピピーっ！👮👮ネガティブ警察です🚨🚨🚨🙅🙅🙅🙅\nそのツイートは❗❗❗ネガティブな考えになるゾ😤😤😤💢💢💢")
            break

# Bot の起動と Discord サーバーへの接続
client.run(DISCORD_BOT_TOKEN)
