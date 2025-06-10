import streamlit as st

def render(lang="中文"):
    st.title("🎥 教学视频" if lang == "中文" else "🎥 Teaching Video")
    st.markdown("---")

    if lang == "中文":
        st.subheader("📺 鸡枞菌课程全程视频（中文）")
        bilibili_embed_code = """
        <div style="text-align:center;">
            <iframe src="https://player.bilibili.com/player.html?bvid=BV13cTkzMEYS&autoplay=0"
                    scrolling="no"
                    border="0"
                    frameborder="no"
                    framespacing="0"
                    allowfullscreen="true"
                    style="width: 50%; height: 315px;">
            </iframe>
        </div>
        """
        st.components.v1.html(bilibili_embed_code, height=350)

    else:
        st.subheader("📺 Jizong Teaching Video (English Version)")
        bilibili_embed_code = """
        <div style="text-align:center;">
            <iframe src="https://player.bilibili.com/player.html?bvid=BV1XzTkz3EuB&autoplay=0"
                    scrolling="no"
                    border="0"
                    frameborder="no"
                    framespacing="0"
                    allowfullscreen="true"
                    style="width: 50%; height: 315px;">
            </iframe>
        </div>
        """
        st.components.v1.html(bilibili_embed_code, height=350)