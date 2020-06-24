from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from annotator_client.models.annotation import Annotation


class AnnotationResource(Resource):
    method_decorators = [jwt_required]

    def put(self, annotation_id):
        body = request.get_json()
        Annotation.objects.get(id=annotation_id).update(**body)
        return '', 200

class AnnotationList(Resource):
    method_decorators = [jwt_required]

    def post(self):
        body = request.get_json()
        annotation = Annotation(**body).save()
        id = annotation.id
        return {'id': str(id)}, 200