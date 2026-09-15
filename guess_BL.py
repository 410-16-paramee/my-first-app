
import time
import streamlit as st

st.title("วายทั่วไทย ใครให้ทาย💏")
st.write("🎯 มีทั้งหมด 25 ข้อ | ⏰ เวลา 2 นาที")


questions = [
    ("1. นักแสดงคู่ไหนรับบทเป็น “คินน์” และ “พอร์ช” ใน KinnPorsche The Series?",
     "มาย - อาโป"),

    ("2. ใครรับบทเป็น “สารวัตร” ใน เพราะเราคู่กัน?",
     "ไบร์ท วชิรวิชญ์"),

    ("3. คู่พระนายหลักของ นิทานพันดาว คือใคร?",
     "เอิร์ท - มิกซ์"),

    ("4. ใน แค่เพื่อนครับเพื่อน ใครรับบทเป็น “ปราณ”?",
     "โอม ภวัต"),

    ("5. ใน แค่เพื่อนครับเพื่อน ใครรับบทเป็น “ภัทร”?",
     "นนน"),

    ("6. คู่ “ซี – นุนิว” แสดงนำในซีรีส์เรื่องใดเป็นเรื่องแรก?",
     "นิ่งเฮียก็หาว่าซื่อ"),

    ("7. ใครรับบทเป็น “เรน” ใน บรรยากาศรัก?",
     "โนอึล"),

    ("8. ใครรับบทเป็น “พายุ” ใน บรรยากาศรัก?",
     "บอส"),

    ("9. ใน แฟนผมเป็นประธานนักเรียน นักแสดงคู่ไหนรับบท “วินซาวด์”?",
     "วินนี่ - สตางค์"),

    ("10. นักแสดงคู่ใดที่เพิ่งประกาศเป็นออฟฟิเชียลในค่าย DUMUNDI?",
     "ธีร์ - เวฟ"),

    ("11. ใน อย่าขอพี่เจน หากอยากทำเฟเวอร์เพื่อแลกกับคำขอ จะต้องไปหาใคร?",
     "พี่เจนใหญ่"),

    ("12. ใน อรุณรุ่ง นักแสดงคู่ใดรับบท “ภพธีร์” และ “หม่อมเจ้าทินกร”?",
     "อิน - องศา"),

    ("13. ใน รักสุดใจนายแฟนบอย นักแสดงคนใดรับบทเป็น “เรนจิ”?",
     "ริวจิน"),

    ("14. ใน WEIRDO-101 แรงโน้มถ่วงระหว่างเรา ซี เดชชาติ รับบทเป็นตัวละครชื่อว่าอะไร?",
     "ชีวา"),

    ("15. ใน SOTUS The Series ตัวละครที่ชื่อ “ก้องภพ” มีรหัสนักศึกษาคือเลขอะไร?",
     "0062"),

    ("16. ใน ข้ามฟ้าเคียงเธอ นักแสดงคนใดรับบท “คณินทร์”?",
     "นุนิว"),

    ("17. ใน PAYBACK The Series ท็อปแทป จารุกิต มีชื่อในวงการว่าอะไร?",
     "ผอ. อาเธอร์"),

    ("18. แอลม่อน ภูมิสุวรรณ และ โปเกรส ภาชวิชญ์ รับบทเป็นตัวละครใดใน When Oranges Fall?",
     "โก๋หนึ่ง และ โก๋สอง"),

    ("19. นักแสดงคู่ใดรับบทเป็นตัวละครหลักในเรื่อง กี่หมื่นฟ้า?",
     "โทมัส - ก้อง"),

    ("20. ใน เขมจิราต้องรอด หมาในเรื่องชื่อว่าอะไร?",
     "เจ้าด่าง"),

    ("21. ใน Ticket To Heaven นักแสดงคนใดรับบทเป็น “แทนรัก”?",
     "โฟร์ท"),

    ("22. นักแสดงคู่ใดรับบทเป็นตัวละครหลักในเรื่อง พี่จะตีนะเนย?",
     "ต้า - บอม"),

    ("23. วงดนตรีในเรื่อง แฟนผมเป็นประธานนักเรียน ชื่อวงดนตรีอะไร?",
     "ชินชิลล่า"),

    ("24. นักแสดงคนใดเล่นเรื่อง ชอกะเชย์คู่กัน A BOSS AND A BABE?",
     "ฟอส - บุ๊ค"),

    ("25. ใน ปลาบนฟ้า คู่พระนายหลักเรียนคณะอะไร?",
     "ทันตแพทยศาสตร์ - แพทย์ศาสตร์"),
]


answers = [
    ["มาย - อาโป", "มายอาโป", "มาย อาโป"],
    ["ไบร์ท วชิรวิชญ์", "ไบร์ท", "วชิรวิชญ์"],
    ["เอิร์ท - มิกซ์", "เอิร์ทมิกซ์", "เอิร์ท มิกซ์"],
    ["โอม ภวัต", "โอม", "ภวัต"],
    ["นนน"],
    ["นิ่งเฮียก็หาว่าซื่อ"],
    ["โนอึล"],
    ["บอส"],
    ["วินนี่ - สตางค์", "วินนี่สตางค์", "วินนี่ สตางค์"],
    ["ธีร์ - เวฟ", "ธีร์เวฟ", "ธีร์ เวฟ"],
    ["พี่เจนใหญ่"],
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
    ["ทันตแพทยศาสตร์ - แพทย์ศาสตร์",
     "ทันตแพทยศาสตร์ แพทย์ศาสตร์",
     "ทันตแพทยศาสตร์-แพทย์ศาสตร์"],
]



if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(questions)

if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False



def reset_game():
    st.session_state.answers = [""] * len(questions)
    st.session_state.start = time.time()
    st.session_state.is_ended = False



def clean_text(text):
    return (
        text.strip()
        .lower()
        .replace(" ", "")
        .replace("-", "")
        .replace("–", "")
    )


def check_answer(user_answer, correct_answers):
    user_answer = clean_text(user_answer)

    for answer in correct_answers:
        if user_answer == clean_text(answer):
            return True

    return False



@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():

    score = 0

    for i in range(len(questions)):
        user_answer = st.session_state.answers[i]

        if check_answer(user_answer, answers[i]):
            score += 1

    st.balloons()

    st.success(f"🏆 ได้คะแนนทั้งหมด {score} / {len(questions)} คะแนน")

  

    if score == 25:
        st.success(
            "🎉 ยินดีด้วย 🥳\n\n"
            "คุณเป็นสาววาย Lv.999+" )

    elif score >= 20:
        st.success(
            "😎 เก่งมาก!!\n\n"
            "คุณเป็นสาววาย Lv.99"  )

    elif score >= 10:
        st.info(
            "💕 คุณทำได้ดีแล้ว" )

    else:
        st.warning(
            "✌️ พยายามอีกหน่อย" )



st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game,
    use_container_width=True
)



if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    elapsed = time.time() - st.session_state.start
    time_left = int(120 - elapsed)

    if time_left > 0:

        minutes = time_left // 60
        seconds = time_left % 60

        st.error(
            f"⏳ เหลือเวลา: {minutes:02d}:{seconds:02d}"
        )

    else:

        st.session_state.is_ended = True
        st.rerun()


st.divider()




for i, (question, correct_answer) in enumerate(questions):

    st.session_state.answers[i] = st.text_input(
        question,
        value=st.session_state.answers[i],
        key=f"answer_{i}"
    )



if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button(
        "📥 ส่งคำตอบ",
        use_container_width=True
    ):

        st.session_state.is_ended = True
        st.rerun()



if st.session_state.is_ended:
    show_result_dialog()


st.divider()

st.write("กลุ่มที่ 1 ")

