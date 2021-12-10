import tkinter as tk
import math

class Model():
    def __init__(self):
        self.a = 0
        self.judgeText = 0
        self.stopflag = False

    def flagModel(self):
        if self.stopflag == False:
            self.stopflag = True
        else:
            self.stopflag = False

    def judgeModel(self):
        if 150 <= self.a and self.a < 210:
            self.judgeText = 1
        elif 90 <= self.a and self.a < 150:
            self.judgeText = 2
        elif 30 <= self.a and self.a < 90:
            self.judgeText = 3
        elif 0 <= self.a and self.a < 30 or 330 <= self.a and self.a < 360:
            self.judgeText = 4
        elif 270 <= self.a and self.a < 330:
            self.judgeText = 5
        elif 210 <= self.a and self.a < 270:
            self.judgeText = 6

class View():
    def __init__(self, master, m, c):
        self.master = master
        self.m = m
        self.c = c

        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        r=0
        for i in range(6):
            self.canvas.create_arc(75,75,425,425,start=r,extent=60,fill="skyblue",width=2)
            r +=60

        j=1
        for z in [90,150,210,270,330,30]:
            x = ((200*(3**(1/2)))/3)*math.cos(math.radians(z))+250
            y = -100*math.sin(math.radians(z))+250
            self.canvas.create_text(x,y,text=j,font=("Helvetica", 50, "bold"),fill="blue")
            j+=1

        self.master.after(10, self.update)
        self.master.bind("<space>",self.c.flag_judge)

    def update(self):
        self.c.update()

        if self.m.stopflag == False:
            self.canvas.create_line(250,250,-125*math.sin(math.radians(self.m.a))+250,125*math.cos(math.radians(self.m.a))+250,fill="red",width=5,tag="player")
        else:
            self.canvas.create_text(450,450,text=self.m.judgeText,font=("Helvetica", 50, "bold"),fill="blue",tag="judgeText")

        self.master.after(10, self.update)

class Controller():
    def __init__(self, master, m):
        self.master = master
        self.m = m

    def flag_judge(self, event):
        self.m.flagModel()
        self.m.judgeModel()

    def update(self):
        if self.m.stopflag == False:
            self.v.canvas.delete("player")
            self.v.canvas.delete("judgeText")
            self.m.a = (self.m.a+10)%360

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("500x500")
        master.title("ルーレット")

        self.m = Model()
        self.c = Controller(master, self.m)
        self.v = View(master, self.m, self.c)

        self.c.v = self.v


def main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()


if __name__ == "__main__":

    main()
