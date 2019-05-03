import threading
import time

def Filosofo(id, forks, S):
	comido=0
	while(comido==0):

		if(forks[id%5]==1 & forks[(id-1)%5]== 1):
			S.acquire()
			forks[id%5]=0
			forks[(id-1)%5]=0
			print("Filosofo {0} comiendo".format(id+1))
			S.release()
			comido=1

			time.sleep(5)
			

			S.acquire()
			forks[id%5]=1
			forks[(id-1)%5]=1
			print("Filosofo {0} ha comido".format(id+1))
			#time.sleep(1)
			S.release()
			waiting.release()
			
		else:
			S.release()
			print("Filosofo {0} esperando".format(id+1))
			waiting.acquire()
			#time.sleep(1)
		

forks=[1,1,1,1,1]
filosofos= []
S= threading.Semaphore(1)
waiting= threading.Semaphore(1)
for i in range(5):
	filosofos.append(threading.Thread(target= Filosofo, args= (i, forks, S)))

for i in filosofos:
	i.start()

for i in filosofos:
	i.join()
