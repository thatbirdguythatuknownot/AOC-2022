s=... # input
# Part 1
m=[];d=()
for r in s.split('\n'):
 a,*_,b=r.split()
 if'/'>b:*m,v=m;d+=v,;m[-1]+=v
 elif'$ d'>r:m+=0,
 if'/'<a<':':m[-1]+=int(a)
print(sum(_*(1e5>_)for _ in d))
# Part 2
m=[];d=()
for r in s.split('\n'):
 a,*_,b=r.split()
 if'/'>b:*m,v=m;d+=v,;m[-1]+=v
 elif'$ d'>r:m+=0,
 if'/'<a<':':m[-1]+=int(a)
print(min(_ for _ in d if _>sum(m)-4e7))
# Both parts
m=[];d=()
for r in s.split('\n'):
 a,*_,b=r.split()
 if'/'>b:*m,v=m;d+=v,;m[-1]+=v
 elif'$ d'>r:m+=0,
 if'/'<a<':':m[-1]+=int(a)
print(sum(_*(1e5>_)for _ in d),min(_ for _ in d if _>sum(m)-4e7))
