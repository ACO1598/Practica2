import multiprocessing
import threading
import random

def Producer(inv, semaforo):
	semaforo.acquire()
	inv.append(i)
	print("Producer:", inv)
	semaforo.release()

def Consumer(inv, semaforo):
	semaforo.acquire()
	inv.pop()
	print("Consumer:", inv)
	semaforo.release()

inv= [1,2,3]
semaforo= threading.Semaphore(1)
//Establecer el numero de productores y consumidores
nPro= 0
mCon= 0
productores= []
consumidores= []

for i in range(nPro):
	print("Numero de productores: ")
	productores.append(threading.Thread(target= Producer, args=(inv, semaforo)))

Productor= threading.Thread(target= Producer, args=(inv, semaforo))
Consumer= threading.Thread(target= Consumer, args=(inv, semaforo))
Productor.start()
Consumer.start()
Productor.join()
Consumer.join()
print("Inventario final", inv)
