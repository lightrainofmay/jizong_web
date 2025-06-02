import streamlit as st
import random
import csv
import os
import base64

# ========== 题库 ==========
quiz_data = [
    {"img": f"assets/images/jizong{i}.jpg", "is_chicken": True,
     "explain_cn": "这是鸡枞菌，安全可食，常见于白蚁堆附近。",
     "explain_en": "This is Jizong mushroom. Edible and found near termite nests."}
    for i in ["", "1", "2", "3", "4"]
] + [
    {"img": f"assets/images/dumogu{i}.jpg", "is_chicken": False,
     "explain_cn": "这是鹅膏菌，剧毒，有典型“帽子、裙子、鞋子”结构。",
     "explain_en": "This is a deadly Amanita. Cap, ring, and volva structure."}
    for i in ["", "1", "2", "3", "4"]
] + [
    {"img": "assets/images/qianlvzhegu.jpg", "is_chicken": False,
     "explain_cn": "这是铅绿褶菇，有毒，具有灰白菌盖和绿色菌褶。",
     "explain_en": "This is Entoloma sinuatum. Toxic, with gray-white cap and greenish gills."},
    {"img": "assets/images/dusanjun.jpg", "is_chicken": False,
     "explain_cn": "这是毒伞菌，有毒，菌盖白色带鳞片，柄细长。",
     "explain_en": "This is Lepiota. Toxic, with white scaly cap and thin long stalk."}
]
TOTAL_ROUNDS = 15

# ========== 音效播放 ==========
def play_feedback(is_correct=True):
    path = "assets/audio/correct.mp3" if is_correct else "assets/audio/incorrect.mp3"
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """, unsafe_allow_html=True)

# ========== 图片展示 ==========
def show_image_fixed(path, width=400, height=300):
    if not os.path.exists(path):
        st.warning("图像文件未找到")
        return
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div style="text-align:center">
            <img src="data:image/jpeg;base64,{b64}" 
                 style="width:{width}px; height:{height}px; object-fit:cover; border:1px solid #ccc; border-radius:8px;">
        </div>
        """, unsafe_allow_html=True)

# ========== 答题逻辑 ==========
def process_answer(user_choice, current):
    correct = current["is_chicken"]
    st.session_state.quiz_total += 1
    st.session_state.quiz_answered = True
    st.session_state.last_answer_correct = user_choice == correct
    if st.session_state.last_answer_correct:
        st.session_state.quiz_correct += 1

# ========== 排行榜 ==========
def show_leaderboard(lang):
    path = "data/leaderboard.csv"
    if not os.path.exists(path):
        st.markdown("暂无数据。" if lang == "中文" else "No scores yet.")
        return

    with open(path, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    best_scores = {}
    for row in rows:
        name, correct, total, acc = row
        acc = float(acc)
        if name not in best_scores or acc > float(best_scores[name][3]):
            best_scores[name] = row

    sorted_rows = sorted(best_scores.values(), key=lambda x: float(x[3]), reverse=True)

    for i, row in enumerate(sorted_rows[:10]):
        name, correct, total, acc = row
        st.markdown(f"{i+1}. **{name}** - {correct}/{total} ({acc}%)")

# ========== 主函数 ==========
def render(lang="中文"):
    st.title("🍄 小游戏：鸡枞菌识别挑战！" if lang == "中文" else "🍄 MiniGame：Jizong Mushroom Challenge!")

    if "player_name" not in st.session_state:
        st.session_state.player_name = ""

    if not st.session_state.player_name:
        st.session_state.player_name = st.text_input("请输入你的名字：" if lang == "中文" else "Enter your name:")
        if not st.session_state.player_name:
            st.stop()

    # 初始化
    if "quiz_pool" not in st.session_state or st.session_state.get("restart_flag", False):
        st.session_state.quiz_pool = random.sample(quiz_data * 2, TOTAL_ROUNDS)
        st.session_state.quiz_index = 0
        st.session_state.quiz_total = 0
        st.session_state.quiz_correct = 0
        st.session_state.quiz_answered = False
        st.session_state.restart_flag = False

    # 游戏结束
    if st.session_state.quiz_index >= TOTAL_ROUNDS:
        st.success("🎉 游戏结束！" if lang == "中文" else "🎉 Game Over!")
        acc = round(100 * st.session_state.quiz_correct / st.session_state.quiz_total, 1)
        name = st.session_state.player_name
        os.makedirs("data", exist_ok=True)
        with open("data/leaderboard.csv", "a", newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([name, st.session_state.quiz_correct, st.session_state.quiz_total, acc])
        st.markdown(f"✅ 最终得分：{st.session_state.quiz_correct}/{st.session_state.quiz_total}，正确率：{acc}%" if lang == "中文"
                    else f"✅ Final Score: {st.session_state.quiz_correct}/{st.session_state.quiz_total}, Accuracy: {acc}%")

        if st.button("🔄 再玩一次" if lang == "中文" else "🔄 Play Again"):
            st.session_state.restart_flag = True
            st.rerun()

        st.markdown("---")
        st.subheader("🏆 排行榜" if lang == "中文" else "🏆 Leaderboard")
        show_leaderboard(lang)
        return

    # 当前题目
    current = st.session_state.quiz_pool[st.session_state.quiz_index]
    show_image_fixed(current["img"])
    st.markdown("这是鸡枞菌吗？" if lang == "中文" else "Is this a Jizong mushroom?")

    if not st.session_state.quiz_answered:
        col1, col2 = st.columns(2)
        if col1.button("是" if lang == "中文" else "Yes"):
            process_answer(True, current)
        if col2.button("不是" if lang == "中文" else "No"):
            process_answer(False, current)

    if st.session_state.quiz_answered:
        play_feedback(st.session_state.last_answer_correct)
        if st.session_state.last_answer_correct:
            st.success("✅ 回答正确！" if lang == "中文" else "✅ Correct!")
        else:
            st.error("❌ 回答错误！" if lang == "中文" else "❌ Incorrect!")
        st.info(current["explain_cn"] if lang == "中文" else current["explain_en"])

        if st.button("下一题" if lang == "中文" else "Next"):
            st.session_state.quiz_index += 1
            st.session_state.quiz_answered = False
            st.rerun()

    if st.session_state.quiz_total > 0:
        acc = round(100 * st.session_state.quiz_correct / st.session_state.quiz_total, 1)
        st.info(f"✅ 已答：{st.session_state.quiz_total} 题，正确：{st.session_state.quiz_correct}，正确率：{acc}%" if lang == "中文"
                else f"✅ Attempts: {st.session_state.quiz_total}, Correct: {st.session_state.quiz_correct}, Accuracy: {acc}%")

    st.markdown("---")
    st.subheader("🏆 排行榜" if lang == "中文" else "🏆 Leaderboard")
    show_leaderboard(lang)