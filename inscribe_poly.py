"""
File: inscribe_poly.py
Name: Nicholas Shinn
Description: Draws polygons inside circles based on user input
"""

import turtle as t
import math as m

def main():
	"""
	initializes the canvas and turtle before drawing the polygons
	"""
	initialization()
	drawPolygon(200, int(input('Enter number of sides: ')), 0)
	t.done()

def initialization():
	"""
	Initializes turtle
	Pre: Turtle down, facing East
	Post: Turtle up, facing East
	"""
	t.up()
	t.speed(0)

def drawPolygon(r, n, a):
	"""
	Draws a circle and inscrbes the polygons in them before returning perimeter values
	Pre: Turtle facing East, pen up
	Post: Turtle facing East, pen up
	:param r: Radius of circle
	:param n: Number of recursions
	:param a: Distance
	:return: Perimeter of polygon
	"""
	if n==0:
		pass
	elif n >= 3:
		alpha = 360 / n
		beta = alpha / 2
		c = m.sqrt(r ** 2 + r ** 2 - 2 * r * r * m.cos(m.radians(alpha)))
		r_prime = m.sqrt(r ** 2 - (c / 2) ** 2)
		z = n
		t.pencolor('black')
		t.forward(r)
		t.left(90)
		t.down()
		t.circle(r)
		t.up()
		t.left(beta)
		if z % 3 == 0:
			t.pencolor('red')
		elif z % 2 == 0:
			t.pencolor('blue')
		else:
			t.pencolor('green')
		while z > 0:
			t.down()
			t.begin_fill()
			t.forward(c)
			t.left(alpha)
			t.up()
			a += c
			z -= 1
		t.right(90+beta)
		t.backward(r)
		drawPolygon(r_prime, n-1, a)
	else:
		print('Distance: ' + str(a))
		n = int(input('Enter number of sides: '))
		drawPolygon(r, n, a)

main()