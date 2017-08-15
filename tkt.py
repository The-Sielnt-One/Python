import Tkinter as tk
app=tk.Tk()
app.title("Test")
app.geometry("400x400+200+200")

LT=tk.StringVar()
LT.set("Click button")
L1 = tk.Label(app, textvariable=LT, height=4)
L1.pack()

CBV=tk.IntVar()
CB1= tk.Checkbutton(app, variable=CBV , text="Fuck")
CB1.pack()

CN=tk.StringVar(None)
YN=tk.Entry(app, textvariable=CN)
YN.pack()




app.mainloop()
