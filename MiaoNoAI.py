import time

Prefix = '!!AI'
helpmsg = '''--------- MiaoNoAI ---------
§a 当前版本 1.0.3 开发来自CVS服务器
§7{0}§r显示帮助
§7{0} cod §6 <True,False> 是否开启鳕鱼AI
§7{0} salmon §6 <True,False> 是否开启鲑鱼AI
§7{0} tropical_fish §6 <True,False> 是否开启热带鱼AI
§7{0} pufferfish §6 <True,False> 是否开启河豚AI
§7{0} bat §6 <True,False> 是否开启蝙蝠AI
§7{0} rabbit §6 <True,False> 是否开启兔子AI
§7{0} On §6 是否自动关闭已经设置过的生物的AI
§7{0} Off §6 关闭自动设置已经设置过的生物的AI
§7{0} clear on §6 自动清除高占用CPU生物 ->蝙蝠 -> 鱼
§7{0} Off §6 关闭自动清除高占用CPU生物 ->蝙蝠 -> 鱼
§2 最后编辑时间为2020/05/08 23:33
'''.format(Prefix)

cod = False
salmon = False
tropical_fish = False
pufferfish = False
bat = False
rabbit = False
isonload = False
sleeptime = 60
clearentities = False
cleartick = 15

def on_server_stop(server):
    global isonload,clearentities
    clearentities = False
    isonload = False
def on_unload(server):
    global isonload,clearentities
    clearentities = False
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
def ClearEntities(server):
    global cleartick,clearentities
    while True:
        time.sleep(1)
        cleartick = cleartick - 1
        if cleartick == 0:
            server.execute("gamerule doMobLoot false")
            server.execute("kill @e[type=bat]")
            server.execute("kill @e[type=salmon]")
            server.execute("kill @e[type=tropical_fish]")
            server.execute("kill @e[type=pufferfish]")
            server.execute("kill @e[type=cod]")
            server.execute("gamerule doMobLoot true")
            server.say("§6[MiaoNoAI]已经清理全部实体 -> 蝙蝠 鱼类");
            cleartick == 300
        if cleartick == 60:
            server.say("§6[MiaoNoAI]即将在2§l60秒后清理实体")
        if cleartick == 30:
            server.say("§6[MiaoNoAI]即将在§2§l30秒§6后清理实体")
        if cleartick == 10:
            server.say("§6[MiaoNoAI]即将在§2§l10秒§6后清理实体")
        if cleartick == 5:
            server.say("§6[MiaoNoAI]即将在§2§l5秒§6后清理实体")
        if cleartick == 4:
            server.say("§6[MiaoNoAI]即将在§2§l4秒§6后清理实体")
        if cleartick == 3:
            server.say("§6[MiaoNoAI]即将在§2§l3秒§6后清理实体")
        if cleartick == 2:
            server.say("§6[MiaoNoAI]即将在§2§l2秒§6后清理实体")
        if cleartick == 1:
            server.say("§6[MiaoNoAI]即将在§2§l1秒§6后清理实体")
        if clearentities == False:
            break
def on_info(server,info):
    global isonload,cod,salmon,tropical_fish,pufferfish,bat,rabbit,clearentities
    if info.content == Prefix:
        server.reply(info, helpmsg);
    if info.content == "!!AI On":
        isonload = True
        server.say("§6[MiaoNoAI]自动关闭实体AI已经开启")
        server_tick(server)
        
    if info.content == "!!AI off":
        isonload = False
        server.say("§6[MiaoNoAI]自动关闭实体AI已经关闭")
    if info.content == "!!AI clear on":
        clearentities = True
        server.say("§6[MiaoNoAI]自动清理高占用实体已经开启")
        ClearEntities(server)
        
    if info.content == "!!AI clear off":
        clearentities = False
        server.say("§6[MiaoNoAI]自动清理高占用实体已经关闭")
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