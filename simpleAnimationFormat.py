# -----------------------------------------------------
# Framework for writing tkinter animations in one line!
# -----------------------------------------------------

# timerFired
timer = lambda d: 0

# keyPressed
key = lambda e, d: 0

# mouseClicked
mouse = lambda e, d: d['circles'].append((e.x, e.y))

# redrawAll
redraw = lambda c, d: [c.create_oval(x-20, y-20, x+20, y+20, fill="red") for (x, y) in d['circles']]


# redrawAllWrapper
rW = lambda tk, c, d, r: (c.delete(tk.ALL),
	c.create_rectangle(0, 0, d['width'], d['height'],
                            fill='black', width=0),
	r(c, d),
	c.update())

	
# mouseWrapper
mW = lambda tk, e, c, d, m: (m(e, d),
	rW(tk, c, d, redraw))

# keyWrapper
kW = lambda tk, e, c, d, k: (k(e, d),
	rW(tk,c, d, redraw))


# NOTE: since tW is recursive, and one-liners don't have names for functions,
# 		we will 'name' this function inside of our data dictionary so we have
#		some semblance of recursion

# data
data = {
		'circles': [], 
		'width': 500, 
		'height': 500, 
		'tD': 100, 
		'tW': lambda tk, c, d, t: (t(d),
			  		rW(tk, c, d, redraw),
					c.after(d['tD'], d['tW'], tk, c, d, t)) # this line... hahaha
	   }

	
# run function
run = lambda t, d, r, c: (c.configure(bd=0, highlightthickness=0), c.pack(), r.bind("<Button-1>", lambda event: mW(t, event, c, d, mouse)), r.bind("<Key>", lambda event: kW(t, event, c, d, key)), tW(t, c, d, timer), r.mainloop())

# setting up stuff for the run function (tkinter, data, root, canvas)
(lambda t: (lambda r, t: run(t, data, r, t.Canvas(r, width=500, height=500)))(t.Tk(), t))((lambda: __import__("tkinter"))())
