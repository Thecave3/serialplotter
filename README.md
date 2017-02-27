# serialplotter

##What is?

A simple serial reader and plotter with a logging util to use your Arduino controller's output directly in your code.

This script was committed for scientifical purpose for the Physics Department of La Sapienza University, Rome.
They need an enviroment controller for their clean room10000 so I used an Arduino to handle back-end [EnviromentController](https://github.com/Thecave3/EnviromentControllerArduino) here the values detected by sensors and then this script to handle the front-end.

##Is a ready-to-implement code?
No,you should shape to what you want to do by yourself.

I finally decided to rewrite the whole software in java to offer a better GUI and proper multithreading interaction.

##How to use it:

Hack’n’play for your personal use.


##Dependencies
- JAVA version:
  This program will NOT compile if you don't have at least:
    - JAVA SE 7
    - JFreeChart  v 1.0.19 that can be obtained
   -  JCommon v 1.0.23

NOTE: [Here](http://www.jfree.org/jfreechart/download/jfreechart-1.0.0-install.pdf) is a simple pdf guide to install and use JFreeChart and JCommon.

PYTHON version
This program will NOT work if you don't have serial and plt modules.
In Linux you can install them with your favourite repository tool:

If you use a Debian-Based distribution:
  sudo apt-get install python-serial
  sudo apt-get install python-matplotlib

Windows Users should install Anaconda Enviroment because it contains all the libraries used.
