s = "one+two+one-two"
k, g= [], []
d = ""
for i in s:
    if i.isalpha():
        d = d+i
    else:
        k.append(1 if d == "one" else 2)
        g.append(i)
        d = ""
if d:
    k.append(1 if d == "one" else 2)
sum = k[0]
for i in range(1, len(k)):
    if g[i-1] ==  "+":
        sum = sum + k[i]
    else:
        sum = sum - k[i]
print(sum)
