(lambda t:
	(lambda t, r: 
		(lambda c, r: 
			(c.pack(), c.create_line(100, 100, 400, 400, fill="blue"), r.mainloop())
		)((lambda t, r: 
			t.Canvas(r, width=500, height=500)
		)(t,r), r)
	)(t, t.Tk())
)((lambda: __import__("tkinter"))())