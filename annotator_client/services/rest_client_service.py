import json

import requests

from annotator_client.models.annotation import Annotation


def fetch_annotations(group_id):
    query_result = requests.get("https://hypothes.is/api/search?group=%s" % group_id,
                                headers={'Authorization': 'Bearer 6879-od_O0wgcODj1SEiDYqVKryvaqQDcVKsRWVXCJwTCdhY'})
    annotations = query_result.json()['rows']
    for annotation in annotations:
        annotation_id = annotation['id']
        annotation['hypothesis_id'] = annotation_id
        del annotation['id']
        Annotation(**annotation).save()
        # annotation_id = annotation['id']
        # annotation['hypothesis_id'] = annotation_id
        # del annotation['id']
        # annotation_json = json.loads(json.dumps(annotation))
        # print(str(annotation_json.user))
        # annotationEntity = Annotation()
        # annotationEntity.from_json(annotation)
        # Annotation(**annotation_json).save()
    # print(str(annotations))
        # Annotation(**annotation).save()

