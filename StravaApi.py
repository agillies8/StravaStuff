"""
Instuctions to setup Strava API:
1) Get authorization code from authorization page. This is a one time, manual step. 
Paste the below code in a browser, hit enter then grab the "code" part from the resulting url. 

https://www.strava.com/oauth/authorize?client_id=XXXXXXXXXXX&redirect_uri=http://localhost&response_type=code&scope=activity:read_all

2) Exchange authorization code for access token & refresh token

https://www.strava.com/oauth/token?client_id=XXXXXXXXX&client_secret=XXXXXXXXXXXXXXXXX&code=XXXXXXXXXXXXXXXXXXX&grant_type=authorization_code

3) View your activities using the access token just received

https://www.strava.com/api/v3/athlete/activities?access_token=access_token_from_previous_step

3) Use refresh token to get new access tokens

https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&refresh_token=your_refresh_token_from_previous_step&grant_type=refresh_token

4) store credentials in a dotenv file
"""

def getDataset():

    from dotenv import load_dotenv
    import requests
    import urllib3
    import os
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    load_dotenv()

    #need to have keys in .env file, get using instructions above

    auth_url = "https://www.strava.com/oauth/token"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"

    payload = {
        'client_id': os.getenv("CLIENT_ID"),
        'client_secret': os.getenv("CLIENT_SECRET"),
        'refresh_token': os.getenv("REFRESH_TOKEN"),
        'grant_type': "refresh_token",
        'f': 'json'
    }

    #print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    #print("Access Token = {}\n".format(access_token))

    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 200, 'page': 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json() #to get all activities in the account

    #print(my_dataset[0]["name"]) #to test output
    #print(my_dataset[0]["map"]["summary_polyline"]) #to test output
    return my_dataset

getDataset()