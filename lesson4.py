#モジュール
import discord
import random
import re

client = discord.Client()
# ランダムで送るメッセージの一覧 ※ここに書き足すことでランダムに選ぶ内容を増やせる
random_contents = [
    "にゃーん",
    "わん！",
    "コケッコッコー",
    "ぶりぶり！",
    "！・。・！",
    "・。・？",
    "パパウパウパウ！",
    "ぶりゅう・。・",
    "パオ～～ン",
    "ガオー",
    "ゲコゲコ",
]
random_sleep_contents = [
    "おすやみさない！！",
    "さいなら。",
    "オヤスミキモ",
    "Good night:last_quarter_moon_with_face:",
    "また明日～",
]
random_buri_contents = [
    "ぶりゅう・。・",
    "・。。・",
    "呼んだ・。・？" ,
    "ぶりぶり～・。・＾",
    "！・。・！",
    "ぶりゅううう",
    "ブリュウナク:dragon:",
]

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

@client.event
async def on_message(message):
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が 鳴いて だった場合
    if re.search("ぶり", message.content) or re.search("ブリ", message.content) or re.search("ぷり", message.content) or re.search("プリ", message.content):
        # 送信するメッセージをランダムで決める
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif re.search("わに", message.content) or re.search("ワニ", message.content) :
        await message.channel.send(" 毎日読もう！100日後に殺すワニ :crocodile: \nhttp://aomoriumare.web.fc2.com/wani.html")
    elif re.search("おや", message.content) or re.search("寝", message.content) or  re.search("ねよ", message.content) or  re.search("ねる", message.content) or  re.search('oya', message.content):
        content=random.choice(random_sleep_contents)
        await message.channel.send(message.author.nick +"君、"+ content)
    elif re.search("おは", message.content) or re.search('oha', message.content):
        await message.channel.send("おはよう！ " + message.author.nick + "！！")
    elif re.search("こん", message.content) or re.search('kon', message.content):
        await message.channel.send("こんたま、" + message.author.nick + "殿。" )
    elif re.search("おｋ", message.content) or re.search("ok", message.content):
        await message.channel.send("ok, google. :man_gesturing_ok:")
    elif re.search("。・", message.content) or  re.search("・。", message.content) or  re.search("。＾", message.content):
        content=random.choice(random_buri_contents)
        await message.channel.send(content)
    elif re.search("＞＜", message.content):
        await message.channel.send(" ＞＜；")
    elif re.search("かっこいい", message.content or re.search("カッコイイ", message.content)):
        await message.channel.send("** 呼んだかね？"+message.author.nick+"君。**")
    elif re.search("うんこ", message.content) or re.search("うんち", message.content):
        await message.channel.send(":poop:")
        
client.run("NjkxNTI4ODg1MjU0MjI1OTIw.XniH-w.GI5rmObnKJFNUSq75qPFXnNKiz0")
