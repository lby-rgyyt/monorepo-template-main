import json
import jsonapi


c1 = complex(1, 2)

j_c1 = json.dumps(c1, cls=jsonapi.MyEncoder)
un_j_c1 = json.loads(j_c1, cls=jsonapi.MyDecoder)

print(j_c1)
print(un_j_c1)
