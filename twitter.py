
from requests_oauthlib import OAuth1Session
import sys, os, json, argparse
import os
import json
import time
import random

class Twitter:

    def __init__(self, consumer_key, consumer_secret, proxy):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.proxy = proxy
        self.listAccounts = []
        self.sessions = []

    @staticmethod
    def check_api(consumer_key, client_secret, proxy):
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        oauth = OAuth1Session(consumer_key, client_secret)
        oauth.proxies = {
            'http': proxy,
            'https': proxy
        }

        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
            return True
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )
            return False

    def get_authorize_url(self, proxy):
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"

        oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret)  
        oauth.proxies = {
            'http': proxy,
            'https': proxy
        } 

        try:
            fetch_response = oauth.fetch_request_token(request_token_url) # try with proxies here
        except ValueError:
            print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        self.resource_owner_key = fetch_response.get("oauth_token")
        self.resource_owner_secret = fetch_response.get("oauth_token_secret")
        
        # Get authorization
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)
        return authorization_url

    def link_account(self, verifier, proxy):

        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.resource_owner_key,
            resource_owner_secret=self.resource_owner_secret,
            verifier=verifier,
        )
        
        oauth_tokens = oauth.fetch_access_token(access_token_url)
        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]
        
        # Make the request
        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )
        
        oauth.proxies = {
            'http': proxy,
            'https': proxy
        }

        response = oauth.get("https://api.twitter.com/2/users/me", params={"user.fields": "created_at,description,username"})
        
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )
        
        json_response = response.json()

        self.listAccounts.append({"account": json_response['data']['username'], "oauth": oauth})
        
        info_to_serialize = {
            'resource_owner_key': access_token,
            'resource_owner_secret': access_token_secret,
            'proxy': proxy
        }

        self.sessions.append(info_to_serialize)

    def export_sessions(self):
        ofile = open(f'{self.consumer_key}.json', 'w')
        sessions_final = json.dumps(self.sessions)
        ofile.write(sessions_final)
        print(f"Updated {self.consumer_key}.json")
    
    def import_sessions(self, fileName):
        
        with open(fileName, 'r') as j:
            sessions = json.loads(j.read())

        for session in sessions:
            oauth = OAuth1Session(
                self.consumer_key,
                client_secret=self.consumer_secret,
                resource_owner_key=session['resource_owner_key'],
                resource_owner_secret=session['resource_owner_secret'],
            )

            oauth.proxies = {
                'http': session['proxy'],
                'https': session['proxy']
            }
            response = oauth.get("https://api.twitter.com/2/users/me", params={"user.fields": "created_at,description,username"})
        
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(response.status_code, response.text)
                )
        
            json_response = response.json()
            
            self.listAccounts.append({"account": json_response['data']['username'], "oauth": oauth})
    
    def follow(self, names, username):

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['account'] == name:
                   accounts_to_use.append(account) 
                  
        for account in accounts_to_use:
            # Making the request
            account = account["oauth"]
            token = account.token["oauth_token"]
            response = account.get(f"https://api.twitter.com/2/users/by?usernames={username}")
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(response.status_code, response.text)
                )
            data = json.loads(response.text)
            payload = {"target_user_id": data['data'][0]['id']}
            
            id = token[0:19]
            response = account.post(
                "https://api.twitter.com/2/users/{}/following".format(id), json=payload
                )

            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(response.status_code, response.text)
                )

    def tweet(self, names, text):
    
        payload = {"text": text}

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['account'] == name:
                   accounts_to_use.append(account) 

        for account in accounts_to_use:
            account = account["oauth"]
            response = account.post(
                "https://api.twitter.com/2/tweets",
                json=payload
            )
            if response.status_code != 201:
                raise Exception(
                    "Request returned an error: {} {}".format(response.status_code, response.text)
                )

    def retweet(self, names, link, pause):

        tweetid = ""
        for c in link:
            if c.isdigit():
                tweetid = tweetid + c
        print("Tweet ID: " + tweetid) 
        payload = {"tweet_id": tweetid}

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['account'] == name:
                   accounts_to_use.append(account) 
        
        for account in accounts_to_use:
            
            account = account["oauth"]
            token = account.token["oauth_token"]
            id = token[0:19]
            response = account.post(
                "https://api.twitter.com/2/users/{}/retweets".format(id), json=payload
            )
            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(response.status_code, response.text)
                )
            if pause:
                time.sleep(random.randint(1, 60))

    def like(self, names, link):

        tweetid = ""
        for c in link:
            if c.isdigit():
                tweetid = tweetid + c
        print("Tweet ID: " + tweetid) 

        payload = {"tweet_id": tweetid}

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['account'] == name:
                   accounts_to_use.append(account) 
        

        for account in accounts_to_use:
            # Making the request
            account = account["oauth"]
            token = account.token["oauth_token"]
            id = token[0:19]
            response = account.post(
                "https://api.twitter.com/2/users/{}/likes".format(id), json=payload
                )

            if response.status_code != 200:
                raise Exception(
                    "Request returned an error: {} {}".format(response.status_code, response.text)
                )
    
    def delete(self, names):
        for name in names:
            for account in self.listAccounts:
                if account['account'] == name:
                   self.listAccounts.remove(account)