#モジュール
import discord
import random
import re

client = discord.Client()

flag=0

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
    "キモチェェ～～～！！！・。・＾",
]
random_w=[
    "** ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ**",
    "**(爆笑)**",
    "**(笑)**",
    "笑止！！",
    "＾＾",
    "ハハハハハハハハハハハハ",
   " マジですか!　フハハ!",
    "(　◠´つ◠｀) フェハハｗｗ",
    "(　◠´つ◠｀) フェハハｗｗ(　；◠´つ◠｀) わ、笑ってないっすよww",
]
    
@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('We have logged in as {0.user}'.format(client))
    print('------')

@client.event
async def on_message(message):
    # イベント入るたびに初期化はまずいのでグローバル変数で
    global flag
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が ~~だった場合
    if re.search("ぶり", message.content) or re.search("ブリ", message.content) or re.search("ぷり", message.content) or re.search("プリ", message.content):
        # 送信するメッセージをランダムで決める
        content = random.choice(random_contents)
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send(content)
    elif re.search("わに", message.content) or re.search("ワニ", message.content) :
        await message.channel.send(" 毎日読もう！100日後に殺すワニ :crocodile: \nhttp://aomoriumare.web.fc2.com/wani.html")
    elif re.search("おや", message.content) or re.search("寝", message.content) or  re.search("ねよ", message.content) or  re.search("ねる", message.content) or  re.search("oya", message.content):
        content=random.choice(random_sleep_contents)
        await message.channel.send(message.author.display_name +"君、"+ content)
    elif re.search("おは", message.content) or re.search('oha', message.content):
        await message.channel.send("おはよう！ " + message.author.display_name + "！！")
    elif re.search("こん", message.content) or re.search('kon', message.content):
        await message.channel.send("こんたま、" + message.author.display_name + "殿。" )
    elif re.search("さようなら", message.content) or re.search("さよなら", message.content):
        await message.channel.send("さようなら、" + message.author.display_name + "。" )
    elif re.search("おｋ", message.content) or re.search("ok", message.content):
        await message.channel.send("ok, google. :man_gesturing_ok:")
    elif re.search("。・", message.content) or  re.search("・。", message.content) or  re.search("。＾", message.content):
        content=random.choice(random_buri_contents)
        await message.channel.send(content)
    elif re.search("＞＜", message.content):
        await message.channel.send(" ＞＜；")
    elif re.search("かっこいい", message.content) or re.search("カッコイイ", message.content) or re.search("イケメン", message.content) or re.search("いけめん", message.content):
        await message.channel.send("** 呼んだかね？"+message.author.display_name +"君。**")
    elif re.search("うんこ", message.content) or re.search("うんち", message.content) or re.search("unko", message.content) or re.search("unnko", message.content):
        await message.channel.send(":poop:")
    elif re.search("ｗ", message.content) or re.search("笑", message.content):
        content=random.choice(random_w)
        await message.channel.send(content)
    elif re.search("ミキ", message.content) or re.search("miki", message.content) or re.search("みき", message.content):
        await message.channel.send("**mikki is dead!!!:skull_crossbones:**")

#ログを一掃する
    if message.content == '/clean':
        flag=1
        await message.channel.send("本当に一掃して良いのかい？\n良ければ  y を、ﾔﾊﾟﾘ止めとくなら n を入力するのだ・。・")
    #y を入力した場合
    if flag==1 and ((message.content=="y") or (message.content=="ｙ")):
        flag=0
        #ログ消去 purge()
        await message.channel.purge()
        await message.channel.send("そして残ったのは、化身のみであった…")
    #n を入力した場合
    elif flag==1 and ((message.content=="n") or (message.content=="ｎ")):
        flag=0
        await message.channel.send("賢明な判断だ・。・＾")


@client.event
async def on_message_delete(message):
   # channel = client.get_channel(372001297291018252)
    await message.channel.send(f"{message.author.name}さんのメッセージが削除されやした・。；\n```\n{message.content}\n```")

# メンバのステータスが変更されたら
@client.event
async def on_member_update(before, after):
    if before.status != after.status:
        msg = after.display_name + " が " + str(after.status) + "状態になったことをお知らせしやす・。・"
        channel = client.get_channel(372001297291018252)
        await after.send(msg)
       # await client.send_message(text_chat,msg)

#@client.event
#async def on_connect():
        
client.run("NjkxNTI4ODg1MjU0MjI1OTIw.Xn894A.Q4MIvwEL1x8Waxhucv9oYzlkj5I")
