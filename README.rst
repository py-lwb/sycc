.. image:: https://img.shields.io/pypi/v/sycc?color=9cf&label=sycc&logo=sycc&logoColor=success&style=flat-square/
.. image:: https://static.pepy.tech/personalized-badge/sycc?period=total&units=abbreviation&left_color=blue&right_color=green&left_text=Downloads
.. image:: https://static.pepy.tech/personalized-badge/sycc?period=month&units=international_system&left_color=lightgrey&right_color=brightgreen&left_text=Downloads
 :target: https://pypi.org/project/sycc/#Description/


sycc
^^^^^^^^^^^^^^^^^^^^^

*time:2020-2021*

sycc:s是Simplify或Sphere(球体)的意思,y是圆的意思,第一个c指代Cylinder（圆柱）,第二个c指代Ring（圆环）

+-+-+-+-+-+-+-+-+-+-

虹源三式:代表着只是个人第一次编辑的代码程序，虹代表作者写了许多为让运行程序能看到彩色字体而写了许多让程序颜色不那么单一的代码。
而本程序是用来辅助计算 ``圆`` 、``圆环`` 、 ``圆柱`` 、``球体`` 以目前作者知识量制作后续可能会更新圆锥等规则几何物体。

虹源三式这个名字则代表拥有运行可见彩色字体源自个人制作编写的三种(已更新为四种)几何图形计算方式。

+-+-+-+-+-+-+-+-+-+-


Logo
------------------
.. image:: https://i.loli.net/2021/11/21/prfjHoNVOWsDulg.jpg

请等待下一次更新


特点
-------
1.不会显得那么单调，加入了部分色彩（cmd或Terminal显示,pycharm可能无效）

2.能使用四种不同的计算器

3.操作简单,不易报错

4.没有团队，作者“孤军作战”


下载&更新&运行
-------------------------------------------
使用pip下载:

::
    
    $pip install sycc -i https://pypi.org/simple/


使用git下载

::
    $git clone https://github.com/py-lwb/sycc.git
    $cd sycc
    $python setup.py install

使用pip更新:

::
    
    $pip install --upgrade sycc -i https://pypi.org/simple/


运行方式1:

::
            
    $sycc

运行方式2:

::  
    
    from sycc import *
    
    if __name__ == '__main__':
        main()


cmd或linux系统的终端使用运行方式1

python交互式窗口或编辑一个新的py文件中使用运行方式2

**注** :第三方编辑器(eg:pycharm)可能无法显示本程序应有的高亮颜色


权利
---------
**本模块的解释权归作者所有**

**作品翻译权归作者和用户**

即将开源至 **github**


提示与警告
--------------------------------

**tips :作者定制版本!**   ##开源

当你使用这个模块，出现程序错误时，你可以通过qq邮箱找到我

*qq邮箱*: ``lwb29@qq.com``:

::
    
    当您正在使用此项目时，您默认同意并了解以下内容。

    1.遵循你当地的法律，不要触犯法律。如果你在使用该项目中触犯了法律，与作者无任何关系

    2.请合理使用使用本项目。如果您在使用项目时发现bug，可以发送电子邮件到lwb29@qq.com
    
    3.最终解释权归作者所有。

    4. 项目已开源,建议请lwb29@qq.com


问题
-------
q:为什么经常出现退出或切换模式?

a:如果不及时切换或退出则会出现各种报错,这也不是大家想看到的.

q:为什么需要密码?

a:此版本为作者定制版,暂不提供他人使用.

如果还有其他问题邮箱lwb29@qq.com.

q:为什么进度条加载这么慢?

a:版本号获取方式与众不同


New
-----
1.待更新:修复在部分linux系统显示闪烁问题,git

2.优化代码逻辑

3.优化部分高亮彩色显示

4.优化自述文件显示

5.优化依赖包

6.略微美化

7.优化加载进度条(tqdm),优化版本号获取时间方式

8.新增略微有趣小彩蛋(1个)

9.增加 ``cls`` 或 ``clear`` 命令的执行

10.简化tqdm


特别鸣谢
-----------
1.感谢 **九霄天** 的赠与本项目的名字(+-+-+-+-+-中内容)——*虹源三式*

2.感谢Miss.Wei

3.感谢csdn,百度,博客圆,pypi,pydroid,网易云,阿里云

4.感谢 ``colorama`` ``tqdm`` ``netifaces`` 的作者

5.当然在此的感谢人员和平台数不胜数,在此统一感谢


声明
---------

1.本模块调用::

    ①python的内置库

    ②colorama模块

    ③tqdm模块的一部分

2.关于 *tqdm* 的 **简化** 问题::

    删除 tqdm/tqdm/std.py 中部分长注释和部分本模块用不到的py文件

3.使用 **sycc LICENSE** 开源协议(sycc作者添加部分内容)

4.colorama(BSD),tqdm(many),netifaces(MIT),开源协议,我已放置requires_LICENSE
文件夹