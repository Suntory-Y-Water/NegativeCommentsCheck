import discord

# Bot のアクセストークン
DISCORD_BOT_TOKEN = "TOKEN"

# 接続に必要な設定/オブジェクト
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルに通知する
    print("YOUR DISCORD BOT is ACTIVE now!")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # Bot からのメッセージは無視する
    if message.author.bot:
        return

    # Hello と送られたら Hi! と返す
    if message.content == "Hello":
        await message.channel.send("Hi!")

    if message.content == "/sco":
        await message.channel.send("Hi!")

# Bot の起動と Discord サーバーへの接続
client.run(DISCORD_BOT_TOKEN)

