import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newdb"]
mycol = mydb["newc"]

# mydict = { "username": "user2", "password": "22222222" }
# myquery = { "username": "user2" }

# mycol.delete_one(myquery)
# x = mycol.insert_one(mydict)
# print(x.inserted_id)
for x in mycol.find():
  print(x)