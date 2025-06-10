import streamlit as st
import os

def show_image_local(path, caption=None, width=300):
    if os.path.exists(path):
        st.image(path, caption=caption, width=width)
    else:
        st.warning(f"⚠️ 图像未找到: {path}")

def show_video_local(path):
    if os.path.exists(path):
        st.video(path)
    else:
        st.warning(f"⚠️ 视频未找到: {path}")

def render(lang="中文"):
    st.title("🎎 非遗文化与故事" if lang == "中文" else "🎎 Intangible Heritage & Stories")
    st.markdown("---")

    st.subheader("🍄 鸡枞菌的文化与记载" if lang == "中文" else "🍄 Cultural Legacy of Jizong Mushrooms")

    if lang == "中文":
        st.markdown("""
鸡枞菌为白蘑科植物鸡枞的子实体，是山珍中的珍品。其肉厚肥硕，质细丝白，味道鲜甜香脆，富含人体所需的蛋白质和多种维生素。

明代旅行家徐霞客在游历云南期间，曾在大理鸡足山、保山、凤庆、祥云等地多次品尝鸡枞，并在日记中详细记录了烹饪方式、味道体验以及鸡枞的干制和油炸方法。他对云南人将一朵鸡枞变着花样成菜深感惊讶，认为鸡枞可做干货便于远行，也可鲜食炖汤，是滇中佳品。
        """)
        show_image_local("assets/images/Xu-Xiake.jpg", caption="徐霞客画像（图片来自何创时云端博物馆）")

        st.markdown("""
鸡枞不仅是云南的美食象征，也被古人咏诗赞美。例如：

> 海上天风吹玉芝，樵童睡熟不曾知。  
> 仙翁住近华阳洞，分得琼英一两枝。  
> ——杨升庵（杨慎）
        """)
        show_video_local("assets/audio/shi1_ch.mp4")

        st.markdown("""
> 至味常无种，轮菌雪作肤。  
> 茎从新雨茁，香自晚春腴。  
> 鲜嫩头番秀，肥抽九节蒲。  
> 秋风菁菜客，食品列兹无。  
> ——清·贾杰《鸡枞》
        """)
        show_video_local("assets/audio/shi2_ch.mp4")

        show_image_local("assets/images/yangshen.jpg", caption="杨慎画像（图片来自维基百科）")

        st.markdown("这些诗句展示了鸡枞在中国传统文化中的独特地位。")
    else:
        st.markdown("""
Jizong mushroom, the fruiting body of a species from the Agaricaceae family, is a prized wild delicacy in China. Thick, tender, white-fibered, and rich in protein and vitamins, it is celebrated for its flavor and texture.

Ming Dynasty explorer Xu Xiake wrote about eating Jizong mushrooms in many parts of Yunnan — Dali, Baoshan, Fengqing, Xiangyun. He praised both fresh and dried preparations, noting how locals transformed a single mushroom into many dishes.
        """)
        show_image_local("assets/images/Xu-Xiake.jpg", caption="Portrait of Xu Xiake（Picture from HSC Online Museum）")

        st.markdown("""
Jizong is not only a culinary treasure but also a poetic symbol in Chinese literature. For example:

> *Heaven’s wind from the sea breathes on jade mushrooms;  
> The woodcutter naps, unaware of their bloom.  
> The immortal near Huayang Cave  
> Shares a branch of celestial essence.*  
> —Yang Shen, Ming Dynasty
        """)
        show_video_local("assets/audio/shi1_en.mp4")

        st.markdown("""
> *No need to sow this rarest taste,  
> Its snow-white cap a gift of spring.  
> It buds with rain, aromas rich,  
> And feeds the honored guest in fall.*  
> —Jia Jie, Qing Dynasty
        """)
        show_video_local("assets/audio/shi2_en.mp4")

        show_image_local("assets/images/yangshen.jpg", caption="Portrait of Yang Shen（From Wikipedia）")

        st.markdown("These verses reflect the reverence for Jizong mushrooms in classical Chinese culture.")

    st.markdown("---")
    st.info("🍄 鸡枞不仅是一种野生美味，更是中国诗意山林生活的象征。" if lang == "中文" else "🍄 Jizong is not just a delicacy — it symbolizes a poetic life in the mountains of China.")