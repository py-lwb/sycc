from sys import path
path.append('..')
from .__init__ import *
from e.__init__ import *
from p.pdsys import os1,os2
pai2='π'
qt_font='\033[1;33m球体\033[0m\033[1;1m'
def part_qt():
    #print('球体-β')
    while True:
        try:
            r=eval(input('请输入半径:'))
            d=2*r
            if r<=0:
        	    print('你输入的数太小\n请重新选择'+qt_font+'模式重试')
        	    switch(3)
        	    break
        except ZeroDivisionError:
            print('除数不能为0')
        except Exception:
            print('半径:请输入有效数字')
            print('半径:\033[6;31mError\033[0m\n')
            print('请选择'+qt_font+'模式重试')
            switch(2)
            break
        print('【'+qt_font+'】')
        aboutpi()
        if os1=='Linux' or os2=='linux':
            xxx=input('请输入(\033[1;32m1,2,3,4,5\033[0m\033[1;1m)中的一个数字:')
        elif os1=='Windows' or os2=='windows':
            xxx=input('请输入1,2,3,4,5中的数字')
        print('')
        try:
            xxx=int(xxx)
        except ZeroDivisionError:
            print('除数不能为0')
        except (Exception,IOError,ValueError,TypeError,SyntaxError,EOFError,NameError,KeyboardInterrupt):
            print('请输入指定范围的整数,不可以使用运算符')
            switch(0.3)
            break
        try:
        	if xxx>5 or xxx<=0:
        		end1=sj.now()-start
        		print('即将\033[10;31m退出\033[0m,','本次使用时间:',end1,'\n程序将在3s后关闭,谢谢使用')
        		exitings(3)
        		tc('谢谢使用')
        	elif xxx==5:
        		print('-'*40)
        		switch(0.3)
        		break
        	elif xxx==1:
        	    S=4*3.14*r**2
        	    c=2*3.14*r
        	    s=2*3.14*r
        	    v=4/3*3.14*pow(r,3)
        	    dw()
        	    print('======计算结果======')
        	    print('当半径=',r,'直径=',d,'时')
        	    print('截面面积={:.4f}'.format(s))
        	    print('截面周长={:.4f}'.format(c))
        	    print('表面积={:.4f}'.format(S))
        	    print('体积={:.4f}'.format(v)+'\n')
        	elif xxx==2:
        	    s=2*pai1*r
        	    c=2*pai1*r
        	    S=4*pai1*pow(r,2)
        	    v=4/3*pai1*r**3
        	    dw()
        	    print('======计算结果======')
        	    print('当半径=',r,'直径=',d,'时')
        	    print('截面面积={:.4f}'.format(s))
        	    print('截面周长={:.4f}'.format(c))
        	    print('表面积={:.4f}'.format(S))
        	    print('体积={:.4f}'.format(v)+'\n')
        	elif xxx==3:
        	    r2=r**2#r²+pai2#截
        	    s=r2*4#4r²+pai2#表
        	    v=r**3*4/3#
        	    c=2*r
        	    print('======计算结果======')
        	    print('当半径=',r,'直径=',d,'时')
        	    print('截面面积={:.4f}'.format(r2)+pai2)
        	    print('截面周长={:.4f}'.format(c)+pai2)
        	    print('表面积={:.4f}'.format(s)+pai2)
        	    print('体积={:.4f}'.format(v)+pai2+'\n')
        	elif xxx==4:
        	    defpi=input('请输入要自定义的π(大于等于3且小于3.2)->')
        	    try:
        	        defpi=eval(defpi)
        	        if defpi<3 or defpi >3.2:
        	            print('^大于3小于3.2^|||3s后进入切换模式\n请选择'+qt_font+'模式')
        	            switch(3)
        	            break
        	        else:
        	            s=defpi*r**2
        	            S=4*defpi*r**2
        	            v=4/3*defpi*r**3
        	            c=2*defpi*r
        	            print('======计算结果======')
        	            print('当半径=',r,'直径=',d,'π=',defpi,'时')
        	            print('截面面积={:.6f}'.format(s))
        	            print('截面周长={:.6f}'.format(c))
        	            print('表面积={:.6f}'.format(S))
        	            print('体积={:.6f}'.format(v)+'\n')
        	    except ZeroDivisionError:
        	        print('除数不能为0')
        	    except (Exception,KeyboardInterrupt):
        	        print('请输入指定范围的数字')
        	else:
        	    end1=sj.now()-start
        	    print('即将\033[10;31m退出\033[0m,','本次使用时间:',end1,'\n程序将在5s后关闭,谢谢使用')
        	    exitings(5)
        	    tc('谢谢使用')
        except Exception as e:
            print(e)
            print(qt_font+'beta报告:在本模式中您的操作出现\033[1;1m\033[6;31mError\033[0m\n','\b已为您自动跳转选择模式,请选择'+qt_font+'模式')
            switch(1)