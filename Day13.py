# Strings are Immutable
a = "Akash"
print(len(a))
print(a.upper())
print(a.lower())

b = "!!!Harry!!!"
print(b.rstrip("!"))
print(b.strip("!"))

c = "!!!!!Harry!!!!!!!Harry!!!!!!!Cena!!!!!!!"
print(c.replace("Harry", "John"))
print((c.count("Harry")))
print(c.count("!"))
print(c.count("!!!"))
print(c.endswith("!!"))
print(len(c))
print(c.endswith("Cena",24, 33))

d = "Silver Spoon"
print(d.split(" "))

e = "hello worLd"
print(e.capitalize())
print(len(e))
print(len(e.center(50)))
print(e.center(50))

f = "My name is Akash"
print(f.find("is"))
print(f.find("he"))
print(f.index("is"))
# print(f.index("he"))

g = "Hello"
h = "hello!$"
i = "Hi there"
print(g.isalnum())
print(h.isalnum())
print(i.isalnum())

j = "Welcome"
k = "welcome0"
print(j.isalpha())
print(h.isalpha())

l = "Welcome to Python"
m = "Welcome to Python\n"
print(l.isprintable())
print(m.isprintable())

n = "       "
o = "Welcome t oPython"
print(n.isspace())
print(o.isspace())

p = "World Cup"
q = "World CUP"
r = "World of Cup"
print(p.istitle())
print(q.istitle())
print(r.istitle())

s = "Python is easy"
print(s.startswith("Py"))

t = "sWAP cASE"
print(t.swapcase())

u = "hello there"
print(u.title())