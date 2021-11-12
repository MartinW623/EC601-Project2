# EC601-Project2
### Product Mission：

This product is designed to help users easily obtain information on public platforms such as Twitter and perform sentiment analysis on the content of Twitter texts.

### User stories：

As a social science researcher, I want to study the emotions expressed by the messages sent by the public on public platforms.

As a parent, I want to judge whether my children who have just entered elementary school will be exposed to electronic devices and social media in advance will be badly affected and induced.

As a politician, I hope to know what the public is most concerned about and what the mainstream views of different politicians and events are.

As a company's decision-maker, I hope that after our company launches a new product, we can get the most authentic user experience from the public.

As a content creator, I need to know the most popular elements at the moment, and to understand people’s views on different popular elements.

### MVP

Users can obtain information on the public social media Twitter, and perform sentiment analysis.


## Assignment
### Introduction
This is the second project of EC601. I will use Twitter API and Google NLP API to obtain data form Twitter and analyze its sentiment.

I choose tweepy to finish the twitter analysis tool.

This project includes testing files and result file.  
The Twitter testing file is the function to download your home timeline tweets and print each one of their texts to the console.  
The Google NLP testing file is the function to analyze the sentiment of every sentences of the input file.   
The result files are the results of the printed home timeline tweets and printed sentiment results.  

### Getting Start
#### Setting up Twitter API authentication
- Create your own key and access token
```
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
```
#### Installing the client library
- Setting up a python development environment first- [python environment](https://cloud.google.com/python/docs/setup "The tutorial to set up")    
- Then install the library `pip install --upgrade google-cloud-language`
#### Setting up authentication
- Create new account and select a project
- Create a service account key and a JSON key file will be downloaded to your computer
- Provide authentication credentials to your application code by setting the environment variable`GOOGLE_APPLICATION_CREDENTIALS`
  - Replace ***`KEY_PATH`*** with the path of the JSON file that contains your service account key.
  -  `export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"`
### Run the program
```
python Home_timeline_twitters.py
python Google_NPL.py Home_timeline_tweets_results.txt
```
### Get the results
```
This tweet is used to test Twitter API.
这条推用来测试Twitter API平台。
...
```
```
Sentence 0 has a sentiment score of -0.10000000149011612
Sentence 1 has a sentiment score of 0.20000000298023224
...
```
## Project3-Unit test
- I write a unit testing program `Unit_test.py` to test whether `Google_NLP.py` could get the right result.  
- First, import the module **` unittest `** which I choose to use.  
- Then the function `"asserEqual"` is used to compare if the `"print_result"` function could get the right result.  
- I also used **`time`** module to get the running time of every unit of **`unittest`**, which is aimed to illustarte how to implemet time testing function.


## Reference
Tweepy: <https://docs.tweepy.org/en/stable/getting_started.html>  
Google NLP: <https://cloud.google.com/natural-language/docs/reference/libraries#cloud-console>  
Unittest: <https://docs.python.org/3/library/unittest.html>
