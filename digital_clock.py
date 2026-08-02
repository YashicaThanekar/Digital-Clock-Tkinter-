from tkinter import *
from datetime import datetime
from tkinter import messagebox

# ---------------- CLOCK WINDOW ----------------
root = Tk()
root.title("Digital Clock")
root.geometry("1000x400+300+170")
root.resizable(False, False)
root.configure(bg="pink")

f = ("Cambria", 130, "bold")
bf = ("Cambria", 20, "bold")

def clock():
    sw.withdraw()
    t.withdraw()
    root.deiconify()

def stopwatch():
    root.withdraw()
    t.withdraw()
    sw.deiconify()

def timer():
    sw.withdraw()
    root.withdraw()
    t.deiconify()

Button(root, text="Clock", font=bf, command=clock, bg="Violetred4", fg="white").place(x=330, y=20)
Button(root, text="Stopwatch", font=bf, command=stopwatch, bg="Violetred4", fg="white").place(x=430, y=20)
Button(root, text="Timer", font=bf, command=timer, bg="Violetred4", fg="white").place(x=590, y=20)

lab_msg = Label(root, text="", font=f, bg="pink", fg="red4")
lab_msg.place(x=150, y=90)

def show_clock():
    dt = datetime.now()
    msg = f"{dt.hour:02}:{dt.minute:02}:{dt.second:02}"
    lab_msg.config(text=msg)
    root.after(1000, show_clock)

show_clock()


# ---------------- STOPWATCH ----------------
sw = Toplevel()
sw.withdraw()
sw.title("StopWatch")
sw.geometry("1000x400+300+170")
sw.resizable(False, False)
sw.configure(bg="pink")

tb = ("Cambria", 17, "bold")

Button(sw, text="Clock", font=bf, command=clock, bg="Violetred4", fg="white").place(x=330, y=20)
Button(sw, text="Stopwatch", font=bf, command=stopwatch, bg="Violetred4", fg="white").place(x=430, y=20)
Button(sw, text="Timer", font=bf, command=timer, bg="Violetred4", fg="white").place(x=590, y=20)

hr = 0
mn = 0
sec = 0
running = False

label1 = Label(sw, text="00:00:00", font=f, bg="pink", fg="red4")
label1.place(x=150, y=90)

def show():
    global hr, mn, sec, running

    if running:
        sec += 1

        if sec == 60:
            sec = 0
            mn += 1

        if mn == 60:
            mn = 0
            hr += 1

        label1.config(text=f"{hr:02}:{mn:02}:{sec:02}")
        sw.after(1000, show)

def start():
    global running
    if not running:
        running = True
        show()

def stop():
    global running
    running = False

def reset():
    global hr, mn, sec, running
    running = False
    hr = mn = sec = 0
    label1.config(text="00:00:00")

Button(sw, text="Start", font=tb, command=start).place(x=350, y=300)
Button(sw, text="Stop", font=tb, command=stop).place(x=470, y=300)
Button(sw, text="Reset", font=tb, command=reset).place(x=590, y=300)


# ---------------- TIMER ----------------
t = Toplevel()
t.withdraw()
t.title("Timer")
t.geometry("1000x400+300+170")
t.resizable(False, False)
t.configure(bg="pink")

Button(t, text="Clock", font=bf, command=clock, bg="VioletRed4", fg="white").place(x=330, y=20)
Button(t, text="Stopwatch", font=bf, command=stopwatch, bg="VioletRed4", fg="white").place(x=430, y=20)
Button(t, text="Timer", font=bf, command=timer, bg="VioletRed4", fg="white").place(x=590, y=20)

label2 = Label(t, text="00:00:00", font=f, bg="pink", fg="red4")
label2.place(x=150, y=130)

running_timer = False
total = 0

def countdown():
    global total, running_timer

    if not running_timer:
        return

    hr = total // 3600
    mn = (total % 3600) // 60
    sec = total % 60

    label2.config(text=f"{hr:02}:{mn:02}:{sec:02}")

    if total > 0:
        total -= 1
        t.after(1000, countdown)
    else:
        running_timer = False
        for i in range(5):
            t.after(i * 500, root.bell)
        messagebox.showinfo("Timer", "Time's Up!")

def start_timer():
    global total, running_timer

    if total == 0:
        h = hour.get().strip()
        m = minute.get().strip()
        s = second.get().strip()

        if h == "" or m == "" or s == "":
            messagebox.showerror("Input Error", "Ensure all fields are filled")
            return

        if not (h.isdigit() and m.isdigit() and s.isdigit()):
            messagebox.showerror("Input Error", "Ensure all fields are numeric")
            return

        if len(h) > 2 or len(m) > 2 or len(s) > 2:
            messagebox.showerror("Input Error", "Max 2 digits allowed")
            return

        total = int(h) * 3600 + int(m) * 60 + int(s)

    if total > 0:
        running_timer = True
        countdown()

def stop_timer():
    global running_timer
    running_timer = False

def reset_timer():
    global running_timer, total

    running_timer = False
    total = 0
    label2.config(text="00:00:00")

    hour.delete(0, END)
    minute.delete(0, END)
    second.delete(0, END)

    hour.insert(0, "0")
    minute.insert(0, "0")
    second.insert(0, "0")


Label(t, text="Hours", font=tb, bg="pink").place(x=340, y=90)
Label(t, text="Minutes", font=tb, bg="pink").place(x=460, y=90)
Label(t, text="Seconds", font=tb, bg="pink").place(x=580, y=90)

hour = Spinbox(t, from_=0, to=23, width=5, font=tb)
hour.place(x=340, y=120)

minute = Spinbox(t, from_=0, to=59, width=5, font=tb)
minute.place(x=460, y=120)

second = Spinbox(t, from_=0, to=59, width=5, font=tb)
second.place(x=580, y=120)

Button(t, text="Start", font=tb, command=start_timer).place(x=330, y=330)
Button(t, text="Stop", font=tb, command=stop_timer).place(x=470, y=330)
Button(t, text="Reset", font=tb, command=reset_timer).place(x=610, y=330)

root.mainloop()