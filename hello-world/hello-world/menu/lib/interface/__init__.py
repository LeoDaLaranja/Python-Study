def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '~' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[032mSua Opção: \033[m')
    return opc


#Primeira 

db.companies.find({"$expr": {
            "$gt":["$number_of_employees","$founded_year"]



}




db.listingsAndReviews.find( {"property_type":{"$eq":"House"},"amenities": {
                                  "$all": [ "Changing table" ]
                                         }}


).count()

{"amenities": {"$all":["Free parking on premises","Wifi"."Air conditioning"]}, "bedrooms": {"$gte":2}} 

db.trips.find({"start station location.coordinates.0" : -74}).count()
db.inspections.find({"address.city":"NEW YORK"}).count()

db.listingAndReviews.find(
    {"amenities" : "Wifi"},
    {"price":1,"address":1, "_id":0}
).pretty()


db.listingAndReviews.aggregate([
    {$match : {"amenities": "Wifi"}},
    {$project : {"price": 1, "address": 1, "_id": 0}}
])

db.listingsAndReviews.aggregate([
    {$project : {"room_type": 1, "_id":0}},
    {$group: {"_id":"$room_type"}}

])
db.listingsAndReviews.findOne({},{"room_type":1,"_id":0})

db.companies.find({"founded year":{"$ne" : null}},{"name":1,"founded_year":1}.sort({"founded_year":1}).limit(5)

db.trips.find({"birth year":{"$ne": ""}},
            {"birth year": 1, "_id": 0}
).sort({"birth year":-1}).limit(1)

db.collection.updateOne({<query to locate>},{<update>})
db.collection.updateOne({<query>},{<update>},{"upsert":true})
db.iot.updateOne({ "sensor": r.sensor, "date": r.date,
                   "valcount": { "$lt": 48 } },
                         { "$push": { "readings": { "v": r.value, "t": r.time } },
                        "$inc": { "valcount": 1, "total": r.value } },
                 { "upsert": true })