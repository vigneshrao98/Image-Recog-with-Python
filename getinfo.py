from clarifai.rest import ClarifaiApp
import json

app=ClarifaiApp()
model=app.models.get('general-v1.3')
def get_pred(img_path):
    response = model.predict_by_filename(filename=img_path)
    data=json.load(response)
    result=data['outputs']['0']['data']['concepts']['0']['name']
    return result
