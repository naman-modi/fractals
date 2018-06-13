import turtle
from sys import exit
def tree(a, n, angle):
	if n == 0:
		ob.left(angle)
		ob.forward(0.75 * a)
		ob.backward(0.75 * a)
		ob.right(2 * angle)
		ob.forward(0.75 * a)
		ob.backward(0.75 * a)
		ob.left(angle)
	else:
		ob.left(angle)
		ob.forward(a)
		tree(0.75 * a, n-1, angle)
		ob.backward(a)
		ob.right(2 * angle)
		ob.forward(a)
		tree(0.75 * a, n-1, angle)
		ob.backward(a)
		ob.left(angle)
try:
	a = int(input("Enter length : "))
	n = int(input("Enter number of iterations : "))
	angle = int(input("Enter angle : "))
except KeyboardInterrupt:
	exit(0)
except:
	print("Invalid input")
	exit(-1)
ob = turtle.Turtle();
turtle.bgcolor("black")
ob.speed(10000)
ob.pencolor("green")

ob.penup()
ob.goto(0, -200)
ob.pendown()
ob.left(90)
ob.forward(2 * a)
tree(a, n, angle)
input()
