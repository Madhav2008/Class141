from flask import Flask, json, jsonify, request
import csv

allMovies = []

file = open('movies.csv', encoding='utf-8')
reader = csv.reader(file)

data = list(reader)
allMovies = data[1:]

likedMovies = []
dislikedMovies = []
notWatchedMovies = []

app = Flask(__name__)

@app.route('/get-movie')
def get_movie():
    return jsonify({
        'data' : allMovies[0],
        'status' : 'Success',
    })

@app.route('/liked-movie', methods=['POST'])
def liked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        'status' : 'Success'
    }),201

@app.route('/dislike-movie', methods=['POST'])
def disliked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    dislikedMovies.append(movie)
    return jsonify({
        'status' : 'Success'
    }),201

@app.route('/not-watched-movie', methods=['POST'])
def not_watched_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    notWatchedMovies.append(movie)
    return jsonify({
        'status' : 'Success'
    }),201

if __name__ == '__main__':
    app.run()