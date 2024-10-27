import streamlit as st
import joblib
from PIL import Image

# تحميل النموذج
model = joblib.load('dehydration_model.pkl')

# إضافة CSS لتخصيص الثيم
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa; /* لون خلفية مائي */
    }
    h1 {
        color: #00796b; /* لون عنوان التطبيق */
    }
    .stButton>button {
        background-color: #009688; /* لون زر */
        color: white; /* لون نص الزر */
    }
    .stTextInput>div>input {
        border: 2px solid #00796b; /* لون حدود حقل الإدخال */
    }
    .stImage {
        border-radius: 10px; /* زوايا مستديرة للصور */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# تغيير عنوان التطبيق
st.title("لاصقة مراقبة الجفاف")

# إضافة مقدمة للتطبيق
st.markdown("""
    ## مقدمة
    هذا التطبيق يقيس مستوى الجفاف في الجسم ويصنف مستوى الرطوبة في الجسم. 
    أدخل مستوى الترطيب الخاص بك، وسنساعدك في تحديد ما إذا كنت تعاني من جفاف أم لا.
""")

hydration_level = st.number_input("أدخل مستوى الترطيب", min_value=0, max_value=100)

if st.button("تصنيف"):
    prediction = model.predict([[hydration_level]])
    
    if prediction[0] == 1:
        result = "الشخص يعاني من جفاف"
        st.write(result)
        # عرض الصورة عند الإصابة بالجفاف
        img_dehydrated = Image.open("/home/ec2-user/hydration_app/little-kid-feeling-thirsty-want-600nw-2371892167.jpg.webp")  # ضع مسار الصورة هنا
        st.image(img_dehydrated, caption='الشخص مصاب بالجفاف', use_column_width=True)
        # إضافة نصيحة
        st.warning("نصيحة: يُرجى شرب الماء بكميات كافية وزيارة الطبيب إذا استمرت الأعراض.")
    else:
        result = "الشخص غير مصاب بالجفاف"
        st.write(result)
        # عرض الصورة عند عدم الإصابة بالجفاف
        img_hydrated = Image.open("/home/ec2-user/hydration_app/images-8.jpeg")  # ضع مسار الصورة هنا
        st.image(img_hydrated, caption='الشخص غير مصاب بالجفاف', use_column_width=True)
