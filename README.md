# Carwow Bitmap Editor Case Study

The purpose of this exercise is to create a Python program based on the description given in order to simulate a basic 
interactive bitmap editor. Bitmaps are represented as an M x N matrix of pixels with each element representing a colour.

This Bitmap Editor is implemented as following:
* [bitmap_editor] This is a bash script file which will read the given argument and will call the main function to execute 
the program.
* [main.py] This is the main function which takes the input file path passes it to the parser and receives a queue containing
commands as dicts executes the instructions.
* [parser.py] This is a which reads the input file line by line and checks the validity of the commands.
* [commands.py] This file stores the given commands as python variables so they can be easily accessed.
* [bitmap.py] This file contains the bitmap class which contains the methods to create, show, clear or modify the bitmap object
which is a multi-dimensional array of characters.

## Getting Started

You can run the default set of commands given by cloning this repo and typing in the command line:

```
./bitmap_editor examples/show.txt
```

## Authors

* **Ioannis Nianios** 
