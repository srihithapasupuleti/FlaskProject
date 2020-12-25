from app import app
import flask
from flask import Flask,request, jsonify
from flask import render_template
import tweepy
import pyodbc


app = Flask(__name__)

consumer_key = 'N3bdxtz74myZn366YVb639SWl'
consumer_secret = 'UO5UQIegQKyiJP5P3KJLPkqmMypgLYm49UqHrBYh6Slk17S9c8'
access_token = '1272328408677179392-ZOT9wRAhsIBpXF3tn3cGrr25dceQGq'
access_token_secret = 'Ako66yF7B0zke093jagnEWyYcrvwIIkQYNqnlVyvHhHix'


def fndataconnecttwitter(tmp):
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-5OJ0R1H\SQLEXPRESS;'
                      'Database=twitter;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM twitter.dbo.Table_1')
    
    for row in cursor:
        print(row)


    cursor = conn.cursor()
    cursor.execute('INSERT INTO dbo.Table_1 VALUES (?)', (tmp) )
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into twitter table")
    cursor.close()


def OAuth():
	try:
		auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
		auth.set_access_token(access_token,access_token_secret)
		return auth
	except Exception as e:
		return None


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    oauth = OAuth()

    api = tweepy.API(oauth)
    # api.update_status("srihitha")
    public_tweets=get_tweets("srihithapasupu1")
    return render_template('home.html')


# Function to extract tweets 



def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_token , access_token_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
        tmp=[]  
  
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            tmp.append(j)  
        
        fndataconnecttwitter(tmp[0])
        print(tmp) 

       
        
@app.route('/posts')

def get_tweets1():
        username = "srihithapasupu1"
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
        # Access to user's access key and access secret
        auth.set_access_token(access_token , access_token_secret) 
        # Calling api
        api = tweepy.API(auth) 
        tweets = api.user_timeline(screen_name=username)
        tmp=[]  
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv: 
            tmp.append(j)
        search = request.args.get('q')
        public_tweets = api.user_timeline(search)
        return render_template('posts.html',tweets=public_tweets)



if __name__ == "__main__":
    app.run()
    
  
  

