import json
import pickle
import yaml


#  we can use to perform serialization and desirialization
# serialization: converting python objects like dict, lists into json format / string represention ( dump / dumps )
# deserialization: converting json string to into python objects like dict (load / loads )
# dump and dumps
candidate_details = {"name": "msn", "course": "python", "place": "bangalore"}
# data = json.dumps(candidate_details, indent=4)
# print(data)
# # write into a file we can use dump
# with open("file1.json", "w") as jw:
#     json.dump(data, jw, indent=4)
#
# ddata = json.loads(data)
# print(ddata)
#
# with open('file1.json', 'r') as rj:
#     rdata = json.load(rj)
# print(rdata)

"""
pickle we can use to perform serialization and desirialzation
we can use byte streams, load, loads , dump, dumps
.pkl

"""

with open("file1.pkl", 'wb') as pk:
    pickle.dump(candidate_details, pk)

with open("file1.pkl", "rb") as rk:
    data = pickle.load(rk)

print(data)

with open('file1.yaml', 'r') as ry:
    data = yaml.safe_load(ry)
print(data)