lambda l, w: list(filter(lambda x: True in [True if w in inserts else False for inserts in [[x[:i] + c + x[i+1:] for c in string.ascii_lowercase] for i in range(len(x))]], list(filter(lambda x: len(x) == len(w), l))))