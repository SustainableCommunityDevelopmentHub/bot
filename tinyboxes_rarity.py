import pymongo
import requests


client = pymongo.MongoClient("localhost", 27017)
mydb = client["tinybox_attributes"]
myrec = mydb["minted_boxes"]


#test loop
#r=0
#for i in range(1,1000):
#    print("love i:" + str(i) +" r " + str(r) )

API_SUBURL = "https://api.opensea.io/api/v1/asset/0x46F9A4522666d2476a5F5Cd51ea3E0b5800E7f98/"

for i in range(1,1411):

        API_URL = API_SUBURL + str(i)
        NFTdata = requests.request("GET", API_URL)
        trait_scheme = NFTdata.json()['traits'][0]['value']
        trait_columns = NFTdata.json()['traits'][1]['value']
        trait_rows = NFTdata.json()['traits'][2]['value']
        trait_mirroring = NFTdata.json()['traits'][3]['value']
        trait_saturation = NFTdata.json()['traits'][4]['value']
        trait_shapes = NFTdata.json()['traits'][5]['value']
        trait_spread = NFTdata.json()['traits'][6]['value']
        trait_hue = NFTdata.json()['traits'][7]['value']
        trait_lightness = NFTdata.json()['traits'][8]['value']
        trait_animation = NFTdata.json()['traits'][9]['value']
        trait_shades = NFTdata.json()['traits'][10]['value']
        trait_hatching = NFTdata.json()['traits'][12]['value']
        trait_contrast = NFTdata.json()['traits'][16]['value']
        trait_phase = NFTdata.json()['traits'][17]['value']
        trait_rendered = NFTdata.json()['traits'][18]['value']

        mylist = [
                { "boxnum": i,
                "trait_scheme": trait_scheme,
                "trait_columns": trait_columns,
                "trait_rows": trait_rows ,
                "trait_mirroring": trait_mirroring ,
                "trait_saturation": trait_saturation ,
                "trait_shapes": trait_shapes ,
                "trait_spread": trait_spread ,
                "trait_hue": trait_hue ,
                "trait_lightness": trait_lightness ,
                "trait_animation": trait_animation ,
                "trait_shades": trait_shades ,
                "trait_hatching": trait_hatching ,
                "trait_contrast": trait_contrast ,
                "trait_phase": trait_phase ,
                "trait_rendered": trait_rendered }
                ]

        x = myrec.insert_many(mylist)
        # print list of the _id values of the inserted documents:
        print(x.inserted_ids)
~                               
