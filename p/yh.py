from .__init__ import *
from .pdsys import os1,os2
from sys import path
path.append('..')
from e.__init__ import *
pai2='π'
def yh_error(p1,p2):
    e_back=p1+p2
    print(e_back+'请输入有效数字')
    print(e_back+'\033[6;31mError\033[0m\n')
    print('请选择\033[6;35m圆环\033[0m\033[1;1m模式重试')
    switch(2)
def part_yh():#圆环
    while True:
        r1=input('请输入外圆半径:')
        try:
        	r1=eval(r1)
        	if r1<=0:
        	    print('你输入的数太小\n请重新选择\033[6;35m圆环\033[0m\033[1;1m模式重试')
        	    switch(3)
        	    break
        except ZeroDivisionError:
            print('除数不能为0')
        except (Exception,IOError,ValueError,TypeError,SyntaxError,EOFError,NameError,KeyboardInterrupt):
            yh_error('外圆半径',':')
            break
        r2=input('请输入内圆半径:')
        try:
        	r2=eval(r2)
        	if r2<=0:
        	    print('你输入的数太小\n请重新选择\033[6;35m圆环\033[0m\033[1;1m模式重试')
        	    switch(2)
        	    break
        except ZeroDivisionError:
            print('除数不能为0')
        except (Exception,IOError,ValueError,TypeError,SyntaxError,EOFError,NameError,KeyboardInterrupt):
            yh_error('内圆半径',':')
            break
        try:
            if r2>=r1:
                print('①.内圆半径应<外圆半径\n②.2s后重新选择\033[6;35m圆环\033[0m\033[1;1m模式重试\n\033[7;35mtips:\033[0m\033[1;1m注意外圆半径和内圆半径的顺序')
                switch(3)
                break
        except Exception:
            print('出现\033[6;31mError\033[0m\n')
            print('请选择\033[6;35m圆环\033[0m\033[1;1m模式重试')
            switch(2)
            break
        print('【\033[6;35m圆环\033[0m\033[1;1m】')
        aboutpi()
        if os1=='Linux':
            xxx=input('请输入(\033[1;32m1,2,3,4,5\033[0m\033[1;1m)中的一个数字:')
        elif os1=='Windows':
            xxx=input('请输入1,2,3,4,5中的数字')
        print('')
        try:
            xxx=int(xxx)
        except ZeroDivisionError:
            print('除数不能为0')
        except (Exception,IOError,ValueError,TypeError,SyntaxError,EOFError,NameError,KeyboardInterrupt):
            print('请输入正确的整数,不可以使用运算符')
        try:
            if xxx>5 or xxx<=0:
                end1=sj.now()-start
                print('即将\033[10;31m退出\033[0m,','本次使用时间:',end1,'\n程序将在5秒后关闭,谢谢使用')
                exitings(5)
                tc('谢谢使用')
            elif xxx==5:
                print('-'*40)
                switch(0.1)
                break
            elif xxx==1:
                Sr1=r1*r1*3.14 #外圆s
                Sr2=r2*r2*3.14 #内圆s
                S=Sr1-Sr2     #圆环s
                C1=6.28*r1 #外圆c
                C2=6.28*r2 #内圆c 
                dw()
                print('=====计算结果=====')
                print('圆环面积=','{:.5f}'.format(S))
                print('外圆周长=','{:.4f}'.format(C1))
                print('内圆周长=','{:.4f}'.format(C2))
                print('外圆面积=','{:.5f}'.format(Sr1))
                print('内圆面积=','{:.5f}'.format(Sr2))
            elif xxx==2:
                Sr1=r1*r1*pai1 #外圆s #6
                Sr2=r2*r2*pai1 #内圆s #7
                S=Sr1-Sr2      #圆环s #6
                C1=2*pai1*r1 #外圆周长#6
                C2=2*pai1*r2 #内圆周长 #6
                print('=====计算结果=====')
                print('圆环面积=','{:.5f}'.format(S))
                print('外圆周长=','{:.4f}'.format(C1))
                print('内圆周长=','{:.4f}'.format(C2))
                print('外圆面积=','{:.5f}'.format(Sr1))
                print('内圆面积=','{:.5f}'.format(Sr2))
            elif xxx==3:
                Sr1=r1*r1 #外圆s 
                Sr2=r2*r2#内圆s
                S=Sr1-Sr2      #圆环s
                C1=2*r1 #外圆周长
                C2=2*r2#内圆周长
                dw()
                print('=====计算结果=====')
                print('圆环面积=','{:.5f}'.format(S),pai2) 
                print('外圆周长=','{:.4f}'.format(C1),pai2)
                print('内圆周长=','{:.4f}'.format(C2),pai2)
                print('外圆面积=','{:.5f}'.format(Sr1),pai2)
                print('内圆面积=','{:.5f}'.format(Sr2),pai2)
            elif xxx==4:
                defpi=input('请输入要自定义的π(大于等于3且小于3.2)->')
                try:
                    defpi=eval(defpi)
                    if defpi<3 or defpi >3.2:
        	            print('^大于3小于3.2^|||3s后进入切换模式\n请选择圆柱模式')
        	            switch(3)
        	            break
                    elif defpi >=3 and defpi <3.2:
                        Sr1=r1*r1*defpi    #外圆s
                        Sr2=r2*r2*defpi #内圆s
                        S=Sr1-Sr2             #圆环s
                        C1=2*defpi           #外圆周长
                        C2=2*defpi*r2    #内圆周长
                        dw()
                        print('=====计算结果=====')
                        print('圆环面积=','{:.5f}'.format(S))
                        print('外圆周长=','{:.4f}'.format(C1))
                        print('内圆周长=','{:.4f}'.format(C2))
                        print('外圆面积=','{:.5f}'.format(Sr1))
                        print('内圆面积=','{:.5f}'.format(Sr2))        	            
                except ZeroDivisionError:
        	        print('除数不能为0')
                except (Exception,IOError,ValueError,TypeError,SyntaxError,EOFError,NameError,KeyboardInterrupt):
                    print('请输入正确的数字')
            else:
                end=sj.now()-start
                print('即将\033[10;31m退出\033[0m,','本次使用时间:',end,'\n程序将在5秒后关闭,谢谢使用')
                exitings(5)
                tc('谢谢使用')
        except Exception:
            print('\033[6;35m圆环\033[0m\033[1;1mbeta报告:在本模式中您的操作出现\033[1;1m\033[6;31mError\033[0m\n','\b已为您自动跳转选择模式,请选择\033[6;35m圆环\033[0m\033[1;1m模式')
            switch(1)
            break