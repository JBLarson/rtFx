#import packages
import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

#import forex input module
import input_forex as inp

#localize initial set (strike range), pointed sets (b1 / s1), and cartesian product (net)
strike_range = inp.stk_rng
net_results = inp.net_rez
b1_results = inp.b1_rez
s1_results = inp.s1_rez

#forex buy mpl tkinter function
def buy_plot():
    root = tkinter.Tk()
    root.wm_title("Buy USD/JPY>109.25")
    fig = Figure(figsize=(8, 6), dpi=100)

    fig.add_subplot(111).stackplot(strike_range, b1_results, labels=['b1'])
    #fig.add_subplot(111).stackplot(strike_range, s1_results, labels=['s1'])

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent Error
    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    tkinter.mainloop()


#forex sell mpl tkinter function
def sell_plot():
    root = tkinter.Tk()
    root.wm_title("Sell USD/JPY>109.44")
    fig = Figure(figsize=(8, 6), dpi=100)
    fig.add_subplot(111).stackplot(strike_range, s1_results, labels=['s1'])
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    tkinter.mainloop()


#forex net mpl tkinter function
def net_plot():
    root = tkinter.Tk()
    root.wm_title("Buy USD/JPY>109.25 Sell USD/JPY>109.44 - Net Position")
    fig = Figure(figsize=(8, 6), dpi=100)
    fig.add_subplot(111).stackplot(strike_range, net_results, labels=['net'])
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)
    tkinter.mainloop()

buy_plot()
sell_plot()
net_plot()
