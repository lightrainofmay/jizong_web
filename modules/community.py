import streamlit as st

def render(lang="中文"):
    st.title("🤝 社区参与与传承" if lang == "中文" else "🤝 Community Engagement & Transmission")
    st.markdown("---")

    if "show_form" not in st.session_state:
        st.session_state.show_form = False
    if "submissions" not in st.session_state:
        st.session_state.submissions = []

    # 一、项目介绍
    if lang == "中文":
        st.subheader("📚 鸡枞文化日")
        st.markdown("""
欢迎参与“鸡枞菌文化日”活动！  
点击下方按钮上传你与鸡枞的故事：图片、音频或文字内容，展示你与鸡枞的美好记忆。
        """)
    else:
        st.subheader("📚 Jizong Cultural Day")
        st.markdown("""
Welcome to our **Jizong Mushroom Cultural Day**!  
Click the button below to upload your story with images, audio, or text to showcase your memory with Jizong.
        """)

    # 二、点击按钮显示上传表单
    if not st.session_state.show_form:
        if st.button("📤 上传你的故事" if lang == "中文" else "📤 Upload Your Story"):
            st.session_state.show_form = True

    # 三、上传表单区域（展开后）
    if st.session_state.show_form:
        with st.form("upload_form", clear_on_submit=True):
            col1, col2, col3 = st.columns([1.2, 1.5, 1.5])
            with col1:
                name = st.text_input("你的名字" if lang == "中文" else "Your name", max_chars=20)
            with col2:
                uploaded_image = st.file_uploader("图片" if lang == "中文" else "Image", type=["png", "jpg", "jpeg"])
            with col3:
                uploaded_audio = st.file_uploader("音频" if lang == "中文" else "Audio", type=["mp3", "wav", "m4a"])

            story_text = st.text_area("鸡枞故事（可中英文）" if lang == "中文" else "Jizong Story (bilingual)", height=100)

            submitted = st.form_submit_button("✅ 保存" if lang == "中文" else "✅ Save")
            if submitted:
                if name and (uploaded_image or uploaded_audio or story_text):
                    st.session_state.submissions.append({
                        "name": name,
                        "image": uploaded_image,
                        "audio": uploaded_audio,
                        "text": story_text
                    })
                    st.success("✅ 上传成功！已加入展示区。" if lang == "中文" else "✅ Upload successful! Added to the display.")
                    st.session_state.show_form = False
                else:
                    st.warning("请填写姓名并至少上传一项内容。" if lang == "中文" else "Please enter your name and upload at least one item.")

    st.markdown("---")

    # 四、用户上传展示
    st.subheader("🖼 用户上传展示" if lang == "中文" else "🖼 User Submissions")
    for i, sub in enumerate(st.session_state.submissions):
        st.markdown(f"**{i+1}. 来自 {sub['name']} 的分享**" if lang == "中文" else f"**{i+1}. Story from {sub['name']}**")
        if sub["image"]:
            st.image(sub["image"], width=300)
        if sub["audio"]:
            st.audio(sub["audio"])
        if sub["text"]:
            st.markdown(f"✍️ {sub['text']}")
        st.markdown("---")

    # 五、互动测验
    st.subheader("🎯 学习小测验" if lang == "中文" else "🎯 Knowledge Mini Quiz")
    if lang == "中文":
        st.markdown("请完成以下问题，并点击“提交答案”查看成绩：")
    else:
        st.markdown("Please complete the quiz and click 'Submit' to check your results:")

    q1 = st.radio("1️⃣ 鸡枞菌通常与哪种昆虫共生？" if lang == "中文" else "1️⃣ Jizong mushrooms live in symbiosis with which insect?",
                  options=["蜜蜂", "白蚁", "瓢虫"] if lang == "中文" else ["Bees", "Termites", "Ladybugs"], key="q1")
    q2 = st.radio("2️⃣ 下列哪个是成熟可采的鸡枞？" if lang == "中文" else "2️⃣ Which of the following is a mature, harvestable Jizong?",
                  options=["菌盖闭合的幼菌", "菌盖张开的鸡枞", "干枯的老鸡枞"] if lang == "中文" else ["Immature closed cap", "Mature open cap", "Dried old mushroom"], key="q2")
    q3 = st.radio("3️⃣ 鸡枞生态系统中最重要的地下结构是？" if lang == "中文" else "3️⃣ What is the key underground structure for Jizong’s growth?",
                  options=["菌丝", "树根", "岩石"] if lang == "中文" else ["Mycelium", "Tree roots", "Rocks"], key="q3")

    if st.button("📘 提交答案" if lang == "中文" else "📘 Submit Quiz"):
        correct = 0
        correct += 1 if q1 == ("白蚁" if lang == "中文" else "Termites") else 0
        correct += 1 if q2 == ("菌盖张开的鸡枞" if lang == "中文" else "Mature open cap") else 0
        correct += 1 if q3 == ("菌丝" if lang == "中文" else "Mycelium") else 0

        st.markdown("---")
        if correct == 3:
            st.success("🎉 全部答对了！你是鸡枞小达人！" if lang == "中文" else "🎉 Perfect score! You're a Jizong expert!")
        else:
            st.warning(f"你答对了 {correct} 题，再试试！" if lang == "中文" else f"You got {correct} correct. Try again!")

    st.markdown("---")

    # 六、结语
    if lang == "中文":
        st.info("🧒 通过记录与传承，我们可以更好地理解鸡枞文化的价值，也帮助下一代认识生态保护的重要性。")
    else:
        st.info("🧒 By recording and sharing, we pass on the cultural value of Jizong and promote ecological awareness among future generations.")