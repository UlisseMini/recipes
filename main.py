import json
import os
import os.path as path

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/r/{recipe}')
def recipe(recipe: str):
    "Read a recipe file"
    try:
        return json.load(open(path.join('./recipes', recipe + '.json')))
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Recipe not found")

@app.get('/recipes')
def recipes():
    "Return list of recipes"
    return [x[:-5] for x in filter(lambda x: x.endswith('.json'), os.listdir('./recipes'))]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
