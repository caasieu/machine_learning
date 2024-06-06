
a = [1,4,5,2,3]
b = [4,5,6]

def Union(a, b):
  # to avoid repetition using 'set'
  c = sorted(list(set(a) | set(b)))
  return c

def Intersection(a, b):
  c = [value for value in a if value in b]
  return c

union = Union(a, b)
intersection = Intersection(a, b)


print('union:', union)
print('intersection:', intersection)
