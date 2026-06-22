"""
Exercice 31.1 : API Todo List avec FastAPI
Crée une API REST pour gérer des tâches.

Modèle Todo :
- id: int (auto)
- title: str
- description: str (optionnel)
- completed: bool = False
- created_at: datetime

Endpoints :
- GET /todos : liste toutes les tâches
- GET /todos/{id} : une tâche par id
- POST /todos : crée une tâche
- PUT /todos/{id} : met à jour une tâche
- DELETE /todos/{id} : supprime une tâche
- GET /todos?completed=true : filtre par statut

Exécution : uvicorn api_todo:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# À compléter
app = FastAPI(title="Todo API", version="1.0.0")

class TodoCreate(BaseModel):
    pass

class Todo(TodoCreate):
    pass

# Endpoints à implémenter

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
