from flask import request
from flask_restx import Resource

from models import db, Director, DirectorSchema
from app import api

directors_ns = api.namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@directors_ns.route('/')
class DirectorAdd(Resource):

    def get(self):
        dirs = Director.query.all()
        return directors_schema.dump(dirs), 200

    def post(self):
        data = request.json
        print(data)
        director = Director(
            name=data.get("name"),
        )
        db.session.add(director)
        db.session.commit()
        return "", 201


@directors_ns.route('/<int:uid>/')
class DirectorView(Resource):

    def get(self, uid):
        director = Director.query.get(uid)
        if not director:
            return "", 404
        return director_schema.dump(director), 200

    def put(self, uid):
        director = Director.query.get(uid)
        if not director:
            return "Not found", 404
        data = request.json
        director.name = data.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    def delete(self, uid):
        director = Director.query.get(uid)
        if not director:
            return "Not found", 404
        db.session.delete(director)
        db.session.commit()
        return "", 204