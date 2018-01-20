#! /home/pi/.pyenv/shims/python

# init
import discord
import random
import configparser


client = discord.Client()


# login
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# 応答
@client.event
async def on_message(message):

    # if mentioned me
    if client.user.mentioned_in(message):
        if client.user != message.author \
           and message.content.count('@everyone') == 0 \
           and message.content.count('@here') == 0:

            # debug
            # print(message.content);
            # if message.content.count('@everyone'):
            #     return 0;
            # if message.content.count('@here'):
            #     return 0;


            # target
            list = [  "わかばシューター"\
                     ,"もみじシューター"\
                     ,"スプラシューター"\
                     ,"スプラシューターコラボ"\
                     ,"プライムシューター"\
                     ,"プライムシューターコラボ"\
                     ,".52ガロン"\
                     ,".96ガロン"\
                     ,"ジェットスイーパー"\
                     ,"ジェットスイーパーカスタム"\
                     ,"シャープマーカー"\
                     ,"ボールドマーカー"\
                     ,"N-ZAP85"\
                     ,"N-ZAP89"\
                     ,"プロモデラーMG"\
                     ,"プロモデラーRG"\
                     ,"ホットブラスター"\
                     ,"ホットブラスターカスタム"\
                     ,"ロングブラスター"\
                     ,"ラピッドブラスター"\
                     ,"Rブラスターエリート"\
                     ,"ノヴァブラスター"\
                     ,"クラッシュブラスター"\
                     ,"L3リールガン"\
                     ,"L3リールガンD"\
                     ,"H3リールガン"\
                     ,"ボトルガイザー"\
                     ,"スプラローラー"\
                     ,"スプラローラーコラボ"\
                     ,"カーボンローラー"\
                     ,"ヴァリアブルローラー"\
                     ,"ダイナモローラー"\
                     ,"パブロ"\
                     ,"パブロ・ヒュー"\
                     ,"ホクサイ"\
                     ,"ホクサイ・ヒュー"\
                     ,"スプラチャージャー"\
                     ,"スプラスコープ"\
                     ,"スプラチャージャーコラボ"\
                     ,"スプラスコープコラボ"\
                     ,"リッター4K"\
                     ,"リッター4Kカスタム"\
                     ,"4Kスコープ"\
                     ,"4Kスコープカスタム"\
                     ,"ソイチューバー"\
                     ,"スクイックリンα"\
                     ,"14式竹筒銃・甲"\
                     ,"スプラマニューバー"\
                     ,"スプラマニューバーコラボ"\
                     ,"スパッタリー"\
                     ,"デュアルスイーパー"\
                     ,"ケルビン525"\
                     ,"バケットスロッシャー"\
                     ,"バケットスロッシャーコラボ"\
                     ,"ヒッセン"\
                     ,"スクリュースロッシャー"\
                     ,"バレルスピナー"\
                     ,"バレルスピナーデコ"\
                     ,"スプラスピナー"\
                     ,"ハイドラント"\
                     ,"パラシェルター"\
                     ,"キャンピングシェルター"\
                     ,"スパイガジェット "\
                     ,"スパッタリー・ヒュー"\
                     ,".52ガロンデコ"\

            ]


            # make random value
            n = random.randint(0,len(list)-1)
            print(n)

            # send message
            m = message.author.mention + " : " + list[n]
            await client.send_message(message.channel, m)


# run
inifile = configparser.ConfigParser()
inifile.read('./etc/token.conf', 'UTF-8')
TOKEN=inifile.get('test', 'WEAPON_SELECTOR')
client.run(TOKEN)

