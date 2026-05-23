import streamlit as st
import requests

# 1. إعدادات النظام السيادي
st.set_page_config(page_title="Global Sales Nexus", layout="wide")
st.title("🌐 بوابة التاجر العالمي - منصة المليون دولار")

# 2. لوحة التحكم
with st.sidebar:
    st.header("إعدادات التاجر")
    sales_type = st.radio("نوع المنتج:", ["منتج رقمي (Digital)", "منتج مادي (Physical)"])
    market_target = st.text_input("السوق المستهدف (مثلاً: الجزائر، الخليج، أمريكا):")

# 3. إدخال بيانات أي منتج
st.subheader("تفاصيل المنتج:")
product_name = st.text_input("اسم المنتج الذي تريد بيعه الآن:")
price = st.number_input("سعر البيع (بالدولار):", min_value=1.0)
description = st.text_area("وصف موجز للمنتج:")

# 4. محرك التنفيذ الذكي
if st.button("🚀 توليد خطة المبيعات السيادية"):
    if product_name:
        with st.spinner("جاري برمجة إمبراطوريتك الرقمية..."):
            payload = {
                "type": sales_type,
                "target_market": market_target,
                "product": product_name,
                "price": price,
                "description": description,
                "status": "INITIATING_SALES_FUNNEL"
            }
            try:
                # هذا هو الرابط الذي أعطيتني إياه سابقاً
                requests.post("http://localhost:5678/webhook/market-analyzer-v1", json=payload)
                st.success("✅ تم إرسال المنتج للمحرك! سيقوم الذكاء الاصطناعي الآن بكتابة خطة التسويق.")
                st.json(payload)
            except:
                st.error("خطأ في الاتصال بالمحرك الرقمي.")
    else:
        st.error("الرجاء إدخال اسم المنتج.")

st.caption("بروتوكول عديد العيد - تحويل كل معلومة إلى مال.")
