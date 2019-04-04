# ./app.py

from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

# allows grabbing env variables saved in config file
app.config.from_object('config')
api_url_base = app.config["API_URL_BASE"]
api_by_popularity = app.config["API_BY_POPULARITY"]


def get_popular_movies():

    response = requests.get(api_by_popularity)

    if response.status_code == 200:
        movies = json.loads(response.content.decode('utf-8'))
        movies = movies['results']
        return movies

    else:
        return None


def get_movie_array():
    popular_movies = get_popular_movies()
    movie_list = []

    if popular_movies is not None:
        for movie in popular_movies:
            movie_list.append(
                {'title': movie['title'], "release_date": movie['release_date'], "popularity": movie['popularity']})

    else:
        print('[!] Request failed')
    return (movie_list)


@app.route("/", methods=["GET"])
def home():
    movie_array = get_movie_array()
    return render_template('home.html', movie_array=movie_array)


if __name__ == "__main__":
    app.run(debug=True)
