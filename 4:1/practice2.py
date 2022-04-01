a = "-"

for i in range(1, 6):
    if i == 3:
        continue
    for a in range(1, 26):
        if a == 25:
            break
        print(a)
    print(i)
print("------------------------------------------")
print(2+3*5-7)
print((2+3)*5-7)
print(7 > 12 or 5+7 > 14)