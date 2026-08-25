import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = "" 
    st.session_state.start = time.time() 
    st.session_state.is_ended = False 

@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()


    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")


    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")


    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2


if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)
import streamlit as st

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


ans3 = st.text_input(
    "คำตอบข้อ 3",
    value=st.session_state.ans3_val
)

ans4 = st.text_input(
    "คำตอบข้อ 4",
    value=st.session_state.ans4_val
)


if st.button("ตรวจคำตอบ"):

    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""


    ans3 = st.text_input("คำตอบข้อ 3")
    ans4 = st.text_input("คำตอบข้อ 4")


u_ans3 = ans3.strip().lower()
u_ans4 = ans4.strip().lower()


correct_ans3 = "คำตอบข้อ3"
correct_ans4 = "คำตอบข้อ4"

score = 0

if u_ans3 == correct_ans3:
    score += 1

if u_ans4 == correct_ans4:
    score += 1


if u_ans3 == correct_ans3 and u_ans4 == correct_ans4:
    score = 4



ans3 = st.text_input(
    "กรอกคำตอบข้อ 3",
    key="input_ans3"
)

ans4 = st.text_input(
    "กรอกคำตอบข้อ 4",
    key="input_ans4"
)



if st.button("ส่งคำตอบ"):

    st.session_state.ans3_val = ans3
    st.session_state.ans4_val = ans4


    st.write("คำตอบข้อ 3 :", st.session_state.ans3_val)
    st.write("คำตอบข้อ 4 :", st.session_state.ans4_val)



if st.button("ดูผลลัพธ์"):

    @st.dialog("ผลลัพธ์")
    def show_result():
        st.write("คำตอบข้อ 3 :", st.session_state.ans3_val)
        st.write("คำตอบข้อ 4 :", st.session_state.ans4_val)
        st.write("คะแนน :", score)

    show_result()
st.divider()
st.write("นางสาวปารมี จันทร์เลิศ เลขที่ 16 ม.4/10")

