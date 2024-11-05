from fastapi import FastAPI
import sqlite3
#delete venv (yellow) command shift p (select intepreter)
app = FastAPI()
#pip install fastapi requests
@app.get('/root')
def get_tasks():
    with sqlite3.connect("./todos.db") as conn:
        query = conn.execute("SELECT FROM todos;)")
        result = query.fetchall

        response = []
        for todo in result:
            todo_json = {
                'id': todo[0],
                'todo': todo[1]
            }
            response.append(todo_json)
        return response
#pip install uvicorn
#uvicorn main:app --reload
#reload = restart servers everytime there is a change in the code (good for testing)


