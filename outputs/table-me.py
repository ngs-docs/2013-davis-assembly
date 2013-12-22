import sys

data = open(sys.argv[1]).read()
data = data.split('\n\n')

x = []

for r in data:
    if not r.strip():
        continue
    r = r.splitlines()
    a, b = r[:2]
    c = " ".join(r[2:-1])
    d = r[-1]

    x.append((a,b,c,d))

len_a = max([ len(a) for (a, b, c, d) in x ])
len_b = max([ len(b) for (a, b, c, d) in x ])
len_c = max([ len(c) for (a, b, c, d) in x ])
len_d = max([ len(d) for (a, b, c, d) in x ])

#print x
#print len_a, len_b, len_c, len_d

format_str = '| %%%ds | %%%ds | %%%ds | %%%ds |\n' % (len_a, len_b, len_c, len_d)

sys.stdout.write('+%s+%s+%s+%s+\n' % ('-' * (len_a + 2), '-'* (len_b + 2), '-'*(len_c + 2), '-'*(len_d + 2)))

for a, b, c, d in x:
    sys.stdout.write(format_str % (a,b,c,d))
    sys.stdout.write('+%s+%s+%s+%s+\n' % ('-' * (len_a + 2), '-'* (len_b + 2), '-'*(len_c + 2), '-'*(len_d + 2)))
