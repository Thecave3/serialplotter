#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reader.py
#
#  Copyright 2016 Andrea Lacava, Thecave3
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import sys #ctrl-c handling and clear handling
import serial # sudo apt-get install python-serial
import numpy as np # real-time
import matplotlib.pyplot as plt # sudo apt-get install python-matplotlib
import os

#NB il programma NON funziona senza i moduli serial, numpy e plt
#Installazione di tali moduli per windows http://docs.python.it/html/inst/



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
    print( "Errore, porta sbagliata?")
    print("Prima di eseguire lo script settare correttamente la porta, la porta di default è /dev/ttyACM0")
    print( "Termino applicazione")
    sys.exit()

#crea file di log dove salva i dati raccolti dall'arduino
logger = open("logger.csv",'w')
plt.axis([0, 2000, 0, 2000])
plt.ion()

#the big loop
while 1:
    try:
        data=ser.readline()
        print( "Pressione ambientale: "+ data[0]+"Umidità %: "+ data[1]+" Temperatura °C: "+ data[2] +" Pressione interna: "+data[3]+ "Tempo: "+data[4])
        os.system('cls' if os.name == 'nt' else 'clear')
        logger.write(data)
        data = data.strip("\n").strip("\r")
        data = data.split(';')
        y = data[0]
        x = data[4]
        plt.scatter(x, y)
        plt.pause(0.05)

    except KeyboardInterrupt:
        logger.flush()
        plt.close()
        logger.close()
        ser.close()
        sys.exit()

#this will be never reached (hopefully)
print ("Contact IMMEDIATELY thecave003  @ www.andrealacava.com")
