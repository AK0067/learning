# learning vars in py
age = 15
name = "Aurea"
print("Hi, I'm " + name + ", I'm about " + str(age) + " years old right now, as for what I'm doing, I'm learning Python :(");
# second type vars, the one above was very simple useage of vars, now let's experiment a bit ;)
x = "who tf are u?" # this bro will get overwritten
x = "who're you?" # this bro overwrites
print("Now, " + x);
# float in the air /j
y = str(1)
z = int(2)
a = float(3)
print("So, do you like the number: " + y + str(z) + str(a) + "?")
# the types ah nah this ain't no ts
print("Right now learnt these types of vars:")
print(type(y))
print(type(z))
print(type(a))
# now it's the better creation of vars with the lifesaved f string, so excited!
b, c, d = "I'm", "curious", "about what"
print(f"So, now {b} a bit {c} {d} are you.")
# well this is just a wasteage but sure, and here we're again with the f string, oh and don't worry I'm not addicted to it ;)
e=f= g = "Well"
print(f"{e} will you answer me?")
print(f"{f}, seems like your a thick headed.")
print(f"{g}, nevermind you are just a tough neck which got cracked easily.")
# unpacking stuff, oh nah this ain't unpacking the stuff purchased from stores
birbs = ["Ostrich", "Parakeet", "Crow"]
h, i, j = birbs
print(f"So which birb do you like? {h}? {i}? {j}?")
# vars but it's meth ;) oh and ofc an f string is always there
k = 1
l = 0
print(f"I know your an idiot, so do you think that {k} + {l} = {k + l}?")
print("I know you don't think so, because your just some random idiot.")
# global vars testing
