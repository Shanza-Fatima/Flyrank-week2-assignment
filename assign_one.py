from fastapi import FastAPI
app = FastAPI()

tasks = [{'id': 1,
          'title': 'presentation',
          'done': True},{'id': 2,
          'title': 'cloud assignment',
          'done': False},{
          'id': 3,
          'title': 'floaral work',
          'done': True}]
@app.get('/tasks/{id}')

#successfully implemented the first endpoints
@app.get('/')
def return_json():
    return {'name': "TaskAPI",
            'version': '1.0',
            'endpoints': ['/tasks']}
@app.get('/health')
def check():
    return {'status': "OK"}