# serialplotter

## What is?

A simple serial reader and plotter with a logging util to use your Arduino controller's output directly in your code.

This script was committed for scientifical purpose for the Physics Department of La Sapienza University, Rome.
They need an enviroment controller for their clean room10000 so I used an Arduino to handle back-end [EnviromentController](https://github.com/Thecave3/EnviromentControllerArduino) here the values detected by sensors and then this script to handle the front-end.

## What is to implement for now

Multithreading segmentation

## How to use it:

Hack’n’play for your personal use.


## Dependencies

- PYTHON version:
  This program will NOT work if you don't have serial and plt modules.
  In Linux you can install them with your favourite repository tool.

 If you use a Debian-Based distribution:

  ```
    sudo apt-get install python-serial
    sudo apt-get install python-matplotlib
  ```
Windows Users should install Anaconda Enviroment because it contains all the libraries used.
