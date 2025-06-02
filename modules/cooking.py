# modules/cooking.py

import streamlit as st

def render(lang="中文"):
    st.title("🍳 传统烹饪与饮食文化" if lang == "中文" else "🍳 Culinary & Dietary Culture")
    st.markdown("---")

    # 一、鸡枞菌的美味与传统
    if lang == "中文":
        st.markdown("""
鸡枞菌肉质厚实、味鲜香脆，被誉为“菌中之冠”。明清典籍中多次记载其独特美味，尤其是以菜籽油炸制的“油鸡枞”最为经典。传统做法包括将干鸡枞炸至酥香制成鸡枞油，或与辣椒、蔬菜等搭配翻炒。
        """)
    else:
        st.markdown("""
Jizong mushrooms are meaty, flavorful, and crispy, earning the title “King of Mushrooms.” Ancient Chinese texts from the Ming and Qing dynasties praise their unique taste. The classic dish “You Jizong” (Jizong fried in rapeseed oil) remains a signature way to enjoy them. Traditional cooking includes dry-frying, deep-frying to make mushroom oil, or stir-frying with vegetables and chili.
        """)

    st.image("assets/images/jizongcook.jpg", caption="传统鸡枞油制作 | Traditional Fried Jizong in Oil", width=500)

    st.markdown("---")

    # 二、教学视频：油炸鸡枞
    st.subheader("🎥 教学微视频：如何炸鸡枞" if lang == "中文" else "🎥 Instructional Video: How to Fry Jizong")

    # 嵌入 Bilibili 视频（BV 号）
    bilibili_url = "https://player.bilibili.com/player.html?bvid=BV1vj7rzeETP&autoplay=0"
    st.components.v1.html(f"""
        <iframe src="{bilibili_url}" 
                scrolling="no" 
                border="0" 
                frameborder="no" 
                framespacing="0" 
                allowfullscreen="true" 
                style="width: 50%; height: 400px;">
        </iframe>
    """, height=420)

    st.markdown("---")

    # 三、营养与药用价值
    st.subheader("🧬 鸡枞的营养与药用价值" if lang == "中文" else "🧬 Nutritional & Medicinal Value")

    if lang == "中文":
        st.markdown("""
据《本草纲目》记载，鸡枞菌“益胃清神”。现代研究表明，其含有多种氨基酸和多糖成分，有助于增强免疫力、滋补脾胃。
        """)
    else:
        st.markdown("""
According to *Compendium of Materia Medica*, Jizong is said to "nourish the stomach and calm the mind." Modern studies show it contains amino acids and polysaccharides that help enhance immunity and support digestion.
        """)

    st.markdown("---")
    st.info("🍄 学做鸡枞菜，体会民族味道！" if lang == "中文" else "🍄 Learn to cook Jizong and experience ethnic flavors!")