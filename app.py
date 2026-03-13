
import streamlit as st
import requests

@st.cache_data(ttl="1 day")
def get_rates():
    url = "https://open.er-api.com/v6/latest/RUB"
    inverse_rates = requests.get(url).json()["rates"]
    return {x: 1 / y for x, y in inverse_rates.items()}

st.title("Конвертер валют")
col1, col2 = st.columns(2)
inp_value = col1.number_input("", min_value=0, value=1)
rates = get_rates()
currency = col2.selectbox("Валюта", list(rates))
st.success(f"{inp_value * rates[currency]:,.2f} RUB")
