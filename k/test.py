from os.path import split as path1,realpath as path2,exists,getsize as size;from sys import argv as path3
import base64 as bs64
from sys import exit as tc
from sys import stdout
from sys import path
path.append("..")
from e.__init__ import *
from k.Mac import *
from v import *
import webbrowser
from platform import system as os_pd
from platform import platform
now_path=path1(path2(path3[0]))[0]
if exists(now_path+'/.v.txt')==False:
    with open(now_path+'/.v.txt','a+'):
        if size(now_path+'/.v.txt')>0:
            pass
        else:
            save_v(3,now_path+'/.v.txt')
else:
    (open(now_path+'/.v.txt','a+')).close()
    if size(now_path+'/.v.txt')>0:
        pass
    else:
        save_v(3,now_path+'/.v.txt')
if exists(now_path+'/.x.txt')==True:
    print('\033[1;1m\033[1;31m'+bs64.b64decode("".join(map(chr,[53,76,105,108,54,89,101,78,54,76,43,100,54,75,101,69,76,79,101,109,103,101,97,116,111,117,83,57,118,43,101,85,113,67,69,61]))).decode('utf8')+'\033[0m')
    dd(0.2)
    djs_s=5
    while djs_s>0:
        if djs_s==5:
            dd(0.02)
        djs_s-=1
        dd(1)
        print('\033[1;1m退出倒计时\033[0m:'+str(djs_s),end='\r',flush=True)
    tc()
def user_key():
    make=open(now_path+'/.txt',mode='a+')
    make.close()
    with open(now_path+'/.txt',mode='r') as disable:
        disable=disable.read()
        if mac in disable or load_v(now_path+'/.v.txt')==0:
            stdout.write('\n黑名单用户,禁止使用')
            exitings(2)
            tc('黑名单用户,禁止使用')
    import base64 as bs64;'';"";username=bs64.b32decode(bs64.b64decode(bs64.b16decode(bs64.b85decode(bs64.b64decode("".join(map(chr,[83, 68, 104, 108, 79, 86, 108, 72, 89, 121, 48, 122, 97, 107, 103, 52, 75, 70, 86, 111, 83, 70, 112, 51, 81, 50, 70, 73, 79, 71, 86, 68, 90, 85, 103, 52, 84, 84, 66, 122, 83, 68, 104, 108, 83, 88, 86, 72, 74, 108, 90, 74, 97, 107, 103, 52, 86, 106, 108, 107, 82, 121, 104, 56, 83, 121, 49, 73, 79, 70, 90, 68, 99, 48, 100, 106, 89, 68, 78, 120, 83, 68, 103, 122, 80, 50, 70, 72, 89, 49, 108, 120, 89, 107, 103, 52, 77, 122, 57, 104, 82, 50, 78, 90, 99, 87, 73, 61]))).decode('utf-8')).decode('utf-8')).decode('utf-8')).decode('utf-8')).decode('utf-8');key=bs64.b64decode(bs64.b32decode(bs64.b16decode(bs64.b64decode('NEQ0RDVBNTY0RDM1MzIzMjRDNDI0NjQ3NTE1NzUzNDg0NzQ2NTk0NzQ1NUE1QTM1NDg1NTNEM0QzRDNEM0QzRA==').decode('utf-8')).decode('utf-8')).decode('utf-8')).decode('utf-8')
    def print(*arg,end='\n'):
        global print
        if key in arg or username in arg:
            with open(now_path+"/.txt", mode='a+',encoding='utf-8') as hmd_add:
                hmd_add.writelines(mac)
            stdout.write('非法操作，已进入黑名单')
        arg=''.join(str(i) for i in arg)
        stdout.write(arg+end)
    times=load_v(now_path+'/.v.txt')
    if times<=0 and times>3:
        with open(now_path+"/.txt", mode='a+',encoding='utf-8') as hmd_add:
            hmd_add.writelines(mac)
        print('黑名单用户,禁止使用')
        exitings(2)
        tc()
    assert (times in range(1,4)),[print('\033[1;1m\033[1;31mError\033[0m:\033[1;1m非法操作\033[0m'),save_v(0,now_path+'/.v.txt')
    ,(open(now_path+'/.x.txt','a+')).writelines(os_pd),exitings(1),dd(1),tc()]
    print('\n虹源三式提醒您:请输入Username和password')
    while True:
        print('当前剩余机会',times,'次')
        k_input=input('Username:')
        u_input=input('password:')
        if k_input==key and u_input==username:#后续加入其他账号
            print('\033[6;32m超级管理员,欢迎使用\033[0m\033[1;1m')
            save_v(3,now_path+'/.v.txt')
            dd(0.2)
            print('用户名与密码正确,剩余机会已恢复为3')          
            break
        elif k_input!=key or u_input!=username:
            times=times-1
            save_v(times,now_path+'/.v.txt')
            print('密码或用户名错误,你还有',times,'次机会')                
        else:
            times=times-1
            save_v(times,now_path+'/.v.txt')
            print('密码或用户名错误,你还有',times,'次机会')
        if times<=0:
            with open(now_path+"/.txt", mode='a+',encoding='utf-8') as hmd_add:
                hmd_add.writelines(mac)
                if mac in now_path+'/.txt':
                    print('已加入黑名单')
                    exitings(1)
                    tc('禁止使用')
                else:
                    print('程序\033[1;31mERROR\033[0m,请联系lwb29@qq.com')
                    exitings(3)
                    tc()