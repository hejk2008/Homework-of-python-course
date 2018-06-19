#! /usr/bin/env python3
# coding: utf-8

'''
虚拟宠物猫游戏
在达成题目要求的前提下，增加了手动存档读档、死亡后删档并保存游玩记录等功能。
加入了游戏秘籍以便调试，用法如下：
    首先输入"cheatmode"，来激活调试模式，然后输入"property=value"
    例如输入"health=100"可以将生命值调整为100
    可以调节的属性有hungry, happiness, health和hours
有关os.system的代码仅在 Windows和Linux 下测试过，因此对于mac的兼容性未知。
'''

__author__ = 'hejk2008 (Jack He)'

import json
import random
import threading
import os
import sys

def fun_timer():
    '''每5秒执行一次，并同时计算宠物的各项数值'''
    global timer, hours, hungry, happiness, health, hungry_increase, happiness_increase, health_increase, doing, cmd, days
    hours += 1
    if hours > 23:
        hours = 0
        days += 1
    if hours < 8 and doing == '我醒着但很无聊...':
        happiness_increase = 0
        hungry_increase = 1
        health_increase = 0
        doing = '我在睡觉...'
    if hours >= 8 and doing == '我在睡觉...':
        happiness_increase = -1
        hungry_increase = 2
        health_increase = 0
        doing = '我醒着但很无聊...'
    if hungry > 80 or hungry < 20:
        happiness += happiness_increase
        hungry += hungry_increase
        health += health_increase - 2
    elif happiness < 20:
        happiness += happiness_increase
        hungry += hungry_increase
        health += health_increase - 1
    else:
        happiness += happiness_increase
        hungry += hungry_increase
        health += health_increase
    if hungry > 100:
        hungry = 100
    if happiness > 100:
        happiness = 100
    if health > 100:
        health = 100
    if hungry < 0:
        hungry = 0
    if happiness < 0:
        happiness = 0
    if health < 0:
        health = 0
    timer = threading.Timer(5.0, fun_timer)#5s执行一次fun_timer
    timer.start()


def fun_save():
    '''用于写入存档的函数'''
    global hours, hungry, happiness, health, hungry_increase, happiness_increase, health_increase, doing, days
    statusdict = {'happiness': happiness, 'hungry': hungry, 'health': health,
                  'happiness_increase': happiness_increase, 'hungry_increase': hungry_increase, 'health_increase': health_increase,
                  'doing': doing, 'hours': hours, 'days': days}
    with open('save.json', 'w', encoding='utf-8') as statusjson:
        statusjson.write(json.dumps(statusdict, indent=2))


def fun_load():
    '''用于加载存档的函数'''
    global hours, hungry, happiness, health, hungry_increase, happiness_increase, health_increase, doing, days
    while True:
        try:
            statusdict = {}
            with open('save.json', 'r', encoding='utf-8') as statusjson:
                statusdict = json.loads(statusjson.read())
            hours = statusdict['hours']
            happiness = statusdict['happiness']
            hungry = statusdict['hungry']
            health = statusdict['health']
            happiness_increase = statusdict['happiness_increase']
            hungry_increase = statusdict['hungry_increase']
            health_increase = statusdict['health_increase']
            doing = statusdict['doing']
            days = statusdict['days']
            break
        except FileNotFoundError:       #当存档不存在时，新建存档
            hours = random.randint(0,23)
            happiness = random.randint(20,80)       #为防止过高的游戏难度，随机数取值控制在20~80
            hungry = random.randint(20,80)
            health = random.randint(20,80)
            if hours >= 8:
                happiness_increase = -2
                hungry_increase = 1
                health_increase = 0
                doing = '我醒着但很无聊...'
            else:
                happiness_increase = 0
                hungry_increase = 1
                health_increase = 0
                doing = '我在睡觉...'
            days = 0
            break
        except (json.decoder.JSONDecodeError, KeyError) as err:     #当存档损坏时，提供三种选择：开始新游戏、手动检查存档、退出程序
            print('\n###SAVE FILE CORRUPTED!###\nError:', err)
            choice = input('Enter "new" to start a new game, "check" to check the savefile, "quit" to quit the program. ')
            if choice == 'new':
                os.remove('save.json')
                continue
            elif choice == 'check':        #自动打开文本编辑器以便于修正存档 
                if sys.platform == 'win32':
                    os.system('notepad save.json')
                    os.system('pause')
                elif sys.platform == 'linux':
                    os.system('vi save.json')
                    input('Press Enter after correction.')
                else:
                    input('Please correct the file manually, and then press Enter.')
                continue
            elif choice == 'quit':
                exit()
            else:
                print('Please enter new/check/quit.')
                continue


def fun_status():
    '''返回宠物的状态'''
    global hungry, happiness, health
    hungry_progress = '*' * (hungry // 2) + '-' * (50 - hungry // 2)
    happiness_progress = '*' * (happiness // 2) + '-' * (50 - happiness // 2)
    health_progress = '*' * (health // 2) + '-' * (50 - health // 2)
    return '\n当前时间：%d点\n我当前的状态：%s\nHappiness:     Sad %s Happy(%.3d)\nHungry:       Full %s Hungry(%.3d)\nHealth:       Sick %s Healthy(%.3d)\n'\
        % (hours, doing, happiness_progress, happiness, hungry_progress, hungry, health_progress, health)


def main():
    '''主函数'''
    welcome = '''我的名字叫做Tommy，一只可爱的猫咪，喵喵~~\n你可以和我一起散步，玩耍，你也需要给我好吃的东西，带我去看病，也可以让我发呆...'''
    helpmsg = '''
commands:
1. walk: 散步
2. play: 玩耍
3. feed: 喂我
4. seedoctor: 看医生
5. letalone: 让我独自一人
6. status: 查看我的状态
7. bye: 不想看到我
8. help: 打印命令帮助
9. save: 存档
10. load: 读档
11. cheatmode: 打开调试模式'''
    print(welcome)
    print(helpmsg)
    #初始化参数
    global hours, hungry, happiness, health, hungry_increase, happiness_increase, health_increase, doing, cmd, days
    fun_load()
    print(fun_status())
    fun_timer()  #启动定时器
    cheat_flag = False      #This flag should be switched to Flase after development.
    #开始游戏循环
    while True:
        cmd = input('你想: ')
        #游戏秘籍代码
        if cmd == 'cheatmode':
            cheat_flag = True
            print('\nCheat mode activated!\nEnter "property=value" to change it.\nAcceptable properties:hungry, happiness, health, hours.\n')
            continue
        if cheat_flag:
            if cmd.split(sep='=')[0] == 'hungry':
                hungry = int(cmd.split(sep='=')[1])
                print('\nCheat applied!\n', fun_status())
                continue
            if cmd.split(sep='=')[0] == 'happiness':
                happiness = int(cmd.split(sep='=')[1])
                print('\nCheat applied!\n', fun_status())
                continue
            if cmd.split(sep='=')[0] == 'health':
                health = int(cmd.split(sep='=')[1])
                print('\nCheat applied!\n', fun_status())
                continue
            if cmd.split(sep='=')[0] == 'hours':
                hours = int(cmd.split(sep='=')[1])
                print('\nCheat applied!\n', fun_status())
                continue
        #常规控制代码
        if cmd in ('walk', 'play', 'feed', 'seedoctor') and doing == '我在睡觉...':
            if input('\n你确认要吵醒我吗？我在睡觉，你要是坚持吵醒我，我会不高兴的！(y表示是/其它表示不是) ') == 'y':
                happiness += -4
                if happiness < 0:
                    happiness = 0
            else:
                print('')
                continue
        if cmd == 'walk':
            happiness_increase = 0
            hungry_increase = 3
            health_increase = 1
            doing = '我在散步...'
            print('\n' + doing + '\n')
        elif cmd == 'play':
            happiness_increase = 1
            hungry_increase = 3
            health_increase = 0
            doing = '我在玩耍...'
            print('\n' + doing + '\n')
        elif cmd == 'feed':
            happiness_increase = 0
            hungry_increase = -3
            health_increase = 0
            doing = '我在吃饭...'
            print('\n'+doing+'\n')
        elif cmd == 'seedoctor':
            happiness_increase = 0
            hungry_increase = 0
            health_increase = 4
            doing = '我在看医生...'
            print('\n'+doing+'\n')
        elif cmd == 'letalone':
            if 0 <= hours < 8:
                happiness_increase = 0
                hungry_increase = 1
                health_increase = 0
                doing = '我在睡觉...'
                print('\n'+doing+'\n')
            else:
                happiness_increase = -1
                hungry_increase = 2
                health_increase = 0
                doing = '我醒着但很无聊...'
                print('\n'+doing+'\n')
        elif cmd == 'status':
            print(fun_status())
        elif cmd == 'help':     #打印帮助信息
            print(helpmsg)
        elif cmd == 'save':     #手动存档
            fun_save()
            print('\nSaved!\n')
        elif cmd == 'load':     #手动读档
            fun_load()
            print('\nLoaded!')
            print(fun_status())
        elif cmd == 'bye':
            print('\n记得来找我哦~Bye.....')
            fun_save()
            timer.cancel()
            break
        else:
            print('\n我不懂你在说什么\n')
        if health <= 0:      #死亡后删除存档并保存用户姓名和游戏时长
            print('Your pet has died!')
            timer.cancel()
            name = input('Please input your name:')
            with open('statistics.txt', 'a') as statistics:
                print('You have kept the pet for %d days!'%days)
                print('%s\t\t%s days'%(name, days), file=statistics)
            try:
                os.remove('save.json')
            except FileNotFoundError:
                pass
            break


if __name__ == '__main__':
    main()
