# ./app.py

from flask import Flask, request, render_template, g
import json
import requests

app = Flask(__name__)
app.config.from_object('config')

api_token = app.config["API_TOKEN"]

api_url_base = app.config["API_URL_BASE"]
api_by_popularity = app.config["API_BY_POPULARITY"]


def get_popular_movies():

    response = requests.get(api_by_popularity)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


get_popular_movies = get_popular_movies()


def get_movie_array():
    movie_list = []
    if get_popular_movies is not None:
        print("here's your info: ")
        for results in get_popular_movies['results']:
            for movie in results.items():
                movie_list.append(movie)
        print(movie_list)
        return movie_list

    else:
        print('[!] Request failed')


get_movie_array = get_movie_array()


@app.route("/", methods=["GET"])
def home():
    if request.form:
        print(request.form)
    return render_template('home.html',
                           get_popular_movies=get_popular_movies,
                           get_movie_array=get_movie_array,
                           )


if __name__ == "__main__":
    app.run(debug=True)
