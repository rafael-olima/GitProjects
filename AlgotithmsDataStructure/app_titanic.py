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
        url = f"https://api-titanic.onrender.com/predict"

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
                st.write('Survived')
            else:
                st.write('Died')
        else:
            st.error(response.status_code)

if __name__ == "__main__":
    main()