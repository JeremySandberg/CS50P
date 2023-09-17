# Path finding algorithm

#### Video Demo:  <https://youtu.be/59lsn9uEyB4>

## __Summary__
This is my final project for the course CS50P.
It's written entirely in python with related libraries.

## __Structure__
 This project is a simple python script showcasing a pathfinding algorithm. Included is also a test file to test the functionality of the main file.

 Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md

 ## __Libraries__

__NumPy__ :  NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.[(Readmore)](https://numpy.org/)

__MatPlotLib__ : Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. [(Readmore)](https://matplotlib.org/)

## Usage
Run project.py
Enter size of board, this will be a n by n board.
Enter number of blockages, these will be randomly placed.
Find "Figure1.png" in same folder to see the output plot.

For testing run test_project.py using pytest for optimal results.

#### Description:
A simple showcase of using a pathfinding algorithm on a randomly generated board.
It generates a nxn board with given size.
It then puts blockages of a specific amount randomly on the board.
Then making use of the A* search algoritm in order to find a path
I used A* as it is widely used and considered to be one of the best for this application.
I make use of matplotlib in order to create the plot of the board and the path taken if there is one.

### Author : Jeremy Sandberg
