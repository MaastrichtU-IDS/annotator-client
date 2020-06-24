from annotator_client.services.mongodb_service import db

class Annotation(db.DynamicDocument):
    test_field = db.StringField(required=False, unique=True)