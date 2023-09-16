
import json
import jsonapi
import random


for i in range(10):
    c = complex(random.random(), random.random())
    j_c = json.dumps(c, cls=jsonapi.MyEncoder)
    print(j_c)
    un_j_c = json.loads(j_c, cls=jsonapi.MyDecoder)
    print(un_j_c)

for i in range(10):
    r = range(random.randint(-10, 10),
              random.randint(-10, 10), random.randint(1, 4))
    r_c = json.dumps(r, cls=jsonapi.MyEncoder)
    print(r_c)
    un_r_c = json.loads(r_c, cls=jsonapi.MyDecoder)
    print(un_r_c)
