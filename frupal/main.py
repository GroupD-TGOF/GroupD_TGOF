import config
import time
import displaymgr
import mapmgr

def main():
	displaymgr.titlescreen()
	a = mapmgr.createmap()
	time.sleep(5)
	displaymgr.menuscreen()
	time.sleep(5)
	mapmgr.printmap(a)
	
if __name__ == '__main__':
	main()