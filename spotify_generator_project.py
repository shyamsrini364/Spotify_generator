
import requests
import json
uris=[]

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token ='BQAM_a_ykoGPZ406JkK_GizBu7Oo4jafYAPnQ83kCp8ZgJKV-hGKkRBdwL4PrAfsm4-nfKgYJK1nignvZnz-_uzpy-cGJKAwNNugucMWq5lZ0Ab-XHV5KyXg6W4Wa51YjaOlL3Dvd7JIXKIz56DqRqo2nLMg-GQT19LYUXl_32_Ksl73nRXn211nh8_6DqU_gQezQzncLA'

#FILTERS
limit=10 #number of songs
market = "AU" # country
seed_genres= "pop" #genres
target_danceability=0.2
seed_artists="7qjJw7ZM2ekDSahLXPjIlN,2ae6PxICSOZHvjqiCcgon8"
#QUERY FOR SONGS
query = f'{endpoint_url}={limit}&market={market}&seed_artists={seed_artists}&target_danceability={target_danceability}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

#create an array to store playlist
json_response = response.json()
print('Recommended songs:')
for i,j in enumerate(json_response['tracks']):
    uris.append(j['uri'])
    print(f"{i+1} \"{j['name']}\" by {j['artists'][0]['name']}")

print(response)




#create new playlist
user_id=12139472960
endpoint_url=f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body=json.dumps({"name":"Sid Sriram's voice is crazy goo"
                         ,"description": "finally getting this generator done",
                         "public":False})
response=requests.post(url=endpoint_url,data=request_body,headers={"Content-type":"application/json"
                         ,"Authorization":f"Bearer {access_token}"})
url=response.json()['external_urls']['spotify']
print(response.status_code)

#fill the new playlist with reccomendations
playlist_id=response.json()['id']
endpoint_url= f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body=json.dumps({
    "uris" : uris
    })

response = requests.post(url=endpoint_url,data=request_body,headers={"Content-type":"application/json"
                    ,"Authorization":f"Bearer {access_token}"})
#print(response.status_code)
