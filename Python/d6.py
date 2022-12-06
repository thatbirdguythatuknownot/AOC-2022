s=... # input
# Part 1
i=0
while len({*s[i-4:i]})<4:i+=1
print(i)
# Part 2
i=0
while len({*s[i-14:i]})<14:i+=1
print(i)
# Both parts
i=0
for j in 4,14:
 while len({*s[i-j:i]})<j:i+=1
 print(i)
