s=... # input
# Part 1
l=s.split('\n');r=*zip(*l),;s=0
for _ in range(9801):i=_//99;j=_%99;t=l[i];s+=min(eval("max(%ror'/'),"*4%(u:=(t[j+1:-1],t[:j][::-1],r[j][i+1:],r[j][:i][::-1]))))<t[j]
print(s)
# Part 2
l=s.split('\n');r=*zip(*l),;e=0
for _ in range(9801):
 i=_//99;j=_%99;t=l[i];v,w,x,y=eval("(z:=1)and sum(z and(x<t[j]or(z:=0))for x in%r),"*4%(u:=(t[j+1:-1],t[:j][::-1],r[j][i+1:],r[j][:i][::-1])));m,n,o,p=map(len,u);v+=v<m;w+=w<n;x+=x<o;y+=y<p;c=v*w*x*y
 if c>e:e=c
print(e)
# Both parts
l=*open(0),;r=*zip(*l),;e=s=0
for _ in range(9801):
 i=_//99;j=_%99;t=l[i];s+=min(eval("max(%ror'/'),"*4%(u:=(t[j+1:-1],t[:j][::-1],r[j][i+1:],r[j][:i][::-1]))))<t[j];v,w,x,y=eval("(z:=1)and sum(z and(x<t[j]or(z:=0))for x in%r),"*4%u);m,n,o,p=map(len,u);v+=v<m;w+=w<n;x+=x<o;y+=y<p;c=v*w*x*y
 if c>e:e=c
print(s,e)
