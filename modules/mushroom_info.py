# modules/mushroom_info.py

import streamlit as st
import os

def render(lang="中文"):
    st.title("🍄 菌类知识科普" if lang == "中文" else "🍄 Mushroom Knowledge")
    st.markdown("---")

    # 一、什么是蘑菇？
    st.markdown("### 一、什么是蘑菇？（植物学与形态学基础）" if lang == "中文" else "### 1. What are Mushrooms? (Botany and Morphology)")

    if lang == "中文":
        st.markdown("""
蘑菇是某些真菌的子实体，属于真菌界。它们通过孢子繁殖，常见于潮湿、有机物丰富的土壤中。

**基本结构：**
- **菌盖（Cap）**：蘑菇上方的伞状结构。
- **菌褶（Gills）**：位于菌盖下方，释放孢子。
- **菌柄（Stipe）**：支持菌盖的“茎”。
- **菌环（Ring）和菌托（Volva）**：剧毒蘑菇常见的结构特征。
        """)
        image_path = "assets/images/mushroom_structure_ch.PNG"
    else:
        st.markdown("""
Mushrooms are the fruiting bodies of certain fungi, classified under the kingdom Fungi. They reproduce via spores and are commonly found in moist, organic-rich soil.

**Basic Structure:**
- **Cap**: The umbrella-shaped top of the mushroom.
- **Gills**: Located under the cap; they release spores.
- **Stipe (Stalk)**: The stem-like structure that supports the cap.
- **Ring and Volva**: Common features of highly poisonous mushrooms.
        """)
        image_path = "assets/images/mushroom_structure_en.PNG"

    if os.path.exists(image_path):
        st.image(image_path, width=500)
    else:
        st.warning("❗ 蘑菇结构图未找到")

    st.markdown("---")

    # 二、鸡枞
    st.markdown("### 二、鸡枞（Jizong）的形态特征和生态习性" if lang == "中文" else "### 2. Morphological and Ecological Traits of Jizong Mushroom")

    if lang == "中文":
        st.markdown("""
**形态特征：**
- 菌盖灰褐或黄褐，边缘略卷。
- 菌柄粗壮，坚实，无菌环和菌托。
- 菌褶白色或淡黄色。

**生态习性：**
- 与白蚁共生，生于白蚁窝附近。
- 仅在6月~9月雨季大量生长。
- 常见于云南等热带亚热带地区。

鸡枞味道鲜美，是极受欢迎的野生食用菌。
        """)
    else:
        st.markdown("""
**Morphological Traits:**
- Cap is grayish-brown or yellow-brown, slightly curled at the edges.
- Stipe is thick and firm, without a ring or volva.
- Gills are white or pale yellow.

**Ecological Traits:**
- Symbiotic with termites; usually grows near termite mounds.
- Grows abundantly only during the rainy season (June–September).
- Common in tropical and subtropical regions such as Yunnan, China.

Jizong mushrooms are highly prized for their delicious flavor.
        """)

    jizong_path = "assets/images/jizong.jpg"
    if os.path.exists(jizong_path):
        st.image(jizong_path, caption="鸡枞实图" if lang == "中文" else "Jizong Mushroom", width=360)
    else:
        st.warning("❗ 鸡枞图片未找到")

    st.markdown("---")

    # 三、与鸡枞混淆的毒蘑菇
    st.markdown("### 三、与鸡枞容易混淆的毒蘑菇" if lang == "中文" else "### 3. Toxic Mushrooms Easily Confused with Jizong")

    if lang == "中文":
        st.table([
            ["鹅膏菌（Amanita）", "✅ 剧毒", "有菌环和菌托，颜色白或淡黄"],
            ["铅绿褶菇（Entoloma sinuatum）", "✅ 有毒", "灰白菌盖，绿色菌褶"],
            ["毒伞菌（Lepiota）", "✅ 有毒", "白色菌盖带鳞片，柄细长"],
        ])
    else:
        st.table([
            ["Amanita", "✅ Deadly", "Has ring and volva; white or pale yellow color"],
            ["Entoloma sinuatum", "✅ Toxic", "Gray-white cap, greenish gills"],
            ["Lepiota", "✅ Toxic", "White scaly cap, thin long stalk"],
        ])

    # 插图1：铅绿褶菇
    qianlv_path = "assets/images/qianlvzhegu.jpg"
    if os.path.exists(qianlv_path):
        st.image(qianlv_path, caption="铅绿褶菇（有毒）" if lang == "中文" else "Entoloma sinuatum (Toxic)", width=320)

    # 插图2：毒伞菌
    dusan_path = "assets/images/dusanjun.jpg"
    if os.path.exists(dusan_path):
        st.image(dusan_path, caption="毒伞菌（有毒）" if lang == "中文" else "Lepiota (Toxic)", width=320)

    # 插图3：鹅膏菌
    egao_path = "assets/images/egaojun.jpg"
    if os.path.exists(egao_path):
        st.image(egao_path, caption="鹅膏菌（剧毒）" if lang == "中文" else "Amanita (Deadly)", width=320)

    st.markdown("**✅ 提醒：**" if lang == "中文" else "**✅ Caution:**")
    st.markdown(
        "- 鸡枞无“帽子、裙子、鞋子”（无菌盖花纹、菌环、菌托）。" if lang == "中文"
        else "- Jizong lacks the 'hat, skirt, and shoes' (no cap scales, ring, or volva)."
    )
    st.markdown(
        "- 不认识的蘑菇绝对不要采摘食用。" if lang == "中文"
        else "- Never pick or eat mushrooms you cannot confidently identify."
    )

    st.markdown("---")
    st.info("🍄 正确识菇，守护健康！" if lang == "中文" else "🍄 Identify mushrooms properly to protect your health!")