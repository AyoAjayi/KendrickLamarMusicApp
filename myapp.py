import flask
import os
import requests
import json
import random
import requests_oauthlib, requests


app = flask.Flask(__name__)
    
@app.route('/') 
def artist_info(): 
    url = "https://api.genius.com/search?q=Kendrick%20Lamar"
    genius_key = os.getenv("GeniusKey")
    my_headers = {
        "Authorization": "Bearer  " + genius_key
    }
    response = requests.get(url, headers=my_headers)
    json_body = response.json() 
    
    array = json_body["response"]["hits"]
    r = random.randint(0, len(array) - 1) 
    
    #This gets the id of the song that's playing
    song_id = array[r]["result"]["id"]
    song_link = get_songPlaying(song_id)
  
    
    image_url = array[r]["result"]["song_art_image_url"]
    return flask.render_template("index.html", artist = array[r]["result"]["primary_artist"]["name"], song = array[r]["result"]["title"], photo = image_url, tweet = twitter_quotes(), video = song_link)
   
   
def twitter_quotes():
    twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=KendrickLamar&count=10"
    twitter_key = os.getenv("TwitterKey")
    twitter_secret_key = os.getenv("SecretKey")
    twitter_token = os.getenv("Token")
    twitter_secret_token = os.getenv("SecretToken")
    
    
    oauth = requests_oauthlib.OAuth1(
        twitter_key,
        twitter_secret_key,
        twitter_token,
        twitter_secret_token
     )
    
    response = requests.get(twitter_url, auth=oauth)
    json_body = response.json()
    array = json_body['statuses']
    
    num = random.randint(0, len(array) - 1)
    different_tweets =  array[num]["text"]
    return different_tweets
   
    
def get_songPlaying(song_id):
    song_id_url= "https://api.genius.com/songs/" + str(song_id)
    song_id_genius_key = os.getenv("SongIDKey")
    song_id_headers = {
            "Authorization": "Bearer  " + song_id_genius_key
    }
    response2 = requests.get(song_id_url, headers=song_id_headers)
    json_body2 = response2.json()
    
   
    song_link = json_body2["response"]["song"]["apple_music_player_url"]
    return song_link


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)

