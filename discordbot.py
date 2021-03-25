# インストールした discord.py を読み込む
import discord
import time

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODI0NDU4OTIxNDQyODAzNzcy.YFvrNA.ue5YfuE_m_xqaWo59I0p0VUto78'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('準備完了')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # if message.content == '/あらせ':
    #     for num in range(20):
    #         await message.channel.send('@everyone')
    #         time.sleep(1);
    #         await message.channel.send('@everyone')
    #         time.sleep(1);
    #         if message.content == '/とまれ':
    #             break
    if message.content == message.content:
        mc = message.content
        mc = mc.split()
        if mc[0] == "#メンション" or mc[0] == "#めんしょん" or mc[0] == "#mention" or mc[0] == "#m":
            if int(mc[2]) >= 51:
                await message.channel.send(mc[2] + "回は多すぎだろ！？せめて50回以下にしとけよ！")
            else:
                forNum = int(mc[2])
                global counting 
                counting = 0
                for num in range(forNum):
                    counting = counting + 1
                    time.sleep(1)
                    await message.channel.send(str(counting) + " " + mc[1])
    
    if message.content == "#help":
        await message.channel.send("#m (メンションしたい人のメンション) (回数)")
        await message.channel.send("最大50回まで指定することができます。")
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
