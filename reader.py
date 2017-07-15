#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys #ctrl-c handling and clear handling
import serial
import matplotlib.pyplot as plt #plotter
import os
import threading

print( "Provo ad aprire porta Arduino...")
# apre la porta seriale ad un baudrate 9600
try:
    ser = serial.Serial(
    port='COM65',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
    )
except serial.serialutil.SerialException:
    print( "Errore, porta sbagliata? Dispositivo non collegato?")
    print("Prima di eseguire lo script settare correttamente la porta, la porta di default è COM65")
    print( "Termino applicazione")
    sys.exit(-1)

# crea file di log dove salva i dati raccolti dall'arduino
print("Creo un nuovo file di log...\n")
try:
	logger = open("logger.csv",'w')
except IOError:
	print("Errore in creazione nuovo file di log, controlla che il vecchio file non sia aperto con altri programmi")
	print("Uscita in corso...")
	sys.exit(-1)

print( "File di log creato correttamente!")
print( "Nota che il file logger.csv viene sovrascritto ogni volta, se quindi devi salvare i dati rinomina il file vecchio")

plt.axis([0, 8640, 0.2, 1.1])
plt.ion()

# the big loop
while 1:
    try:
		data=ser.readline()
		os.system('cls' if os.name == 'nt' else 'clear')
		data.strip('\n')
		logger.write(data)
		data = data.strip("\n").strip("\r")
		data = data.split(';')
		print( "Pressione ambientale: "+ data[0]+"\nUmidita' %: "+ data[1]+"\nTemperatura (gradi centigradi): "+ data[2] +"\nPressione interna: "+data[3]+ "\nTime: "+data[4])
		y = data[3]
		x = data[4]
		plt.scatter(x, y)
		plt.pause(0.05)

    except KeyboardInterrupt:
        logger.flush()
        plt.close()
        logger.close()
        ser.close()
        print("Uscita in corso...")
        sys.exit()

    except IndexError:
        logger.flush()
        print("Errore di lettura arduino, valore saltato, misurazione non valida")
        pass

    except serial.serialutil.SerialException:
        logger.flush()
        print("Errore di lettura errore di lettura socket, ripeto operazione")
        pass

#this will be never reached (hopefully)
print ("Contact IMMEDIATELY thecave003  @ www.andrealacava.com")
