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

def render(lang="中文"):
    st.title("🌱 生态系统与保护" if lang == "中文" else "🌱 Ecosystem & Conservation")
    st.markdown("---")

    # 一、鸡枞菌的生态特点
    st.subheader("🌿 鸡枞的自然生态" if lang == "中文" else "🌿 Natural Ecology of Jizong")
    if lang == "中文":
        st.markdown("""
鸡枞菌对环境要求极高，必须在特定的生态条件下才能自然生长，目前尚无成熟的人工种植方法。

鸡枞与白蚁共生，在白蚁垒筑的“蚁穴”中生长，依赖微生物、温湿度、土壤等多个因素共同作用，是典型的生态系统“合作产物”。
        """)
    else:
        st.markdown("""
Jizong mushrooms grow only in specific ecological conditions and have not yet been successfully cultivated artificially.

They exist in symbiosis with termites, growing on “fungus combs” built by termite colonies. Their survival depends on a complex mix of microbes, temperature, humidity, and soil — a perfect example of ecological cooperation.
        """)

    st.image("assets/images/shengtai.png", use_column_width=False, width=500)

    st.markdown("---")

    # 二、保护性采摘原则
    st.subheader("🧺 保护性采摘方法" if lang == "中文" else "🧺 Sustainable Harvesting Techniques")
    if lang == "中文":
        st.markdown("""
为了让鸡枞菌群持续繁衍，采摘时需注意以下几点：

- 不破坏菌丝和周围生态  
- 只采摘成熟的菌盖与菌柄  
- 保留菌丝，以便再次繁殖  
- 用竹篓等透气容器装载  
        """)
    else:
        st.markdown("""
To allow continuous reproduction of Jizong mushrooms, harvesters should follow these guidelines:

- Do not damage the underground mycelium or surrounding habitat  
- Only pick fully matured caps  
- Leave the fungus base in place to enable regrowth  
- Use breathable containers like bamboo baskets  
        """)

    st.image("assets/images/baohu1.png", width=350)
    st.image("assets/images/baohu2.png", width=350)
    st.image("assets/images/baohu3.png", width=350)

    st.markdown("---")

    # 三、互动小游戏
    st.subheader("🎮 模拟鸡枞采摘" if lang == "中文" else "🎮 Simulated Jizong Harvest Game")
    st.markdown("选择下列蘑菇中你会采摘的项，保持生态平衡！" if lang == "中文" else "Choose which mushrooms you would pick while keeping the ecosystem balanced!")

    mushrooms = [
        {"img": "mature jizong.PNG", "name_cn": "成熟鸡枞菌", "name_en": " Mature Jizong", "pickable": True},
        {"img": "unmature jizong.PNG", "name_cn": " 未成熟菌", "name_en": " Immature Mushroom", "pickable": False},
        {"img": "junsi.PNG", "name_cn": " 菌丝", "name_en": " Mycelium", "pickable": False},
        {"img": "gankujizong.PNG", "name_cn": " 干枯鸡枞", "name_en": " Dried-out Jizong", "pickable": False},
    ]

    if "eco_score" not in st.session_state:
        st.session_state.eco_score = 0

    correct, wrong = [], []
    cols = st.columns(len(mushrooms))

    for i, m in enumerate(mushrooms):
        with cols[i]:
            # 使用 HTML 保持图像比例一致
            image_path = f"assets/images/{m['img']}"
            st.markdown(f"""
                <div style="text-align:center">
                    <img src="data:image/png;base64,{base64.b64encode(open(image_path, 'rb').read()).decode()}" 
                         style="height:160px; object-fit:contain; margin-bottom:8px;" />
                </div>
            """, unsafe_allow_html=True)
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
        if lang == "中文":
            st.info(f"✅ 正确选择：{', '.join(correct) if correct else '无'}")
            st.info(f"❌ 错误选择：{', '.join(wrong) if wrong else '无'}")
        else:
            st.info(f"✅ Correct Picks: {', '.join(correct) if correct else 'None'}")
            st.info(f"❌ Wrong Picks: {', '.join(wrong) if wrong else 'None'}")

    if st.session_state.eco_score >= 1:
        st.success("🌍 恭喜你完成了生态采摘任务！" if lang == "中文" else "🌍 Well done! You’ve completed the eco-friendly harvest.")

    # 四、鸡枞经济与生态保护
    st.subheader("📈 鸡枞经济与生态数据" if lang == "中文" else "📈 Jizong Economy & Ecological Data")
    if lang == "中文":
        st.markdown("""
鸡枞菌在云南形成了重要的“山货经济”，农民通过晒干、炸制等加工形式销售至城市市场：

- 中国约70%的野生食用菌资源分布在云南  
- 鸡枞出口带来山区收入  
- 鸡枞保护关系到白蚁、森林与菌类生态系统的平衡  
        """)
    else:
        st.markdown("""
Jizong mushrooms support a mountain economy in Yunnan where farmers dry or fry them and sell to cities:

- About 70% of China’s wild mushrooms come from Yunnan  
- Export of Jizong benefits rural income  
- Conservation supports balance among termites, forests, and fungi  
        """)

    st.markdown("---")

        # 五、生态链图示任务
    st.subheader("🖼 生态关系图示" if lang == "中文" else "🖼 Ecological Poster Task")

    if lang == "中文":
        st.markdown("""
鸡枞菌的生长依赖一个完整的生态系统，包含森林、白蚁、蚁穴与微生物。  
森林提供湿润的环境和丰富的腐殖质；  
白蚁在地下构筑蚁穴，并种植“菌丝”作为食物；  
鸡枞菌正是在这些菌丝上与白蚁共生生长；  
人类采摘鸡枞时，如果能遵循生态保护原则，就能让这条生态链持续运作。  

生态链：**森林 → 白蚁 → 蚁穴 → 鸡枞 → 人类**
        """)
    else:
        st.markdown("""
The growth of Jizong mushrooms depends on an interconnected ecosystem involving forests, termites, termite nests, and microbes.  
Forests provide moisture and organic matter;  
Termites build underground nests and cultivate fungus as food;  
Jizong mushrooms grow in symbiosis on these fungus combs;  
Humans can sustainably harvest mushrooms while preserving this ecological cycle.  

Ecological Chain: **Forest → Termite → Termite Nest → Jizong → Human**
        """)

    st.image("assets/images/shengtai5.PNG", width=500)

    st.info("🍄 鸡枞的保护，关系整个生态系统的稳定！" if lang == "中文" else "🍄 Protecting Jizong means maintaining the entire ecosystem!")