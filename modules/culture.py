# modules/culture.py

import streamlit as st

def render(lang="中文"):
    st.title("🎎 非遗文化与故事" if lang == "中文" else "🎎 Intangible Heritage & Stories")
    st.markdown("---")

    # 一、民间传说与鸡枞的“灵性”
    st.subheader("🌩 鸡枞与雷雨的传说" if lang == "中文" else "🌩 Jizong and Thunderstorm Legends")
    if lang == "中文":
        st.markdown("""
云南民间广泛流传“鸡枞跑雷出”的说法，意为每逢雷雨天气，鸡枞菌就会迅速破土而出，象征自然界的神秘与灵性。

云南楚雄南华地区的《南华四季歌》中唱道：“三伏雷雨来，鸡枞冒山开。”这些民歌和传说展现了人们对季节节律的细致观察与尊重。

鸡枞中最被推崇的是“鸡枞胆”，即最早破土、质地最紧实、风味最浓的部分，被视为“菌中神话”。挖到鸡枞胆，被认为是运气极好的象征。
        """)
    else:
        st.markdown("""
In Yunnan folklore, it is said that “Jizong mushrooms spring up with thunder,” suggesting that thunderstorms awaken these mushrooms from the soil, symbolizing nature’s vitality and mystery.

A line from the folk song *Four Seasons in Nanhua* reads: “When midsummer storms arrive, Jizong mushrooms bloom across the hills.” Such expressions reflect people’s close observation and reverence for seasonal cycles.

The most prized part is the *Jizong gall*, the earliest and firmest mushroom bud. Discovering one is seen as a stroke of great fortune.
        """)

    st.markdown("---")

    # 二、民谣与谚语
    st.subheader("🎶 鸡枞谚语与双语表达" if lang == "中文" else "🎶 Jizong Proverbs & Bilingual Expressions")
    if lang == "中文":
        st.markdown("""
传统民谣中常以鸡枞菌为象征，表达自然与丰收的联系：

> 鸡枞跑雷出，兴旺伴丰收。  
> **Jizong springs with thunder, harvest brings joy and wonder.**

这类谚语朗朗上口，便于记忆，也体现了自然生态与人类生产之间的紧密联系。
        """)
    else:
        st.markdown("""
In traditional proverbs, Jizong mushrooms often symbolize the bond between nature and prosperity:

> **Jizong springs with thunder, harvest brings joy and wonder.**  
> (Original Chinese: 鸡枞跑雷出，兴旺伴丰收)

Such proverbs are rhythmic and memorable, reflecting the intimate relationship between natural rhythms and agricultural life.
        """)

    st.markdown("---")

    # 三、故事讲述与记录
    st.subheader("📜 民间记忆与口述传统" if lang == "中文" else "📜 Oral Traditions and Elders’ Memories")
    if lang == "中文":
        st.markdown("""
许多少数民族长者保留着与鸡枞相关的童年回忆与民歌。例如，有长者回忆说：

> “十五岁那年，雷雨刚过，我在后山第一次挖到了鸡枞胆。”

这些口述历史可以通过采访记录下来，双语整理后作为文化素材传承。
        """)
    else:
        st.markdown("""
Many elders from ethnic communities still recall childhood memories of foraging Jizong and singing folk songs. One elder recalls:

> “When I was 15, just after a storm, I found my first Jizong gall behind the mountain.”

These oral accounts can be collected and documented bilingually as valuable materials for cultural preservation.
        """)

    st.markdown("---")

    # 四、火把节与鸡枞季节
    st.subheader("🔥 火把节与鸡枞时节" if lang == "中文" else "🔥 Torch Festival & Mushroom Season")
    if lang == "中文":
        st.markdown("""
鸡枞菌的最佳采摘期通常在每年农历六月，恰逢彝族等民族的传统节日——火把节。节日期间，当地举办火把游行、赛歌会、民族集市等活动。

鸡枞成为这一节庆中的重要食材，市场热闹非凡，展示出自然资源与节日文化的紧密结合。
        """)
    else:
        st.markdown("""
The prime harvesting season for Jizong mushrooms usually falls in the sixth lunar month, which coincides with the Yi ethnic group's traditional celebration — the Torch Festival.

This festival features torch parades, singing competitions, and bustling markets, where Jizong mushrooms are a key seasonal delicacy, illustrating the strong bond between ecological resources and festive traditions.
        """)

    st.markdown("---")
    st.info("🍄 鸡枞不仅是一种美味，更是民族文化的承载体。" if lang == "中文" else "🍄 Jizong is not just a delicacy — it’s a bearer of cultural heritage.")