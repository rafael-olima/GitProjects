import streamlit as st
import requests

def main():

    pclass = st.sidebar.selectbox(label='PClass',options=(1,2,3))
    sex = st.sidebar.selectbox(label='Sex',options=(1,0))
    age = st.sidebar.number_input(label='Age',min_value=0,max_value=100,step=1)
    sibSp = st.sidebar.number_input(label='Siblings',min_value=1,max_value=10,step=1)
    parch = st.sidebar.number_input(label='Parch',min_value=1,max_value=10,step=1)
    embarked = st.sidebar.selectbox(label='Embarked',options=['C','Q','S'])

    classify = st.sidebar.button('Classify')

    if classify:
        url = f"http://127.0.0.1:8000/predict"

        input = {
            'pclass': pclass,
            'sex': sex,
            'age': age,
            'sibSp': sibSp,
            'parch': parch,
            'embarked': embarked
        }

        print(input)
        response = requests.post(url, json=input)
        if response.status_code == 200:
            if response.json()['prediction'] == 1:
                st.image('survived.png')
            else:
                st.image('died.png')
        else:
            st.error(response.json())

if __name__ == "__main__":
    main()