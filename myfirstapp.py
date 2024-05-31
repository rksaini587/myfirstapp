import streamlit as st

st.title('BMI Calculator')

Height=st.number_input('Enter Height')
Weight=st.number_input('Enter Weight')

Calculate=st.button('Calculate BMI')


if (Calculate):
    bmi=Weight/Height**2*10000

    if(bmi<20):
        st.title(f' BMI: {bmi}. You are underweight')

    elif(bmi>20 and bmi<=25):
        st.title(f'BMI:{bmi}. You are noraml weight')

    else:
        st.title(f'BMI:{bmi}. You are over weight ')
