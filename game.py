import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client['gameData']
db.drop_collection('players')

players = db['players']


# def createPlayer()
newPlayer1 = { "name": "player1",
                "maxItem": 4,
                "luck": 5,
                "gold": 5,
                "wearingItems": [{"ID": 101, "type": "tool" , "metadata": 18}, {"ID": 102, "type": "weapon", "metadata": 20}],
                "chestItems": [{"ID": 103, "type": "tool" , "metadata": 8}]}

newPlayer2 = {"name": "player2",
                "maxItem": 6,
                "luck": 7,
                "gold": 9,
                "wearingItems": [{"ID": 10, "type": "tool" , "metadata": 8}],
                "chestItems": [{"ID": 111, "type": "accessory" , "metadata": 18}, {"ID": 99, "type": "weapon", "metadata": 2}]
                }

players.insert_one(newPlayer1)   
players.insert_one(newPlayer2)
print(players.find_one({"name":"player2"}))
item = players.find_one({'name': 'player2'}, {"chestItems": {"$elemMatch": {"ID" : 99}}})['chestItems'][0]
players.update_one({"name": "player2" }, { "$pull": { "chestItems": {"ID" : 99} }, "$push": { "wearingItems" : item } })
