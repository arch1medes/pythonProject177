from flask import request
from flask_restx import Resource

from models import db, Genre, GenreSchema
from app import api

genres_ns = api.namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenreAdd(Resource):

    def get(self):
        dirs = Genre.query.all()
        return genres_schema.dump(dirs), 200

    def post(self):
        data = request.json
        print(data)
        genre = Genre(
            name=data.get("name"),
            )
        db.session.add(genre)
        db.session.commit()
        return "", 201


@genres_ns.route('/<int:uid>/')
class GenreView(Resource):

    def get(self, uid):
        genre = Genre.query.get(uid)
        if not genre:
            return "", 404
        return genre_schema.dump(genre), 200

    def put(self, uid):
        genre = Genre.query.get(uid)
        if not genre:
            return "Not found", 404
        data = request.json
        genre.name = data.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, uid):
        genre = Genre.query.get(uid)
        if not genre:
            return "Not found", 404
        db.session.delete(genre)
        db.session.commit()
        return "", 204