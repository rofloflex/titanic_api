'''
Проверка работы API (/health)
curl -X GET http://127.0.0.1:5000/health
(cmd /c "curl -X GET http://127.0.0.1:5000/health")
curl -X GET http://127.0.0.1:5000/stats
curl -X POST http://127.0.0.1:5000/predict_model -H "Content-Type: application/json" -d "{\"Sex\": 0, \"Age\": 22.0, \"Fare\": 7.2500, \"Pclass\": 3}"
'''

from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Загрузка модели из файла pickle
with open ('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Счетчик запросов
request_count = 0

# Модель для валидации выходных данных
class PredictionInput(BaseModel):
    Sex: int
    Age: float
    Fare: float
    Pclass: int

@app.get("/stats")
def stats():
    return {"request_count": request_count}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict_model")
def predict_model(input_data: PredictionInput):
    global request_count
    request_count += 1

    # Создание DF из данных
    new_data = pd.DataFrame({
        'Sex': [input_data.Sex],
        'Age': [input_data.Age],
        'Fare': [input_data.Fare],
        'Pclass': [input_data.Pclass]
    })

    # Предсказание
    predictions = model.predict(new_data)

    # Преобразование результатов
    result = "Survived" if predictions[0] == 1 else "Note Survived"

    return {"Prediction": result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app_api:app", host="0.0.0.0", port=5000, reload=True)