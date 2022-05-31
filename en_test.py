from tkinter import Button, Tk
import tkinter as tk
from collections import defaultdict

# class MainWin(Tk):
#     def __init__(self, parent):
#         Tk.__init__(self, parent)
#         self.parent = parent
#         self.buttons = {}
#         self.dat = ["A", "B", "C", "D"]
#         self.init_widgets()
#
#     def init_widgets(self):
#         for i, d in enumerate(self.dat):
#             btn = Button(
#                 self,
#                 width=10,
#                 text=f"{i}-{d}",
#                 command=lambda x=i: self.on_click(x),
#             )
#             btn.grid(row=i, column=0)
#             self.buttons[i] = btn
#
#     def on_click(self, i):
#         print(f"{i} clicked")
#
#
# if __name__ == "__main__":
#     app = MainWin(None)
#     app.mainloop()

dat = ['A', 'B', 'C']

buttons = {}

app = Tk()
strs = defaultdict()
for i, d in enumerate(dat):
    btn = Button(
        width=10,
        text=f"{i}-{d}",
        command=lambda x=i: on_click(x),
    )
    btn.grid(row=i, column=0)
    buttons[i] = btn

def on_click(i):
    n_buttons = {}
    newWindow = tk.Toplevel(app)
    newWindow.title("new winddow @@")
    newWindow.geometry('320x240')
    n_dat = ['A','B','C']
    for j, d in enumerate(n_dat):
        strs[j] = tk.StringVar()
        strs[j].set("qwke" + d)
        n_btn = Button(newWindow,
            width=10,
            text=f"{d}-{j}",
            command=lambda x=j: new_click(x),
        )
        n_btn.grid(row=j, column=0)
        n_buttons[j] = btn
        input_text = tk.Entry(newWindow, textvariable=strs[j], width = 30)
        input_text.grid(row=j, column=1)

    print(f"{i} clicked")

def new_click(i):
    print(i)
    print(strs)

    print(str(strs[i].get())+ "clicked NEW")

app.mainloop()

#tk-inter 가이드
#https://towardsdatascience.com/empowering-docker-using-tkinter-gui-bf076d9e4974
#mac-os 가이드
#https://stackoverflow.com/questions/70722222/how-to-run-tkinter-inside-a-docker-container-on-macbook-pro


#https://hanseokhyeon.tistory.com/entry/Mac-Docker-%EC%97%90%EC%84%9C-GUI-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-python-matplotlib-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0