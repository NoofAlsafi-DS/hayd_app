import streamlit as st
import joblib

# تحميل النموذج
model = joblib.load('dehydration_model.pkl')

st.title("تطبيق تصنيف حالة الجفاف")
hydration_level = st.number_input("أدخل مستوى الترطيب", min_value=0, max_value=100)

if st.button("تصنيف"):
    prediction = model.predict([[hydration_level]])
    result = "الشخص يعاني من جفاف" if prediction[0] == 1 else "الشخص غير مصاب بالجفاف"
    st.write(result)