import config
import displaymgr
import mapmgr

def main():
	displaymgr.titlescreen()
	a = mapmgr.createmap()
	mapmgr.printmap(a)
	
if __name__ == '__main__':
	main()