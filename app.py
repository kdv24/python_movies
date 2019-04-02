# ./app.py

from flask import Flask, request, render_template, g
import json
import requests

app = Flask(__name__)
app.config.from_object('config')

api_token = app.config["API_TOKEN"]
headers = {'Content-Type': 'appliation/json',
'Authorization': 'Bearer {0} '.format(api_token)}

api_url_base = app.config["API_URL_BASE"]
full_api = app.config["API_FULL_URL"]
api_by_id = app.config["API_BY_ID"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template('home.html', api_by_id=api_by_id, favicon='https://www.themoviedb.org/assets/2/v4/logos/primary-green-d70eebe18a5eb5b166d5c1ef0796715b8d1a2cbc698f96d311d62f894ae87085.svg')


if __name__ == "__main__":
    app.run(debug=True)

def get_movies():

    api_url = 'https://api.themoviedb.org/3/movie/popular?api_key=d8dd03066197e6525f02d3aba1ebe366'

    response = requests.get(full_api, headers=headers)

    if response.status_code == 200:
        print(response)
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

        
get_movies = get_movies()

if get_movies is not None:
     print("here's your info: ")
     for k, v in get_movies['results'][0].items():
        if k == 'title':
            print(f'The title of the movie is: "{v}".')
        if k == 'release_date':
            print(f'The release date for the movie is: "{v}".')
#   TO DO: find out what "popularity means"          
        if k == 'popularity':
            print(f'This movie is number "{v}" on the list of the current most popular movies.')
# all the movies and key/values:
        # print('{0}:{1}'.format(k, v))

else:
    print('[!] Request failed')   