import threading
import time
import random

def Barbero():
	global nClientes
	global AsientoOcupado
	IDActual=0

	while(Asiento != 0):
		time.sleep(1)
		EspacioClientes.acquire()
		if(nClientes > 0):
			Asiento.acquire()
			AsientoOcupado= True
			s= random.random()
			IDActual+= 1
			print("Cliente {0} sera pelado en {1}".format(IDActual, s))
				
			nClientes-=1
			EspacioClientes.release()
			time.sleep(s)

			print("Cliente {0} pelado".format(IDActual))
			AsientoOcupado= False
			Asiento.release()
		else:
			EspacioClientes.release()
			Asiento.acquire()
			AsientoOcupado= True
			time.sleep(1)
			print("Durmiendo")
			AsientoOcupado= False
			Asiento.release()

	print("Fin del barbero")
	

def GeneradorClientes():
	global IDCliente
	global nClientes
	global MaximoClientes
	for i in range(10):
		s= random.random()
		time.sleep(s)
		EspacioClientes.acquire()
		if(nClientes <= MaximoClientes):
			nClientes+=1
			IDCliente+=1
			print("Nuevo cliente {0} al cabo de {1}".format(IDCliente, s))
			
		else:
			print("Cliente rechazado en {0}".format(s))
		EspacioClientes.release()
		

nClientes=0
MaximoClientes= 4
IDCliente= 0
AsientoOcupado= False
Asiento= threading.BoundedSemaphore(1)
EspacioClientes= threading.BoundedSemaphore(1)

Clientes= threading.Thread(target= GeneradorClientes)
Barbero= threading.Thread(target= Barbero)

Clientes.start()
Barbero.start()
Clientes.join()
Barbero.join()
