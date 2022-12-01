s=... # input
# Part 1
print(max(eval(s.replace(*'\n+').replace('++',","))))
# Part 2
print(sum(sorted(eval(s.replace(*'\n+').replace('++',",")))[-3:]))
# Both parts (prints in order of part 2, part 1)
print(sum(v:=sorted(eval(open(0).read().replace(*'\n+').replace('++',",")))[-3:]),v[2])
