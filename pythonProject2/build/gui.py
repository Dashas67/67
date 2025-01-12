
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ssshh\PycharmProjects\pythonProject2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1500x800")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    1038.0,
    29.0,
    anchor="nw",
    text="Pleasure",
    fill="#000000",
    font=("Italiana Regular", 64 * -1)
)

canvas.create_text(
    1204.0,
    88.0,
    anchor="nw",
    text="Cafe",
    fill="#000000",
    font=("Inter", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    447.0,
    400.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1167.5,
    220.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FAF6F6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1032.0,
    y=205.0,
    width=271.0,
    height=29.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1160.5,
    333.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAF6F6",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1025.0,
    y=318.0,
    width=271.0,
    height=29.0
)

canvas.create_text(
    998.0,
    178.0,
    anchor="nw",
    text="Логин",
    fill="#000000",
    font=("Inika", 15 * -1)
)

canvas.create_text(
    995.0,
    284.0,
    anchor="nw",
    text="Пароль",
    fill="#000000",
    font=("Inika", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1073.0,
    y=426.0,
    width=186.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1079.0,
    y=517.0,
    width=180.0,
    height=27.0
)
window.resizable(False, False)
window.mainloop()
