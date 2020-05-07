import time

Prefix = '!!AI'
helpmsg = '''--------- MiaoNoAI ---------
§a 当前版本 1.0.0 开发来自CVS服务器
§7{0}§r显示帮助
§7{0} cod §6 <True,False> 是否开启鳕鱼AI
§7{0} salmon §6 <True,False> 是否开启鲑鱼AI
§7{0} tropical_fish §6 <True,False> 是否开启热带鱼AI
§7{0} pufferfish §6 <True,False> 是否开启河豚AI
§7{0} bat §6 <True,False> 是否开启蝙蝠AI
§7{0} rabbit §6 <True,False> 是否开启兔子AI
'''.format(Prefix)

cod = False
salmon = False
tropical_fish = False
pufferfish = False
bat = False
rabbit = False
isonload = False
sleeptime = 60

def on_server_stop(server):
    global isonload
    isonload = False
def on_unload(server):
    global isonload
    isonload = False
def server_tick(server):
    server.say("StartThread")
    tick = 0
    global isonload
    global sleeptime
    global isonload,cod,salmon,tropical_fish,pufferfish,bat,rabbit
    while True:
        time.sleep(sleeptime)
        if cod == True:
            server.execute('execute as @e[type=minecraft:cod] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        if salmon == True:
            server.execute('execute as @e[type=minecraft:salmon] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        if tropical_fish == True:
            server.execute('execute as @e[type=minecraft:tropical_fish] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        if pufferfish == True:
            server.execute('execute as @e[type=minecraft:pufferfish] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        if bat == True:
            server.execute('execute as @e[type=minecraft:bat] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        if rabbit == True:
            server.execute('execute as @e[type=minecraft:rabbit] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        if isonload == False:
            server.say('Break Loop')
            break
    
def on_info(server,info):
    global isonload,cod,salmon,tropical_fish,pufferfish,bat,rabbit
    if info.content == Prefix:
        server.reply(info, helpmsg);
    if info.content == "!!AI On":
        isonload = True
        server_tick(server)
    if info.content == "!!AI off":
        isonload = False
    if info.content == "!!AI cod True":
        server.reply(info,"§6[MiaoNoAI]已经开启 鳕鱼 AI")
        server.execute('execute as @e[type=cod] if data entity @s {NoAI:1b} run data modify entity @s NoAI set value 0b')
        cod = False
    if info.content == "!!AI cod False":
        server.reply(info,"§6[MiaoNoAI]已经关闭 鳕鱼 AI")
        server.execute('execute as @e[type=cod] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        cod = True
    if info.content == "!!AI salmon True":
        server.reply(info,"§6[MiaoNoAI]已经开启 鲑鱼 AI")
        server.execute('execute as @e[type=salmon] if data entity @s {NoAI:1b} run data modify entity @s NoAI set value 0b')
        salmon = False
    if info.content == "!!AI salmon False":
        server.reply(info,"§6[MiaoNoAI]已经关闭 鲑鱼 AI")
        server.execute('execute as @e[type=salmon] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        salmon = True
    if info.content == "!!AI tropical_fish True":
        server.reply(info,"§6[MiaoNoAI]已经开启 热带鱼 AI")
        server.execute('execute as @e[type=tropical_fish] if data entity @s {NoAI:1b} run data modify entity @s NoAI set value 0b')
        tropical_fish = False
    if info.content == "!!AI tropical_fish False":
        server.reply(info,"§6[MiaoNoAI]已经关闭 热带鱼 AI")
        server.execute('execute as @e[type=tropical_fish] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        tropical_fish = True
    if info.content == "!!AI pufferfish True":
        server.reply(info,"§6[MiaoNoAI]已经开启 河豚 AI")
        server.execute('execute as @e[type=pufferfish] if data entity @s {NoAI:1b} run data modify entity @s NoAI set value 0b')
        pufferfish = False
    if info.content == "!!AI pufferfish False":
        server.reply(info,"§6[MiaoNoAI]已经关闭 河豚 AI")
        server.execute('execute as @e[type=pufferfish] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        pufferfish = True
    if info.content == "!!AI bat True":
        server.reply(info,"§6[MiaoNoAI]已经开启 蝙蝠 AI")
        server.execute('execute as @e[type=bat] if data entity @s {NoAI:1b} run data modify entity @s NoAI set value 0b')
        bat = False
    if info.content == "!!AI bat False":
        server.reply(info,"§6[MiaoNoAI]已经关闭 蝙蝠 AI")
        server.execute('execute as @e[type=bat] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        bat = True
    if info.content == "!!AI rabbit True":
        server.reply(info,"§6[MiaoNoAI]已经开启 兔子 AI")
        server.execute('execute as @e[type=rabbit] if data entity @s {NoAI:1b} run data modify entity @s NoAI set value 0b')
        rabbit = False
    if info.content == "!!AI rabbit False":
        server.reply(info,"§6[MiaoNoAI]已经关闭 兔子 AI")
        server.execute('execute as @e[type=rabbit] unless data entity @s {NoAI:1b} run data modify entity @s NoAI set value 1b')
        rabbit = True