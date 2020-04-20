import collections
d = collections.OrderedDict(one=1, two=2, three=3)

print(d)
d['four'] = 4
print(d)

print(d.keys())
print(d.items())
print(len(d))
for i, item in enumerate(d):
    print(i, item)

print([(i, value) for i, value in enumerate(d)])
