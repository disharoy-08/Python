from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I an a Label", font=('Arial', 24, "bold"))
my_label['text'] = "New Text"
my_label.config(text="New Text")
#my_label.pack()
#my_label.pack(side="left")
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)


# import turtle
# tin = turtle.Turtle()
# tin.write("testing", font={"Times New Roman", 80, "bold"})

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
#button.pack(side="left")
button.grid(column=1, row=1)
button.config(padx=10, pady=10)

button1 = Button(text="New Button", command=button_clicked)
button1.grid(column=2, row=0)
button1.config(padx=10, pady=10)

#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
#input.pack(side="left")
input.grid(column=3, row=2)



window.mainloop()
