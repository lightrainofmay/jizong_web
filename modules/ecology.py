import streamlit as st
import os
import base64

def play_sound(file_name):
    path = os.path.join("assets/audio", file_name)
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            st.markdown(f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """, unsafe_allow_html=True)

def show_image_local(path, width=500):
    if not os.path.exists(path):
        st.warning(f"图片未找到: {path}")
        return
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div style="text-align:center">
            <img src="data:image/png;base64,{b64}" style="width:{width}px; border-radius:8px; border:1px solid #ccc; margin:10px 0;">
        </div>
        """, unsafe_allow_html=True)

def render(lang="中文"):
    st.title("🌱 生态系统与保护" if lang == "中文" else "🌱 Ecosystem & Conservation")
    st.markdown("---")

    st.subheader("🌿 鸡枞的自然生态" if lang == "中文" else "🌿 Natural Ecology of Jizong")
    st.markdown("""
    鸡枞菌对环境要求极高，必须在特定的生态条件下才能自然生长，目前尚无成熟的人工种植方法。

    鸡枞与白蚁共生，在白蚁垒筑的“蚁穴”中生长，依赖微生物、温湿度、土壤等多个因素共同作用，是典型的生态系统“合作产物”。
    """ if lang == "中文" else """
    Jizong mushrooms grow only in specific ecological conditions and have not yet been successfully cultivated artificially.

    They exist in symbiosis with termites, growing on “fungus combs” built by termite colonies. Their survival depends on a complex mix of microbes, temperature, humidity, and soil — a perfect example of ecological cooperation.
    """)

    show_image_local("assets/images/shengtai.png", width=500)
    st.markdown("---")

    st.subheader("🧺 保护性采摘方法" if lang == "中文" else "🧺 Sustainable Harvesting Techniques")
    st.markdown("""
- 不破坏菌丝和周围生态  
- 只采摘成熟的菌盖与菌柄  
- 保留菌丝，以便再次繁殖  
- 用竹篓等透气容器装载  
    """ if lang == "中文" else """
- Do not damage underground mycelium or habitat  
- Only pick fully matured caps  
- Leave the base to enable regrowth  
- Use breathable containers like bamboo baskets  
    """)

    st.image("https://raw.githubusercontent.com/lightrainofmay/jizong_web/main/assets/images/baohu1.PNG", width=350)
    st.image("https://raw.githubusercontent.com/lightrainofmay/jizong_web/main/assets/images/baohu2.PNG", width=350)
    st.image("https://raw.githubusercontent.com/lightrainofmay/jizong_web/main/assets/images/baohu3.PNG", width=350)

    st.markdown("---")
    st.subheader("🎮 模拟鸡枞采摘" if lang == "中文" else "🎮 Simulated Jizong Harvest")

    mushrooms = [
        {"img": "mature jizong.PNG", "name_cn": "成熟鸡枞菌", "name_en": "Mature Jizong", "pickable": True},
        {"img": "unmature jizong.PNG", "name_cn": "未成熟菌", "name_en": "Immature", "pickable": False},
        {"img": "junsi.PNG", "name_cn": "菌丝", "name_en": "Mycelium", "pickable": False},
        {"img": "gankujizong.PNG", "name_cn": "干枯鸡枞", "name_en": "Dried Jizong", "pickable": False},
    ]

    if "eco_score" not in st.session_state:
        st.session_state.eco_score = 0

    correct, wrong = [], []
    cols = st.columns(len(mushrooms))
    for i, m in enumerate(mushrooms):
        with cols[i]:
            show_image_local(f"assets/images/{m['img']}", width=160)
            label = m["name_cn"] if lang == "中文" else m["name_en"]
            if st.checkbox(label, key=f"pick_{i}"):
                if m["pickable"]:
                    st.session_state.eco_score += 1
                    correct.append(label)
                    st.success("👍 正确采摘！" if lang == "中文" else "👍 Good pick!")
                    play_sound("correct.mp3")
                else:
                    wrong.append(label)
                    st.warning("⚠️ 不建议采摘！" if lang == "中文" else "⚠️ Not recommended!")
                    play_sound("wrong.mp3")

    if correct or wrong:
        st.info("✅ 正确选择：" + ", ".join(correct) if lang == "中文" else "✅ Correct Picks: " + ", ".join(correct))
        st.info("❌ 错误选择：" + ", ".join(wrong) if lang == "中文" else "❌ Wrong Picks: " + ", ".join(wrong))

    if st.session_state.eco_score >= 1:
        st.success("🌍 恭喜你完成了生态采摘任务！" if lang == "中文" else "🌍 Well done! You’ve completed the eco-friendly harvest.")

    st.markdown("---")
    st.subheader("📈 鸡枞经济与生态数据" if lang == "中文" else "📈 Jizong Economy & Ecological Data")
    st.markdown("""
- 中国约70%的野生食用菌分布在云南  
- 鸡枞出口带动山区经济  
- 鸡枞保护关系白蚁、森林与生态系统平衡  
    """ if lang == "中文" else """
- ~70% of China’s wild mushrooms are from Yunnan  
- Jizong exports benefit rural income  
- Its conservation sustains termite-forest-fungi balance  
    """)

    st.markdown("---")
    st.subheader("🖼 生态链图示" if lang == "中文" else "🖼 Ecological Chain Diagram")

    st.markdown("""
生态链：**森林 → 白蚁 → 蚁穴 → 鸡枞 → 人类**  
保护生态链，需要我们共同守护鸡枞的生态家园。
    """ if lang == "中文" else """
Ecological Chain: **Forest → Termite → Nest → Jizong → Human**  
Preserving Jizong means sustaining the entire ecosystem.
    """)

    show_image_local("assets/images/shengtai5.PNG", width=500)

    st.info("🍄 鸡枞的保护，关系整个生态系统的稳定！" if lang == "中文" else "🍄 Protecting Jizong keeps the ecosystem in balance!")