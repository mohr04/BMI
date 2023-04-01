import streamlit as st

st.title('BMI')

weight = st.number_input("What's your weight (kg)", step =1)
height = st.number_input("What's your height (meters)")

st.camera_input("cheers")




def bmi(weight, height):
    bmi = round(weight / (height ** 2),1)
    if bmi > 29.9:
        rate = "Obese"
    elif 24.9 < bmi < 30:
        rate = "Overweight"
    elif 18.4 < bmi < 25:
        rate = "Normal, well done"
    else:
        rate = "Underweight"
    return f"Your BMI score is {bmi} and you are at risk of being {rate} "

if st.button("Calculate BMI"):
    st.balloons()
    st.write(bmi(weight, height))
