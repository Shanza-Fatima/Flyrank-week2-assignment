from fastapi import FastAPI, HTTPException
app = FastAPI()

tasks = [{"id": 1,
          'title': 'presentation',
          'done': True},{'id' : 2,
          'title': 'cloud assignment',
          'done': False},{
          'id' : 3,
          'title': 'floaral work',
          'done': True}]
@app.get('/tasks/{id}')
def get_tasks(id: int):
    for task in tasks:
        if task['id'] == id:
            return task
       
    raise HTTPException(status_code=404, detail={'error': f"Task{id} not found"})
#successfully given the expected results    

#successfully implemented the first endpoints
@app.get('/')
def return_json():
    return {'name': "TaskAPI",
            'version': '1.0',
            'endpoints': ['/tasks']}
@app.get('/health')
def check():
    return {'status': "OK"}