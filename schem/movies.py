from flask import request
from flask_restx import Resource

from models import db, Movie, MovieSchema
from app import api

movies_ns = api.namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        """
        Get movies list. Max results per page == 10.
        If 'page' arg is present, it'll offset accordingly.
        'director_id' and/or 'genre_id' args output movies by the director, in the genre, or both
        """
        d_id = request.args.get('director_id')
        g_id = request.args.get('genre_id')
        page = request.args.get('page')
        if page is not None:
            offset = 10 * (int(page)-1)
        else:
            offset = 0
        if d_id is not None and g_id is not None:
            all_movies = Movie.query.filter(Movie.director_id == d_id, Movie.genre_id == g_id).all()
        elif d_id is not None:
            all_movies = Movie.query.filter(Movie.director_id == d_id).all()
        elif g_id is not None:
            all_movies = Movie.query.filter(Movie.genre_id == g_id).all()
        else:
            all_movies = Movie.query.limit(10).offset(offset).all()
        return movies_schema.dump(all_movies)


@movies_ns.route('/<int:uid>/')
class MovieView(Resource):

    def get(self, uid):
        movie = Movie.query.get(uid)
        if not movie:
            return "", 404
        return movie_schema.dump(movie)