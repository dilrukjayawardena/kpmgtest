from google.cloud import firestore
import json 

def data_store(request):
    try:
        db = get_db()
        request_json=None
        content_type = request.headers['content-type']
        print(content_type)
        if content_type == 'application/json':
            request_json = request.get_json()
        if content_type == 'text/plain':
            print(request.data)
            request_json = json.loads(request.data)
        if request_json and 'model' in request_json:
            stored_data=save_data(db,'gptdata',request_json)
            print(stored_data.id)
            data={"id":stored_data.id,"timestamp":stored_data.to_dict()['timestamp']}
            return json.dumps(data,default=str),200
        else:
            return "required body with model attribute"
    except Exception as e:
        error_str='Error: {}'.format(str(e))
        print(error_str)
        return error_str,500

def get_db(project_id=None):
    if project_id is not None:
        db = firestore.Client(project='my-project-id')
        return db
    else:
        db = firestore.Client()
        return db

def save_data(db,collection,data):
    new_data_ref = db.collection(collection).document()
    new_data_ref.set(data)
    new_data_ref.update({
        'timestamp': firestore.SERVER_TIMESTAMP
    })

    doc = new_data_ref.get()
    return doc