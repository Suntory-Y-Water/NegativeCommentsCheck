import os
import discord
import MeCab
from collections import defaultdict

# 日本語評価極性辞書の読み込み 
polarity_dict = defaultdict(lambda: 0)
with open('pn_ja_dic.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word, _, _, polarity = line.strip().split(':')
        polarity_dict[word] = float(polarity)

# MeCabの設定
tagger = MeCab.Tagger()

# Bot のアクセストークン
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

# 接続に必要な設定/オブジェクト
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルに通知する
    print("YOUR DISCORD BOT is ACTIVE now!")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    print(f"Received message: {message.content}")  # Debug message

    # Bot からのメッセージは無視する
    if message.author == client.user:
        return

    # メッセージの感情分析を行う
    node = tagger.parseToNode(message.content)
    sentiment = 0
    while node:
        sentiment += polarity_dict[node.surface]
        node = node.next

    # ネガティブな雰囲気を感じる場合、返信を送信する
    if sentiment < -0.7:  # 適切な閾値を設定してください
        await message.channel.send("ピピーっ！👮👮ネガティブ警察です🚨🚨🚨🙅🙅🙅🙅\nそのつぶやきは❗❗❗ネガティブな考えになるゾ😤😤😤💢💢💢")

# Bot の起動と Discord サーバーへの接続
client.run(DISCORD_BOT_TOKEN)