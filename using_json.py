import json

# here are some rather complex Python structures
a = [{"name":"PC", "cost":500, "detail":{"a":"True", "b":[1,2,3,4]}},{"name":"Screen","cost":250, "detail":{"a":"False", "b":[9,8,7,6]}}]

print(a) # it is currently a list of dictionaries

a_j = json.dumps(a)

print(type(a_j))

b = json.loads(a_j)

print(type(b), b)

# alternatively we can serialize to bytes using pickle
import pickle
import datetime
now = datetime.datetime.utcnow()
p = pickle.dumps(now)
print(now, type(now), p, type(p))
# return to original structure
n = pickle.loads(p)
print(n, type(n))