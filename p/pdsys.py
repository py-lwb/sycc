from colorama import init
from time import sleep as dd
from sys import exit as tc
import platform as pd1
from sys import platform as pd2
from random import choice
import subprocess
os1=pd1.system()#大写
os2=pd2#
colors=[
'\033[1;51m'
'\033[1;43m','\033[1;42m','\033[1;31m',
'\033[1;32m','\033[1;33m','\033[1;34m',
'\033[1;35m','\033[1;36m','\033[1;345m',
'\033[1;46m','\033[1;41m',
'\033[1;45m']

def pdios():
    if (os1=='Windows') or (os2=='windows'):
        init(autoreset=True)
        choice_color=choice(colors)
        subprocess.call("cls", shell=True)
        print('\033[1;1m'+('sycc:'.title().center(5))+'欢迎%sWindows%s用户\n'%(choice_color,'\033[0m'))
        
    elif (os1=='Linux') or (os2=='linux'):
        init(autoreset=False)
        subprocess.call("clear", shell=True)
            #print('\033[1;1m'+('sycc:'.title().center(5))+'\033[0m欢迎%sLinux用户\n'%colors[i])
        choice_color=choice(colors)
        print('\033[1;1m'+('sycc:'.title().center(5))+'\033[0m欢迎%sLinux%s用户\n'%(choice_color,'\033[0m'))
            #print(choice_color.split('\033['))
        dd(1)      
    else:
        print('虹源三式提醒您:不支持该系统,请联系lwb29@qq.com')
        dd(2)
        tc('exit')
