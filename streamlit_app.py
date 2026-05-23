import streamlit as st

# إعداد الصفحة لتكون بملء الشاشة
st.set_page_config(page_title="منصة المليون دولار", layout="wide")

# تصميم Sidebar احترافي
with st.sidebar:
    st.header("إعدادات التاجر")
    product_type = st.radio("نوع المنتج:", ["Digital", "Physical"])
    target_market = st.multiselect("السوق المستهدف:", ["الجزائر", "الخليج", "أوروبا", "أمريكا"])
    st.divider()
    st.info("بروتوكول عديد العيد - تحويل كل معلومة إلى مال")

# تصميم المحتوى الرئيسي
st.title("🌐 بوابة التاجر العالمي - منصة المليون دولار")
st.subheader("تحليل وتوليد خطط المبيعات السيادية")

col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("اسم المنتج الذي تريد بيعه:")
    price = st.number_input("سعر البيع (بالدولار):", min_value=0.0, value=20000.0)

with col2:
    currency = st.selectbox("العملة:", ["USD", "EUR", "DZD"])
    category = st.selectbox("فئة المنتج:", ["Legal Tech", "Digital Services", "Consulting"])

description = st.text_area("وصف موجز للمنتج (القيمة المضافة):", height=150)

if st.button("🚀 توليد خطة المبيعات السيادية"):
    if product_name:
        st.success("تم إرسال البيانات للمعالجة - جاري استخراج الثغرات الربحية...")
        # هنا سيتم ربط الكود بـ n8n لاحقاً
    else:
        st.error("يرجى إدخال اسم المنتج للمتابعة.")
