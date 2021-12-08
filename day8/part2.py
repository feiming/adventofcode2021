from os import chflags
import pprint
f = open("input", "r")
data = [x.rstrip("\n") for x in f if x.rstrip("\n") != ""]
data = [{"signal": i.split("|")[0].strip(), "output": i.split("|")[
    1].strip()} for i in data]


def decode(input):
    unique = sorted(input.split(" "), key=len)
    cf = set()
    bd = set()
    ef = set()
    be = set()
    a = set()
    b = set()
    c = set()
    d = set()
    e = set()
    f = set()
    g = set()
    for i in unique:
        i = set(i)
        if len(i) == 2:
            # 1
            cf = i
        elif len(i) == 3:
            # 7
            if cf:
                a = i - cf
        elif len(i) == 4:
            # 4
            if cf:
                bd = i - cf
        elif len(i) == 6:
            if bd.issubset(i) and cf.issubset(i):
                g = i - a - bd - cf
            elif set(bd).issubset(set(i)):
                ef = i - a - bd - g
            elif set(cf).issubset(set(i)):
                be = i - a - cf - g

        f = ef - be - g
        b = be - ef - g
        e = ef - cf - g
        c = cf - ef
        d = bd - be
    return a, b, c, d, e, f, g


def translate(input, a, b, c, d, e, f, g):
    output = input.split(" ")
    number = ""
    print(
        f"a={a} , b={b} , c={c} , d={d} , e={e} , f={f} , g={g}")
    for i in output:
        if len(i) == 7:
            number += "8"
        elif len(i) == 4:
            number += "4"
        elif len(i) == 3:
            number += "7"
        elif len(i) == 2:
            number += "1"
        elif len(i) == 5:
            # ab d fg
            if not c.issubset(set(i)) and not e.issubset(set(i)):
                number += "5"
            # a cd fg
            elif not b.issubset(set(i)) and not e.issubset(set(i)):
                number += "3"
            # a cde g
            elif not b.issubset(set(i)) and not f.issubset(set(i)):
                number += "2"
        elif len(i) == 6:
            # abcd fg
            if not e.issubset(set(i)):
                number += "9"
            # ab defg
            elif not c.issubset(set(i)):
                number += "6"
            # abc efg
            elif not d.issubset(set(i)):
                number += "0"
    return number


total = 0
for x in data:
    a, b, c, d, e, f, g = decode(x['signal'])
    number = translate(x['output'], a, b, c, d, e, f, g)
    sort_signal = sorted(x['output'].split(' '), key=len)
    total += int(number)
print(total)


# 1=  c  f
# 7=a c  f
# 4= bcd f

# 2=a cde g
# 3=a cd fg
# 5=ab d fg

# 6=ab defg
# 0=abc efg
# 9=abcd fg
# 8=abcdefg

# a={'a'} , b={'e'} , c={'b'} , d={'c'} , e={'f'} , f={'g'} , g={'d'}
#['bg', 'abg', 'bceg', 'abcfg', 'acefg', 'abcdf', 'abcefg', 'acdefg', 'abdefg', 'abcdefg']
# 1 = c=b f=g
# 7 = a=a c=b f=g
# 4 = b=e c=b d=c  f=g
# = a=a c=b d=c e=f f=g
'''
a={'d'} , b={'b'} , c={'f'} , d={'c'} , e={'e', 'a'} , f={'g'} , g={'a'}
['fg', 'dfg', 'bcfg', 'acdfg', 'acdef', 'abcdg', 'abdefg', 'abcdeg', 'abcdfg', 'abcdefg']
['acdfg', 'abcdg', 'abdefg', 'abcdeg'] = 5599
'''
