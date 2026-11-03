"""UBE Safety Talk — participant starting point (NOT final app)."""
import streamlit as st

st.set_page_config(page_title="UBE Safety Talk | Workshop", layout="wide")
st.title("UBE Safety Talk — Workshop Day 1")
st.info("เริ่มต้นโปรเจกต์เรียบร้อย: เปิดไฟล์ PROMPTS แล้วให้ Codex ช่วยพัฒนาทีละขั้นตอน")
st.markdown("**เป้าหมาย:** Safety Talk Form • CSV + Report ID • Dashboard • History")
with st.sidebar:
    st.header("UBE Safety Workshop")
    st.caption("ต้นแบบสำหรับฝึกอบรมในเครื่องเท่านั้น")
st.write("✅ ถ้าเห็นหน้านี้ แสดงว่าติดตั้งและ Run Streamlit ได้แล้ว")
