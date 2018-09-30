### `players` collection:

玩家collection:每个玩家都是一个document，里面包含了玩家的姓名，最大携带装备数，幸运值，工作力。每个document还嵌入了穿着装备及储物箱中装备两个array。每个装备有 ID， 类型，和metadata三个fields，metadata表示装备的数值，不同类型的装备的数值有着不同的含义

Format:
```scala
newPlayer1 = { "name": "player1",
            "maxItem": 4,
            "luck": 5,
            "gold": 5,
            "productivity": 4
            "wearingItems": [{"ID": 101, "type": "tool" , "metadata": 18},
                {"ID": 102, "type": "weapon", "metadata": 20}],
            "chestItems": [{"ID": 103, "type": "tool" , "metadata": 8}]}
```

Related Method:

```scala
创建新玩家，首先检测重名，若无重名，则根据一定规则初始化玩家属性，将玩家加入数据库
def createNewPlayer(name) {
    // check duplicate name
    if (players.find_one({"name": name}, {field: ... }) != None) {
        // report error
    }
    new newPlayer(name)
    players.insert_one(newPlayer)
}

在数据库中通过ID读取玩家信息并返回
def readPlayerInfo(ID, field(optional) ) {
    return players.find_one({"_id": ID}, {field: ... })
}

穿上装备：首先检查是否超过携带数量，若没有超过，则查找装备，取出装备，并穿上装备，同时修改玩家属性
def equipItem(playerID, itemID ) {
    checkItemNumber()
    // find the item.
    item = players.find_one({"ID": "playerID"}, {"chestItems": {"$elemMatch": {"ID" : itemID}}})['chestItems'][0]
    // move the item.
    players.update_one({"ID": "playerID" }, { "$pull": { "chestItems": {"ID" : itemID} }, "$push": { "wearingItems" : item } })
    updatePlayer(item)
}

取下装备：查找装备，取出装备，修改属性
def takeOffItem() {
    // find the item.
    item = players.find_one({"ID": "playerID"}, {"wearingItems": {"$elemMatch": {"ID" : itemID}}})["wearingItems"][0]
    // move the item.
    players.update_one({"ID": "playerID" }, { "$pull": { "wearingItems": {"ID" : itemID} }, "$push": { "chestItems" : item } })
    updatePlayer(item)
}


```


### `market` collection


Format:
```scala

```



### `itemPool` collection