import time
import streamlit as st

st.set_page_config(
    page_title="วายทั่วไทย ใครให้ทาย",
    page_icon="💗",
    layout="centered"
)

st.title("💗 เกมตอบคำถามเพื่อพิสูจน์ว่าคุณคือสาววายตัวจริง!!")
st.write("🎯 มีทั้งหมด 25 ข้อ | ⏰ เวลา 5 นาที")

questions = [
    "1. นักแสดงคู่ไหนรับบทเป็น “คินน์” และ “พอร์ช” ใน KinnPorsche The Series?",
    "2. ใครรับบทเป็น “สารวัตร” ใน เพราะเราคู่กัน?",
    "3. คู่พระนายหลักของ นิทานพันดาว คือใคร?",
    "4. ใน แค่เพื่อนครับเพื่อน ใครรับบทเป็น “ปราณ”?",
    "5. ใน แค่เพื่อนครับเพื่อน ใครรับบทเป็น “ภัทร”?",
    "6. คู่ “ซี – นุนิว” แสดงนำในซีรีส์เรื่องใดเป็นเรื่องแรก?",
    "7. ใครรับบทเป็น “เรน” ใน บรรยากาศรัก?",
    "8. ใครรับบทเป็น “พายุ” ใน บรรยากาศรัก?",
    "9. ใน แฟนผมเป็นประธานนักเรียน นักแสดงคู่ไหนรับบท “วินซาวด์”?",
    "10. นักแสดงคู่ใดที่เพิ่งประกาศเป็นออฟฟิเชียลในค่าย DUMUNDI?",
    "11. ใน อย่าขอพี่เจน หากอยากทำเฟเวอร์เพื่อแลกกับคำขอ จะต้องไปหาใคร?",
    "12. ใน อรุณรุ่ง นักแสดงคู่ใดรับบท “ภพธีร์” และ “หม่อมเจ้าทินกร”?",
    "13. ใน รักสุดใจนายแฟนบอย นักแสดงคนใดรับบทเป็น “เรนจิ”?",
    "14. ใน WEIRDO-101 แรงโน้มถ่วงระหว่างเรา ซี เดชชาติ รับบทเป็นตัวละครชื่อว่าอะไร?",
    "15. ใน SOTUS The Series ตัวละครที่ชื่อ “ก้องภพ” มีรหัสนักศึกษาคือเลขอะไร?",
    "16. ใน ข้ามฟ้าเคียงเธอ นักแสดงคนใดรับบท “คณินทร์”?",
    "17. ใน PAYBACK The Series ท็อปแทป จารุกิต มีชื่อในวงการว่าอะไร?",
    "18. แอลม่อน ภูมิสุวรรณ และ โปเกรส ภาชวิชญ์ รับบทเป็นตัวละครใดใน When Oranges Fall?",
    "19. นักแสดงคู่ใดรับบทเป็นตัวละครหลักในเรื่อง กี่หมื่นฟ้า?",
    "20. ใน เขมจิราต้องรอด หมาในเรื่องชื่อว่าอะไร?",
    "21. ใน Ticket To Heaven นักแสดงคนใดรับบทเป็น “แทนรัก”?",
    "22. นักแสดงคู่ใดรับบทเป็นตัวละครหลักในเรื่อง พี่จะตีนะเนย?",
    "23. วงดนตรีในเรื่อง แฟนผมเป็นประธานนักเรียน ชื่อวงดนตรีอะไร?",
    "24. นักแสดงคนใดเล่นเรื่อง ชอกะเชย์คู่กัน A BOSS AND A BABE?",
    "25. ใน ปลาบนฟ้า คู่พระนายหลักเรียนคณะอะไร?"
]
answers = [
    ["มาย - อาโป", "มายอาโป", "มาย อาโป"],
    ["ไบร์ท วชิรวิชญ์", "ไบร์ท"],
    ["เอิร์ท - มิกซ์", "เอิร์ทมิกซ์", "เอิร์ท มิกซ์"],
    ["โอม ภวัต", "โอม", "ภวัต"],
    ["นนน"],
    ["นิ่งเฮียก็หาว่าซื่อ"],
    ["โนอึล"],
    ["บอส"],
    ["วินนี่ - สตางค์", "วินนี่สตางค์", "วินนี่ สตางค์"],
    ["ธีร์ - เวฟ", "ธีร์เวฟ", "ธีร์ เวฟ"],
    ["พี่เจนใหญ่" ,"เจนใหญ่"],
    ["อิน - องศา", "อินองศา", "อิน องศา"],
    ["ริวจิน"],
    ["ชีวา"],
    ["0062"],
    ["นุนิว"],
    ["ผอ. อาเธอร์", "อาเธอร์"],
    ["โก๋หนึ่ง และ โก๋สอง", "โก๋หนึ่ง โก๋สอง", "โก๋หนึ่งและโก๋สอง"],
    ["โทมัส - ก้อง", "โทมัสก้อง", "โทมัส ก้อง"],
    ["เจ้าด่าง"],
    ["โฟร์ท"],
    ["ต้า - บอม", "ต้าบอม", "ต้า บอม"],
    ["ชินชิลล่า"],
    ["ฟอส - บุ๊ค", "ฟอสบุ๊ค", "ฟอส บุ๊ค"],
    [
        "ทันตแพทย์ฺ - แพทย์",
        "ทันตแพทย์ แพทย์",
        "ทันตแพทย์-แพทย์"
    ]
]

if "answers_user" not in st.session_state:
    st.session_state.answers_user = [""] * 25

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


def reset_game():

    st.session_state.start = time.time()

    st.session_state.is_ended = False

    st.session_state.answers_user = [""] * 25

    # ล้างค่าช่องคำตอบเดิม
    for i in range(25):

        key = f"answer_{i}"

        if key in st.session_state:
            del st.session_state[key]


def clean_text(text):

    text = str(text)

    text = text.strip().lower()

    # ลบช่องว่าง
    text = text.replace(" ", "")

    # ลบเครื่องหมายขีด
    text = text.replace("-", "")
    text = text.replace("–", "")
    text = text.replace("—", "")

    return text



def check_answer(user_answer, correct_answers):

    user_answer = clean_text(user_answer)

    if user_answer == "":
        return False

    for correct in correct_answers:

        if user_answer == clean_text(correct):
            return True

    return False


def calculate_score():

    score = 0

    for i in range(25):

        user_answer = st.session_state.answers_user[i]

        if check_answer(user_answer, answers[i]):
            score += 1

    return score



@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():

    score = calculate_score()

    st.balloons()

    st.subheader("🏆 คะแนนของคุณ")

    st.markdown(
        f"""
        <div style="
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #ff4b8b;
            margin: 10px;
        ">
            {score} / 25
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()


    if score == 25:

        st.success(
            "🎉 ยินดีด้วย 🥳\n\n"
            "คุณเป็นสาววาย Lv.999+"
        )

    elif score >= 20:

        st.success(
            "😎 เก่งมาก!!\n\n"
            "คุณเป็นสาววาย Lv.99"
        )

    elif score >= 10:

        st.info(
            "💕 คุณทำได้ดีแล้ว"
        )

    else:

        st.warning(
            "✌️ คะแนนต่ำกว่า 10\n\n"
            "พยายามอีกหน่อย"
        )

    st.divider()



    st.subheader("📝 ตรวจคำตอบ")

    for i in range(25):

        user_answer = st.session_state.answers_user[i]

        if check_answer(user_answer, answers[i]):

            st.success(
                f"ข้อ {i + 1} ✅ ถูก — {user_answer}"
            )

        else:

            st.error(
                f"ข้อ {i + 1} ❌ ผิด — "
                f"คำตอบของคุณ: "
                f"{user_answer if user_answer else 'ไม่ได้ตอบ'}"
            )



st.button(
    "🎮 เริ่มเล่นเกมใหม่",
    on_click=reset_game,
    use_container_width=True
)


if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    elapsed = time.time() - st.session_state.start

    # 5 นาที = 300 วินาที
    time_left = int(300 - elapsed)

    if time_left > 0:

        minutes = time_left // 60
        seconds = time_left % 60

        # เหลือไม่ถึง 30 วินาที
        if time_left <= 30:

            st.error(
                f"🚨 เหลือเวลา: {minutes:02d}:{seconds:02d}"
            )

        # เหลือไม่ถึง 1 นาที
        elif time_left <= 60:

            st.warning(
                f"⚠️ เหลือเวลา: {minutes:02d}:{seconds:02d}"
            )

        else:

            st.info(
                f"⏳ เหลือเวลา: {minutes:02d}:{seconds:02d}"
            )

    else:

        st.session_state.is_ended = True

        st.rerun()


st.divider()


if st.session_state.start is None:

    st.info(
        "👆 กดปุ่ม “🎮 เริ่มเล่นเกมใหม่” เพื่อเริ่มเกม"
    )

else:

    for i in range(25):

        user_answer = st.text_input(
            questions[i],
            value=st.session_state.answers_user[i],
            key=f"answer_{i}",
            disabled=st.session_state.is_ended
        )

        st.session_state.answers_user[i] = user_answer



if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    st.divider()

    if st.button(
        "📥 ส่งคำตอบ",
        use_container_width=True
    ):

        st.session_state.is_ended = True

        st.rerun()



if st.session_state.is_ended:

    show_result_dialog()



st.divider()

st.write("I 💗 BL ")
