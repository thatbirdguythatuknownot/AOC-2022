s=... # input
# Part 1
print(sum(1-(a>c<=d<b or d>b>=a<c)for a,b,c,d in[eval(l.replace(*'-,'))for l in s.split('\n')]))
# Part 2
print(sum(a<=d>=c<=b for a,b,c,d in[eval(l.replace(*'-,'))for l in s.split('\n')]))
# Both parts
print(sum(1-(a>c<=d<b or d>b>=a<c)+1j*(a<=d>=c<=b)for a,b,c,d in[eval(l.replace(*'-,'))for l in s.split('\n')]))
