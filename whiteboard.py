from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

# Icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# Color Box Image
color_box = PhotoImage(file="section.png")
Label(root, image=color_box, bg="#f2f3f5").place(x=10, y=20)

# Resize Eraser Image
eraser_image = Image.open("eraser.png")
eraser_image = eraser_image.resize((30, 30), Image.LANCZOS)
eraser_image = ImageTk.PhotoImage(eraser_image)

# Eraser Button
eraser_button = Button(root, image=eraser_image, bg="#f2f3f5", command=lambda: show_color('white'))
eraser_button.place(x=30, y=400)

# Color Palette
colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def show_color(new_color):
    global current_color
    current_color = new_color

def display_palette():
    id = colors.create_rectangle((10, 10, 30, 30), fill='black')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 70, 30, 90), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 100, 30, 120), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 130, 30, 150), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10, 160, 30, 180), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 190, 30, 210), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

    id = colors.create_rectangle((10, 220, 30, 240), fill='brown')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown'))

    id = colors.create_rectangle((10, 250, 30, 270), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

display_palette()

# Canvas for drawing
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

current_color = 'black'
last_x, last_y = None, None

def on_button_press(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def on_paint(event):
    global last_x, last_y
    x, y = event.x, event.y
    canvas.create_line((last_x, last_y, x, y), fill=current_color, width=2)
    last_x, last_y = x, y

canvas.bind('<Button-1>', on_button_press)
canvas.bind('<B1-Motion>', on_paint)

root.mainloop()
