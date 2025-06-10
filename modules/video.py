import streamlit as st
import os

def render(lang="中文"):
    st.title("🎬 教学视频" if lang == "中文" else "🎬 Teaching Video")

    if lang == "中文":
        st.markdown("请观看以下教学视频，了解课程核心内容：")
        st.video("https://www.bilibili.com/video/BV13cTkzMEYS/?spm_id_from=333.1387.homepage.video_card.click&vd_source=698c8c973ffab4c7118a2b70fabace67")
    else:
        st.markdown("Watch the following teaching video to understand the course content:")
        st.video("https://www.bilibili.com/video/BV1XzTkz3EuB/?spm_id_from=333.1387.upload.video_card.click&vd_source=698c8c973ffab4c7118a2b70fabace67")