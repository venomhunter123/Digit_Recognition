from tkinter import *
import numpy as np
from PIL import ImageGrab
from Prediction import predict

window = Tk()
window.title("Handwritten digit recognition")
l1 = Label()


def MyProject():
	global l1

	widget = cv

	x = window.winfo_rootx() + widget.winfo_x()
	y = window.winfo_rooty() + widget.winfo_y()
	x1 = x + widget.winfo_width()
	y1 = y + widget.winfo_height()


	img = ImageGrab.grab().crop((x, y, x1, y1)).resize((28, 28))


	img = img.convert('L')


	x = np.asarray(img)
	vec = np.zeros((1, 784))
	k = 0
	for i in range(28):
		for j in range(28):
			vec[0][k] = x[i][j]
			k += 1


	Theta1 = np.loadtxt('Theta1.txt')
	Theta2 = np.loadtxt('Theta2.txt')


	pred = predict(Theta1, Theta2, vec / 255)


	l1 = Label(window, text="Digit = " + str(pred[0]), font=('Algerian', 20))
	l1.place(x=230, y=420)


lastx, lasty = None, None


def clear_widget():
	global cv, l1
	cv.delete("all")
	l1.destroy()


def event_activation(event):
	global lastx, lasty
	cv.bind('<B1-Motion>', draw_lines)
	lastx, lasty = event.x, event.y


def draw_lines(event):
	global lastx, lasty
	x, y = event.x, event.y
	cv.create_line((lastx, lasty, x, y), width=30, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=12)
	lastx, lasty = x, y


# Label
L1 = Label(window, text="Handwritten Digit Recoginition", font=('Algerian', 25), fg="blue")
L1.place(x=35, y=10)

# Button to clear canvas
b1 = Button(window, text="1. Clear Canvas", font=('Algerian', 15), bg="orange", fg="black", command=clear_widget)
b1.place(x=120, y=370)

# Button to predict digit drawn on canvas
b2 = Button(window, text="2. Prediction", font=('Algerian', 15), bg="white", fg="red", command=MyProject)
b2.place(x=320, y=370)

# Setting properties of canvas
cv = Canvas(window, width=350, height=290, bg='black')
cv.place(x=120, y=70)

cv.bind('<Button-1>', event_activation)
window.geometry("600x500")
window.mainloop()
