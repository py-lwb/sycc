from time import sleep as dd
def exit_tips(choose_quit):
	if choose_quit==1:
			print('\n准备退出中……(非正常退出请检查错误)\r')
	elif choose_quit==2:
			print('\n准备切换模式……(非正常切换请检查错误)')
def exitings(wait):
	exit_tips(1)
	while wait>=0:
		wait-=0.01
		dd(0.01)
		print('\r\033[1;1m\033[6;26;31m退出倒计时{:.1f}秒\033[0m'.format(abs(wait)),end="",flush=True)
	print('\n\033[1;23;33mFinish!\nEnd!\033[0m')
def switch(wt):#waiting time
	exit_tips(2)
	while wt>=0:
		wt-=0.01
		dd(0.01)
		print('\r\033[1;1m\033[6;26;32m切换倒计时{:.1f}秒\033[0m'.format(abs(wt)),end="",flush=True)
	print('\n\033[1;23;34mDone!\033[0m')