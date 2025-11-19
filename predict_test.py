import requests
url = 'http://127.0.0.1:9696/predict'
client ={
       "customerid" :15719508,
        "surname" : "davis",
        "creditscore" :528,
        "geography" :  "france",
        "gender"     :  "male",
        "age"         :  31,
        "tenure"       : 6,
        "balance"       : 102016.72,
        "numofproducts"  :   2,
        "hascrcard"       :   "no",
        "isactivemember"   : "no",
        "estimatedsalary"   :  80181.12,
        "complain"            : "no",
        "satisfaction_score"   :  3,
        "card_type"  :  'gold',
        "point_earned"           : 264
}
Response = requests.post(url,json= client).json()
print(Response)

if Response['will_exit'] == True:
    print("Send promotional email to avoid Exit.")
else:
    print("Do not send the promotional email." )