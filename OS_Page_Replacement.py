from tkinter import *
import time
import matplotlib.pyplot as plt
import random
import seaborn as sns
import numpy as np
import pandas as pd
import cufflinks as cf
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

init_notebook_mode(connected=True)


# Selecting Algorithms According to Radio Button Selected
def check():
    if v1.get() == 1:
        fifo()
    if v1.get() == 2:
        sca()
    if v1.get() == 3:
        rp()
    if v1.get() == 4:
        opr()
    if v1.get() == 5:
        lifo()


def get_index(a, b, c):
    lll = []

    for x in a:
        if x not in b[c:]:
            lll.append(-1)
        else:
            lll.append(b.index(x, c))
    if -1 in lll:
        return len(a) - 1 - lll[::-1].index(-1)
    else:
        return a.index(b[max(lll)])


# 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1


def op(main_ll, n_miss, n_hit, frm, ll, l_tf, hit_rec, miss_rec, g_l):
    owin = Tk()
    owin.geometry("1300x1200")
    owin.title("Output")
    color = "#8AE9ED"

    # print(main_ll)
    # print(n_miss)
    # print(n_hit)
    # print(frm)
    # print(ll)
    # print(l_tf)

    x = 25
    y = 25
    for i in range(frm + 1):
        if i == 0:
            ee = Label(owin, text=" ", borderwidth=2, relief="solid", font="montserrat 10 bold",
                       bg=color, fg="#0C424B", wraplength=25)
            ee.pack()
            ee.place(x=x, y=y, height=35, width=35)
        else:
            x = x + 35
            ee = Label(owin, text="F" + str(i), borderwidth=2, relief="solid", font="montserrat 10 bold",
                       bg=color, fg="#0C424B", wraplength=25)
            ee.pack()
            ee.place(x=x, y=y, height=35, width=35)
            owin.update()

    for j in range(len(ll)):
        color = "#8AE9ED"
        if l_tf[j] == True:
            color = "red"
            s1 = "H"
        else:
            s1 = "F"

        x = 25
        y += 35
        ee = Label(owin, text=s1, borderwidth=2, relief="solid", font="montserrat 10 bold",
                   bg=color, fg="#0C424B", wraplength=25)
        ee.pack()
        ee.place(x=x, y=y, height=35, width=35)

        for k in range(frm):
            x += 35
            e = Label(owin, text=str(main_ll[j][k]), borderwidth=2, relief="solid",
                      font="montserrat 10 bold", bg=color, fg="#0C424B", wraplength=25)
            e.pack()
            e.place(x=x, y=y, height=35, width=35)
        owin.update()
        time.sleep(1)
    l5 = Label(owin, text="Page Missed = " + str(n_miss), font="montserrat 15 bold")
    l5.pack()
    l5.place(x=(25 + frm * 35) + 100, y=int(y / 2) - 20, height=50, width=200)
    l6 = Label(owin, text="Page hit = " + str(n_hit), font="montserrat 15 bold")
    l6.pack()
    l6.place(x=(25 + frm * 35) + 100, y=int(y / 2) + 20, height=50, width=200)
    graph(hit_rec, miss_rec, ll, owin, g_l)


def graph(ht, flt, lll, ow, g_ll):
    fig = plt.figure(figsize=(5, 8), dpi=85)
    plt.subplot(2, 1, 1)
    # plt.title("HIT vs Page Sequence")
    plt.xlabel("No.of Frames --->")
    plt.ylabel("Hit --->")
    plt.plot(g_ll, ht, marker='o', color="red")
    plt.subplot(2, 1, 2)
    plt.xlabel("No. of Frames --->")
    plt.ylabel("Fault --->")
    # plt.title("Fault vs Page Sequence")
    plt.plot(g_ll, flt, marker='x', color="blue", ls="--")

    canvas = FigureCanvasTkAgg(fig, master=ow)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(x=800, y=10)


def sca():
    l = [int(h) for h in list(e2.get().split())]

    main_l = []

    hit_record = []
    miss_record = []
    ll = [False for x in range(len(l))]

    u = int(e1.get())
    g_ll = [c for c in range(u + 3)]

    for iii in g_ll:
        ref = [0 for z in range(iii)]
        flt = 0
        ht = 0
        front = 0
        miss = 0
        cnt = 0
        if iii == 0:
            hit_record.append(0)
            miss_record.append(0)
            continue
        m = ['  ' for z in range(iii)]
        for i in range(len(l)):
            y = m.copy()
            if l[i] in m:
                k = m.index(l[i])
                ref[k] = 1
                # front += 1
                cnt += 1
                # ht = cnt
                # flt = miss
                # hit_record.append(ht)
                # miss_record.append(flt)
                y = m.copy()
                if iii == u:
                    yy = m.copy()
                    main_l.append(yy)
                    ll[i] = True
                continue
            else:
                while True:
                    if front >= iii:
                        front = 0
                    if ref[front] == 0:
                        m[front] = l[i]
                        y = m.copy()
                        miss += 1
                        # flt = miss
                        # ht = cnt
                        # miss_record.append(flt)
                        # hit_record.append(ht)
                        front += 1
                        if iii == u:
                            yy = m.copy()
                            main_l.append(yy)
                        # if front >= u:
                        #    front = 0
                        break
                    else:
                        ref[front] = 0
                        front += 1
                        continue
        hit_record.append(cnt)
        miss_record.append(miss)
    op(main_l, miss_record[u], hit_record[u], u, l, ll, hit_record, miss_record, g_ll)


def rp():
    no_of_frames = int(e1.get())
    sequence = [int(h) for h in list(e2.get().split())]

    answer = []
    h_record = []
    f_record = []
    g_ll = [c for c in range(no_of_frames + 3)]
    page_h = 0
    page_f = 0
    ll = [False for x in range(len(sequence))]
    for iii in g_ll:
        if iii == 0:
            h_record.append(0)
            f_record.append(0)
            continue
        page_hit = 0
        page_fault = 0
        current_frame = [' ' for i in range(iii)]

        for i in range(len(sequence)):
            if sequence[i] in current_frame:

                # print(current_frame)
                page_hit += 1
                if iii == no_of_frames:
                    answer.append(list(current_frame))
                    ll[i] = True
                # page_h = page_hit
                # h_record.append(page_h)
                # page_f = page_fault
                # f_record.append(page_f)

            else:
                if page_fault < iii:
                    current_frame[page_fault] = sequence[i]

                else:
                    random_index = random.randint(0, iii - 1)
                    current_frame[random_index] = sequence[i]

                page_fault += 1
                # page_f = page_fault
                # f_record.append(page_f)
                # page_h = page_hit
                # h_record.append(page_h)
                # # print(current_frame)
                if iii == no_of_frames:
                    answer.append(list(current_frame))
        h_record.append(page_hit)
        f_record.append(page_fault)
    op(answer,f_record[no_of_frames],h_record[no_of_frames], no_of_frames, sequence, ll, h_record, f_record, g_ll)


def fifo():
    l = [int(h) for h in list(e2.get().split())]

    main_l = []
    hit_record = []
    miss_record = []
    u = int(e1.get())
    g_ll = [c for c in range(u + 3)]
    # m = [' ' for z in range(u)]
    ll = [False for x in range(len(l))]
    for iii in range(u + 3):
        front = 0
        back = -1
        miss = 0
        cnt = 0
        if iii == 0:
            hit_record.append(0)
            miss_record.append(0)
            continue
        m = [' ' for z in range(iii)]
        for i in range(len(l)):
            y = m.copy()
            if l[i] in m:
                cnt += 1
                # ht=cnt
                # flt=miss
                # hit_record.append(ht)
                # miss_record.append(flt)
                y = m.copy()
                if iii == u:
                    main_l.append(y)
                    ll[i] = True
                continue
            else:
                back += 1
                if back >= iii:
                    m[front] = l[i]
                    y = m.copy()
                    miss += 1
                    # flt=miss
                    # ht=cnt
                    # miss_record.append(flt)
                    # hit_record.append(ht)
                    front += 1
                    if iii == u:
                        main_l.append(y)
                    if front >= iii:
                        front = 0
                else:
                    miss += 1
                    m[back] = l[i]
                    # flt = miss
                    # ht=cnt
                    # hit_record.append(ht)
                    # miss_record.append(flt)
                    y = m.copy()
                    if iii == u:
                        main_l.append(y)
        hit_record.append(cnt)
        miss_record.append(miss)
    op(main_l, miss_record[u], hit_record[u], u, l, ll, hit_record, miss_record, g_ll)


def lifo():
    l = [int(h) for h in list(e2.get().split())]
    main_l = []
    hit_record = []
    miss_record = []
    u = int(e1.get())

    ll = [False for x in range(len(l))]
    g_ll = [c for c in range(u + 3)]
    for iii in g_ll:
        front = 0
        back = -1
        cnt = 0
        miss = 0
        if iii == 0:
            hit_record.append(0)
            miss_record.append(0)
            continue
        m = [' ' for z in range(iii)]
        for i in range(len(l)):
            y = m.copy()
            if l[i] in m:
                cnt += 1
                # ht=cnt
                # flt=miss
                # hit_record.append(ht)
                # miss_record.append(flt)
                y = m.copy()
                if iii == u:
                    main_l.append(y)
                    ll[i] = True
                continue
            else:
                back += 1
                if back >= iii:
                    back = iii - 1
                m[back] = l[i]
                y = m.copy()
                miss += 1
                # flt=miss
                # ht=cnt
                # miss_record.append(flt)
                # hit_record.append(ht)
                if iii == u:
                    main_l.append(y)
        miss_record.append(miss)
        hit_record.append(cnt)
    op(main_l, miss_record[u], hit_record[u], u, l, ll, hit_record, miss_record, g_ll)


def opr():
    l = [int(h) for h in list(e2.get().split())]

    main_l = []
    hit_record = []
    miss_record = []
    u = int(e1.get())
    g_ll = [c for c in range(u + 3)]

    ll = [False for x in range(len(l))]
    for iii in g_ll:
        miss = 0
        cnt = 0
        front = 0
        back = -1
        m = [' ' for z in range(iii)]
        if iii == 0:
            hit_record.append(0)
            miss_record.append(0)
            continue
        for i in range(len(l)):
            y = m.copy()
            if l[i] in m:
                cnt += 1

                y = m.copy()
                if iii == u:
                    yy = m.copy()
                    main_l.append(yy)
                    ll[i] = True
                continue
            else:
                back += 1
                if back >= iii:
                    back = get_index(y, l, i)
                m[back] = l[i]
                y = m.copy()
                miss += 1

                if iii == u:
                    yy = m.copy()
                    main_l.append(yy)
        hit_record.append(cnt)
        miss_record.append(miss)

    op(main_l, miss_record[u], hit_record[u], u, l, ll, hit_record, miss_record, g_ll)


if __name__ == "__main__":
    win = Tk()
    win.title("Page Replacement Algorithms")
    win.geometry("700x700")
    l0 = Label(win, pady=10, text="Page Replacement Algorithms", font="montserrat 25 bold")
    l0.pack()
    l0.place(x=0, y=2)
    l1 = Label(win, text="Enter No of Frames     :", font="montserrat 12 bold", pady=7)
    l1.pack()
    l1.place(x=0, y=75)
    e1 = Entry(win, width=5)
    e1.pack(pady=10)
    e1.place(x=200, y=86, height=20)
    l2 = Label(win, text="Enter Page Reference :", font="montserrat 12 bold", pady=10)
    l2.pack()
    l2.place(x=0, y=120)
    e2 = Entry(win, width=30)
    e2.pack()
    e2.place(x=200, y=134, height=20)

    global v1
    global v2
    global v3

    v1 = IntVar()

    # RadioButtons
    r1 = Radiobutton(win, text="First In First Out :: (FIFO)", variable=v1, value=1, font="montserrat 12 bold",
                     borderwidth=2, activebackground="black", activeforeground="white")
    r1.select()
    r1.pack()
    r1.place(x=0, y=175, height=25)
    r2 = Radiobutton(win, text="Second Chance Algorithm :: (LRU)", variable=v1, value=2, font="montserrat 12 bold",
                     borderwidth=2, activebackground="black", activeforeground="white")
    r2.pack()
    r2.place(x=0, y=200, height=25)
    r3 = Radiobutton(win, text="Random Page Replacement Algorithm", variable=v1, value=3, font="montserrat 12 bold",
                     borderwidth=2, activebackground="black", activeforeground="white")
    r3.pack()
    r3.place(x=0, y=225, height=25)
    r4 = Radiobutton(win, text="Optimal Page Replacement Algorithm", variable=v1, value=4, font="montserrat 12 bold",
                     borderwidth=2, activebackground="black", activeforeground="white")
    r4.pack()
    r4.place(x=0, y=250, height=25)
    r5 = Radiobutton(win, text="Last In First Out :: (LIFO)", variable=v1, value=5, font="montserrat 12 bold",
                     borderwidth=2, activebackground="black", activeforeground="white")
    r5.pack()
    r5.place(x=0, y=275, height=25)

    btn = Button(win, text="Click to Get Output", font="montserrat 12", width=30, command=check,
                 activebackground="black", activeforeground="white")
    btn.pack()
    btn.place(x=150, y=320, height=30)
    win.mainloop()
