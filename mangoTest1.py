import pymongo

client=pymongo.MongoClient("mongodb+srv://nikhilabommareddy:NikhilaAshok@cluster0.lfzadum.mongodb.net/?retryWrites=true&w=majority")
db= client.test
print(db)

d={
     "name" : "Nikhila",
      "surname" : "Bommareddy",
     "email" : "nikhilaashokreddy@gmail.com"
}

d={
    "name":"Ashok",
    "Surname" : "Bommareddy"
    "Email" : "caashokreddy@gmail.com"
}

db1=client['mangoTest1']
coll= db1['test']
coll.insert_one(d)