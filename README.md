# serialplotter

What is?

A simple serial reader and plotter with a log function. The main idea is to use your Arduino controller's output directly in your python code.

This script was committed for scientifical purpose by me. The initial committent was the Physics Department of La Sapienza University, Rome. They need an enviroment controller for their clean room10000 so I used an Arduino to handle backend aka the values detected by sensors and then this script to handle the front-end.

Is a ready-to-implement code?

No,you should shape to what you want to do by yourself.

In the next steps of this work I will make the script a multithreading script.

How to use it

Hack’n’play for your personal use.


Dependencies

This program will NOT work if you don't have serial and plt modules.
Install them with your favourite repository tools:
If you use a Debian-Based distribution:
  sudo apt-get install python-serial
  sudo apt-get install python-matplotlib

Windows Users should download Linux or install Anaconda Enviroment because it contains the most of the libraries used
