import turtle as t

t.bgcolor("sky blue")
t.speed(0)

for x in  range(200):
    if x % 7 == 0:
        t.color("red")
    if x % 7 == 1:
        t.color("orange")
    if x % 7 == 2:
        t.color("yellow")
    if x % 7 == 3:
        t.color("green")
    if x % 7 == 4:
        t.color("blue")
    if x % 7 == 5:
        t.color("navy")
    if x % 7 == 6:
        t.color("purple")
    t.forward(x * 2)

    t.left(175)