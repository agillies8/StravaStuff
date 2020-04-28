
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
Instructions for deploy to heroku:
To create virtual env:

1. create root folder for website, above 'demo'
2. navigate to this folder
3. open a terminal at this level (make sure terminal is in (base))
4. enter command "python -m venv virtual" to install the virutal python env
5. to install specific modules, you need to install to virtual env: eg "virtual\Scripts\pip install flask"
6. Make sure application is running by starting the virtual python evn "virtual\Scripts\python Demo\mainfile.py"
7. the website should now function as expected

Create heroku app from 'Demo' folder:
get to demo folder
-enter "heroku login"
-enter credentials
-enter heroku create andrewsactive

then need 3 files in the 'demo' folder:
install gunicorn: "..\virtual\Scripts\pip install gunicorn"
-requirements.txt first, run ..\virtual\Scripts\pip freeze > requirements.txt
-then create Procfile (no extension) Put this in it: "web: gunicorn app4:app" where app4 is the filename of the main python script
-then create runtime.txt file with python version to run in it.

Then create a git repo for it:
from Demo folder, run 'git init'
then run git add .
then run git commit -m "first commit"
-point git to herku specific app: heroku git:remote --app andrewsactive
push to heroku: git push heroku master
