from __init__ import * #排好顺序start变量覆盖
from p.__init__ import *
from k.test import *
from p.y import *
from p.yh import *
from p.yz import *
from p.qt import *
from p.beginnings import *

  
def pypi_org():
    s=socket.socket()
    s.settimeout(10)
    try:
        readme=open(now_path+'/.net.txt','a+')
        status = s.connect_ex(('pypi.org',443))
        if status == 0:
            s.close()
            return True
            if size(now_path+'/.net.txt')==0:
                save_v(1,now_path+'/.net.txt')
            else:
                pass
            if load_v(now_path+'/.net.txt')==1:
                import webbrowser
                open_web=6
                while open_web in range(1,7):
                    open_web=open_web-1
                    print('\r将在%ds后打开浏览器查看sycc的介绍,请勿关闭'%open_web,end='',flush=True)
                    dd(1)
                print('\n')
                webbrowser.open(link, new=0, autoraise=True)
                save_v(0,now_path+'/.net.txt') 
            else:
                pass
        else:
            pass
    except Exception as e:
        pass
def main():
    pdios();wf();A();pypi_org();user_key();#A()
    #print(version)
    print('\033[7;36m本次开始使用时间:\033[0m','\033[7;32m',start,'\b\b'+'\033[0m','\033[1;1m')
    clear_cls=0
    while True:
        clear_cls+=1
        if clear_cls>1:
            if os1=='Linux':
                os.system('clear')
            elif os2=='Windows' or 'Win32':
                os.system("cls")
        print('\033[1;1m','\b【虹源三式】'.center(5))
        print("===== 切换/选择模式，请选择 =====\n模式1.计算关于"+y_font+"的计算(输入1执行)\n模式2.计算关于"+yz_font+"的计算(输入2执行)\n模式3.计算关于\033[6;35m圆环\033[0m\033[1;1m的计算(输入3执行)\n模式4.计算关于"+qt_font+"的计算(输入4执行)\n输入其他字符退出\n")
        yyy=input('请选择模式(输入数字):')
        try:
            yyy=eval(yyy)
        except (IOError,ValueError,TypeError,SyntaxError,EOFError,NameError,KeyboardInterrupt):
            print('请输入正确数字')
        except ZeroDivisionError:
            print('除数不能为0')
        if yyy==1:
            part_y() 
        elif yyy==2:
            part_yz()
        elif yyy==3:
            part_yh()
        elif yyy==4:
            part_qt()            
        else:
            end=sj.now()-start
            print('即将\033[10;31m退出\033[0m,','本次使用时间:',end,'\n程序将在5秒后关闭,谢谢使用')
            exitings(5)
            tc()