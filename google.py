import streamlit as st
import pandas as pd

def show_sheets_page():
    st.title("📄 قراءة بيانات من Google Sheets")

    # ✅ أدخل فقط ID الصحيح بدون /edit أو /gid
    sheet_id = "1i5isYjIXVZ2-v7TyS2URQ7eOzb6N_7f4ny64T74sTAQ"
    sheet_name = "str1"  # غيّر اسم الورقة حسب ما هو موجود عندك

    # 🧩 توليد رابط CSV مباشر من Google Sheets
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        # 📥 تحميل البيانات من Google Sheets
        df = pd.read_csv(url)
        st.success("✅ تم تحميل البيانات بنجاح من Google Sheets")
        st.dataframe(df)

    except Exception as e:
        st.error(f"❌ حدث خطأ أثناء تحميل البيانات:\n{e}")

# ▶️ تشغيل الصفحة
show_sheets_page()
