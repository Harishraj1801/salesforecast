import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["newdb"]
mycol = mydb["newc"]

mydict = { "username": "harishraj@gmail.com", "password": "Harish@123" }

x = mycol.insert_one(mydict)
print("success")