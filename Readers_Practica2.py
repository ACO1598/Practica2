import threading

def writer(pos, Q, S, biblioteca):
	S.acquire()
	Q.acquire()
	print("Escritor posicion {0} antes: {1}".format(pos, biblioteca[pos]))
	biblioteca[pos]+=1
	print("Escritor posicion {0} despues: {1}".format(pos, biblioteca[pos]))
	Q.release()
	S.release()

def reader(pos, Q, S, biblioteca):
	Q.acquire()
	print("Lector leyendo posicion: ",pos," Contenido: ", biblioteca[pos])
	Q.release()

S= threading.Semaphore(1)
Q= threading.Semaphore(1)
biblioteca= [1,2,3,4,5,4,3,2,1,0]
escritores= []
lectores= []

for i in range(10):
	escritores.append(threading.Thread(target= writer, args=(i, Q, S, biblioteca)))
	lectores.append(threading.Thread(target= reader, args=(i, Q, S, biblioteca)))
	

for i in range(10):
	
	escritores[i].start()
	lectores[i].start()

for i in lectores:
	i.join()

for i in escritores:
	i.join()
