def digit(d, s=''): return d if not s else eval(str(d) + s)
def zero(	s=''): 	return digit(0, s)
def one(	s=''): 	return digit(1, s)
def two(	s=''): 	return digit(2, s)
def three(	s=''): 	return digit(3, s)
def four(	s=''): 	return digit(4, s)
def five(	s=''): 	return digit(5, s)
def six(	s=''): 	return digit(6, s)
def seven(	s=''): 	return digit(7, s)
def eight(	s=''): 	return digit(8, s)
def nine(	s=''): 	return digit(9, s)

def operator(o, s):	return o + str(s)
def plus(d): 		return operator("+", d)
def minus(d): 		return operator("-", d)
def times(d): 		return operator("*", d)
def divided_by(d): 	return operator("//", d)