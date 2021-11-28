#2020-2021
from setuptools import setup
import os
import platform
import sys,time
import sys
try:
    import netifaces
except ImportError:
    import subprocess
    subprocess.call("pip install netifaces", shell=True)
if platform.system() == 'Linux':#
    pass
elif platform.system() == 'Windows':
    pass
else:
    print('不支持该系统')
    time.sleep(10)
    sys.exit()
__Author__ = '神秘的·'
__project_start_time__='2020'
__date_end_time__ = '2021/11'
HERE = os.path.abspath(os.path.dirname(__file__))
print('\n'+'PATH::README.rst:',HERE+'\n\n')
with open(os.path.join(HERE, "README.rst")) as rst:
    R= rst.read()
setup(
    #setup_requires=['pbr'],
    #pbr=True,
    name='sycc', #sycc
    py_modules=['sycc','core','__init__','v'],
    version='0.7.0',#test原0.6.59
    description='虹源三式(四圆计算器)', #原
    long_description = R,
    classifiers=[
    'Natural Language :: Chinese (Simplified)',
    'Development Status :: 6 - Mature',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Android',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Terminals',
    'Topic :: System :: Shells',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Intended Audience :: Developers',],
    keywords=['sycc','3y','a_3y','Circle','圆','圆柱','圆环','py','Chinese','ycc',
    'python','windows','linux','3','y','yh','yz','qt','4','4y','计算器',"Calculator",
    'edu'],# 关键字
    author=__Author__, 
    author_email='lwb29@qq.com', 
    url='http://pypi.org/project/sycc', 
    license='MIT(Modified)',
    packages=["p","k","e","colorama","p/tqdm","requires_LICENSE","imformation"],
    python_requires='>=3.6',
    install_requires=['netifaces>=0.11.0','sycc>=0.6.0'],
    entry_points = {'console_scripts': ['sycc = sycc:main',]},
    project_urls = {
    'url':'pypi.org/project/sycc',
    'pydroid(文件密码:sycc)' : 'https://wwe.lanzoui.com/if8bUw94h6d'
    },
    include_package_data=True,
    zip_safe=True,
)
if os.path.exists('setup.cfg')==True:
    os.remove('setup.cfg')
elif os.path.exists('MANIFEST.in')==True:
    os.remove('MANIFEST.in')