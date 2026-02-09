import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator")

# รับค่าตัวเลข
num1 = st.number_input("ใส่ตัวเลขที่ 1", value=0.0)
num2 = st.number_input("ใส่ตัวเลขที่ 2", value=0.0)

# เลือกการคำนวณ
operation = st.selectbox(
    "เลือกการคำนวณ",
    ("บวก (+)", "ลบ (-)", "คูณ (×)", "หาร (÷)")
)

# ปุ่มคำนวณ
if st.button("คำนวณ"):
    if operation == "บวก (+)":
        result = num1 + num2
    elif operation == "ลบ (-)":
        result = num1 - num2
    elif operation == "คูณ (×)":
        result = num1 * num2
    elif operation == "หาร (÷)":
        if num2 == 0:
            st.error("❌ ห้ามหารด้วย 0")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"✅ ผลลัพธ์ = {result}")
