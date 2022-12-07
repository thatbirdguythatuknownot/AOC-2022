s=... # input
# Part 1
s=[];d=()
for r in open(0):
 a,*_,b=r.split()
 if'/'>b:*s,v=s;d+=v,;s[-1]+=v
 elif'$ d'>r:s+=0,
 if'/'<a<':':s[-1]+=int(a)
print(sum(_*(1e5>_)for _ in d))
# Part 2
s=[];d=()
for r in open(0):
 a,*_,b=r.split()
 if'/'>b:*s,v=s;d+=v,;s[-1]+=v
 elif'$ d'>r:s+=0,
 if'/'<a<':':s[-1]+=int(a)
print(min(_ for _ in d if _>sum(s)-4e7))
# Both parts
s=[];d=()
for r in open(0):
 a,*_,b=r.split()
 if'/'>b:*s,v=s;d+=v,;s[-1]+=v
 elif'$ d'>r:s+=0,
 if'/'<a<':':s[-1]+=int(a)
print(sum(_*(1e5>_)for _ in d),min(_ for _ in d if _>sum(s)-4e7))
