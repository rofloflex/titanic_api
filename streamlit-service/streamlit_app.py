import streamlit as st
import requests
from requests.exceptions import ConnectionError

ip_api = "titanic-api"  # IP адрес или имя хоста Flask API
port_api = "5000"

# Заголовок приложния
st.title("Titanick Survival Prediction:")

# Вывод данных
st.write("Enter the pessenger details:")

# Выпадающее меню для выбора пола
sex = st.selectbox("Sex: 0(female), 1(male)", [0, 1])

# Текстовое поле для ввода возраста с проверкой на число
age = st.text_input("Age", value=10)
if not age.isdigit():
    st.error("Please enter a valid number for Age.")

# Текстовое поле для вывода стоимости билета с проверкой на число
fare = st.text_input("Fare", value=100)
if not fare.isdigit():
    st.error("Please enter a valid number for Fare.")

# Выпадающее меню для выбора класса билета
pclass = st.selectbox("Ticket Class (Pclass)", [1, 2, 3])

# Кнопка для отправки запроса
if st.button("Predict"):
    # Проверка, что все поля заполнены
    if age.isdigit() and fare.isdigit():
        # Подготовка данных для отправки
        data = {
            "Sex": int(sex),
            "Age": float(age),
            "Fare": float(fare),
            "Pclass": int(pclass)
        }

        try:
            # Отправка запроса к Flask API
            response = requests.post(f"http://{ip_api}:{port_api}/predict_model", json=data)

            # Проверка статуса ответа
            if response.status_code == 200:
                prediction = response.json()["Prediction"]
                st.success(f"Prediction: {prediction}")
            else:
                st.error(f"Request failed with status code {response.status_code}")
        except ConnectionError as e:
            st.error(f"Failed to connect to the server")
    else:
        st.error("Please fill in all fields with valid numbers.")