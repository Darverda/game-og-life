from tkinter import *

class Bs:
    def __init__(self):
        self.left = 1
        self.right = 1000
        self.middle = (self.left + self.right) // 2

    def get_middle(self):
        self.middle = (self.left + self.right) // 2
        return self.middle

    def increase_left(self):
        self.left = self.middle + 1

    def decrease_right(self):
        self.right = self.middle

    def reset(self):
        self.left = 1
        self.right = 1000
        self.get_middle()

"""
Функция для старта
"""
def start():
    btn_yes.grid(column=0, row=2)
    btn_no.grid(column=1, row=2)

    btn_restart.grid(column=0, row=3, sticky = W, padx = 15, pady = 15)
    btn_start.grid_remove()
    lbl.config(text=f"Это число больше {bs.get_middle()}?")

def restart():
    bs.reset()
    answer()

def check_guess():
    return bs.left >= bs.right

def answer():
    m = bs.get_middle()
    lbl.config(text=f"Ваше число больше {m}?")

def yes():
    bs.increase_left()
    is_guess = check_guess()
    if is_guess:
        lbl.config(text=f"Это число {bs.left}!")
        return

    answer()

def no():
    bs.decrease_right()

    is_guess = check_guess()
    if is_guess:
        lbl.config(text=f"Это число {bs.left}!")
        return
    answer()


window = Tk()
window.title("Guess number")
window.geometry('500x200')
lbl = Label(window, text="Загадайте число от 1 до 1000 \n и я угадаю его", font=("Consolas", 18))
lbl.grid(column=0, row=0, columnspan = 10)

btn_start = Button(window, text="Начать", command=start)
btn_restart = Button(window, text="Начать сначала", command=restart)
btn_yes = Button(window, text="Да", command=yes)
btn_no = Button(window, text="Нет", command=no)

btn_start.grid(column = 0, row = 1)


bs = Bs()

window.mainloop()

