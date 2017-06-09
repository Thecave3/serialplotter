#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys #ctrl-c handling and clear handling
import serial
import matplotlib.pyplot as plt #plotter
import os
import threading

print( "Provo ad aprire porta Arduino...")
#apre la porta seriale ad un baudrate 9600
try:
    ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
    )
except serial.serialutil.SerialException:
    print( "Errore, porta sbagliata? Dispositivo non collegato?")
    print("Prima di eseguire lo script settare correttamente la porta, la porta di default è /dev/ttyACM0")
    print( "Termino applicazione")
    sys.exit(-1)

#crea file di log dove salva i dati raccolti dall'arduino
logger = open("logger.csv",'w')
plt.axis([0, 2000, 0, 2000])
plt.ion()

#the big loop
while 1:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        data=ser.readline()
        logger.write(data)
        data = data.strip("\n").strip("\r")
        data = data.split(';')
        print( "Pressione ambientale: "+ data[0]+"\nUmidità %: "+ data[1]+"\nTemperatura °C: "+ data[2] +"\nPressione interna: "+data[3]+ "\nTempo: "+data[4])
        y = data[3]
        x = data[4]
        plt.scatter(x, y)
        plt.pause(0.05)

    except KeyboardInterrupt:
        logger.flush()
        plt.close()
        logger.close()
        ser.close()
        sys.exit()

    except IndexError:
        logger.flush()
        print("Errore di lettura arduino, misurazione non valida")
        pass

#this will be never reached (hopefully)
print ("Contact IMMEDIATELY thecave003  @ www.andrealacava.com")
