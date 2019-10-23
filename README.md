
### Kendrick Lamar's music web app created by Ayomide Ajayi
 
This web app is dedicated to Kendrick Lamar. It allows users see his songs, view what people are saying about him on twitter (using the Twitter API), and actually listen to short snippets of his music(using the Genius API). My web page is dynmaic meaning that everytime the web page is refreshed, a new song and tweet are generated for the user to listen to and look at. 

### Built With:

- Python
-	Flask
-	Add-on libraries (os, requests, json, requests_oauthlib)
-	Deployed via [Heroku](https://afternoon-everglades-32362.herokuapp.com/)



### Kendrick Lamar:

I used the twitter API to generate real time tweets on Kendrick Lamar. I searched for his songs using his artist_id.


### Known Problems:

I do not have any known problems regarding the functionalities of this project yet. I will document in this section when I find any issues.
However, I had some issues while working on the project that I fixed later. Some are,

* I struggled with parsing the json data intially. I solved this by looking at genius to see the way the response would be formatted.

* I struggled with getting my app running with heroku initially. However, I realized that I need to update my requirements.txt file. After deploying the app on Heroku, I hid my API keys by using config vars on Heroku.  

### Further Improvements:

* I wish I could find a way to block out the profanity in the tweets in order to improve my project.
* Styling my web page would have made it appealin








# 1) 
The theme I chose for this project is Kendrick Lamar. This web app gave me an opportunity to let users see Kendrick Lamar's songs, view what people are saying about him, and actually listen to short snippets of his music.

# 2) 
For the genius api, I queried kendrick Lamar in the api url to search for his songs, images, and link to his genius page. I did the same for the twitter api. I specifically queried Kendrick Lamar's name to generate random tweets about him.

# 3) 
I struggled with parsing the json data intially. I solved this by looking at genius to see the way the rrsponse would be formatted.
#
I also struggled with the idea of making my webpage dynamic. Once I understood the structure of the json data, then I saw a way to use random to randomly get the information I needed.
# 
It took me a while to get my config vars set up, I reviewed the slides for more clariification.

# 4) 
I think my css code could be more concise. I referenced w3schools so a lot of the design was trial and error for me.
# 5) 
