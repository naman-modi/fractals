import turtle
ob=turtle.Turtle();
ob.speed(10000)
turtle.bgcolor("black")
ob.pencolor("teal")
ob.speed(10000)
ob.hideturtle()
def carpet(a = 200, n = 2):
	if n == 0:
		ob.fillcolor("blue")
		ob.begin_fill()
		for i in range(0, 4):
			ob.forward(a)
			ob.left(90)
		ob.end_fill()
	else:
		for i in range(0, 4):
			carpet(a / 3, n - 1)
			ob.forward(a / 3)
			carpet(a / 3, n - 1)
			ob.forward(a / 3)
			carpet(a / 3, n - 1)
			ob.forward(a / 3)
			ob.left(90)

#driver function
def main():
	size = int(input("Enter size: "))
	iterations = int(input("Enter number of iterations: "))
	carpet(size, iterations)
	input()
if __name__ == "__main__":
	main()
