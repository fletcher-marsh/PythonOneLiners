(lambda t: (lambda r, t: (lambda t, d, r, c: (c.configure(bd=0, highlightthickness=0), c.pack(), r.bind("<Button-1>", lambda event: (lambda tk, e, c, d, m: (m(e, d), (lambda tk, c, d, r: (c.delete(tk.ALL), c.create_rectangle(0, 0, d['width'], d['height'], fill='black', width=0), r(c, d), c.update()))(tk, c, d, lambda c, d: [c.create_oval(x-20, y-20, x+20, y+20, fill="red") for (x, y) in d['circles']])))(t, event, c, d, lambda e, d: d['circles'].append((e.x, e.y)))), r.bind("<Key>", lambda event: (lambda tk, e, c, d, k: (k(e, d), (lambda tk, c, d, r: (c.delete(tk.ALL), c.create_rectangle(0, 0, d['width'], d['height'], fill='black', width=0), r(c, d), c.update()))(tk,c, d, lambda c, d: [c.create_oval(x-20, y-20, x+20, y+20, fill="red") for (x, y) in d['circles']])))(t, event, c, d, lambda e, d: 0)), d['tW'](t, c, d, lambda d: 0), r.mainloop()))(t, {'circles': [], 'width': 500, 'height': 500, 'tD': 100, 'tW': (lambda tk, c, d, t: (t(d), (lambda tk, c, d, r: (c.delete(tk.ALL), c.create_rectangle(0, 0, d['width'], d['height'], fill='black', width=0), r(c, d), c.update()))(tk, c, d, lambda c, d: [c.create_oval(x-20, y-20, x+20, y+20, fill="red") for (x, y) in d['circles']]), c.after(d['tD'], d['tW'], tk, c, d, t)))}, r, t.Canvas(r, width=500, height=500)))(t.Tk(), t))((lambda: __import__("tkinter"))())