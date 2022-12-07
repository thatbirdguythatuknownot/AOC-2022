s=... # input
# Part 1
p=();d={}
for r in s.split('\n'):
 a,*_,b=r.split();q=()
 try:
  for x in p+('',):d[q]=d.get(q,0)+int(a);q+=x,
 except:p+=(b,)*('d 'in r)
 if'..'==b:p=p[:-2]
print(sum(d[_]*(1e5>d[_])for _ in d))
# Part 2
p=();d={}
for r in s.split('\n'):
 a,*_,b=r.split();q=()
 try:
  for x in p+('',):d[q]=d.get(q,0)+int(a);q+=x,
 except:p+=(b,)*('d 'in r)
 if'..'==b:p=p[:-2]
print(min(d[_]for _ in d if d[_]>d[()]-4e7))
# Both parts
p=();d={}
for r in s.split('\n'):
 a,*_,b=r.split();q=()
 try:
  for x in p+('',):d[q]=d.get(q,0)+int(a);q+=x,
 except:p+=(b,)*('d 'in r)
 if'..'==b:p=p[:-2]
print(sum(d[_]*(1e5>d[_])for _ in d),min(d[_]for _ in d if d[_]>d[()]-4e7))
