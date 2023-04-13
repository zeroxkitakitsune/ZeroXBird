# ZeroXBird
A tool to manage bird accounts

> **this app is still in development**

## Usage
1. Install requirements:
```
$ pip install -r requirements.txt
```
2. Build executable file
```
$ python -m PyInstaller --onefile -w main.py
```
3. Locate the file in `/dist` folder and run it
4. Add API and link an account 
## Features
- This app works only with official Bird API. You can apply for one on Twitter's Developer Porttal.
- There are two types of APIs: free and paid one. 
    - With free subscription you can only tweet from the app
    - With paid one you can pretty much do anything:
        - Tweet
        - Follow
        - Retweet
        - Like tweets 
- This app works with proxy for API connection and accounts autorization
- This app also stores your sessions for specific API authorized in a `<API_consumer_key>.json` file
- This app allows you simply import your sessions once you add API in the app

