import pymongo

def db():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017/").films
    except Exception as e:
        print(f"ERROR BBDD: {e}")