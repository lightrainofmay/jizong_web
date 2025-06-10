import streamlit as st
from config import LANGUAGES, MENU
from modules import identify, cooking, culture, ecology, community, mushroom_info 

st.set_page_config(page_title="鸡枞菌互动网页", layout="wide")

# 初始化语言状态
if "lang" not in st.session_state:
    st.session_state.lang = LANGUAGES[0]

# 左侧栏语言选择
lang = st.sidebar.selectbox("选择语言 / Choose Language", LANGUAGES)
st.session_state.lang = lang

# 左侧栏导航菜单
page = st.sidebar.radio("导航 Navigation", list(MENU.keys()))
selected_page = MENU[page]

# 加载模块页面
if selected_page == "identify":
    identify.render(lang)
elif selected_page == "cooking":
    cooking.render(lang)
elif selected_page == "culture":
    culture.render(lang)
elif selected_page == "ecology":
    ecology.render(lang)
elif selected_page == "community":
    community.render(lang)
elif selected_page == "mushroom_info":  # ✅ 新增导航逻辑
    mushroom_info.render(lang)
else:
    col1, col2 = st.columns([3, 1])

    with col1:
        if lang == "中文":
            st.title("🐔🍄 鸡枞大冒险：一起识菌、采菌、做美食！")

            st.image("https://raw.githubusercontent.com/lightrainofmay/jizong_web/refs/heads/main/assets/images/home_cover.PNG", width=400)

            st.markdown("欢迎来到课程主页！请选择左侧菜单浏览各模块内容。")

            st.markdown("---")

            st.markdown("""
            <div style='font-size:14px; color: #555; line-height: 1.6;'>
                <strong>制作者：</strong> 杨晓萱，刘元婷，刘依依，陈媛清，夏柔，黄蕊<br>
                <strong>指导教师：</strong> 周晓宇
            </div>
            """, unsafe_allow_html=True)
        else:
            st.title("🐔🍄 JiZong Quest: Learn, Pick and Cook Mushrooms!")

            st.image("https://raw.githubusercontent.com/lightrainofmay/jizong_web/refs/heads/main/assets/images/home_cover.PNG", width=400)

            st.markdown("Welcome to the homepage! Please use the menu on the left to explore each module.")

            st.markdown("---")

            st.markdown("""
            <div style='font-size:14px; color: #555; line-height: 1.6;'>
                <strong>Created by:</strong> Yang Xiaoxuan, Liu Yuanting, Liu Yiyi, Chen Yuanqing, Xia Rou, Huang Rui<br>
                <strong>Instructor:</strong> Zhou Xiaoyu
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: right; line-height: 1.2;'>
            <span style='font-size:18px; font-weight:600;'>楚雄师范学院语言文化学院</span><br>
            <span style='font-size:16px; font-style: italic; color:#444;'>CXNU School of Language and Culture</span><br>
            <span style='font-size:16px; color:gray;'>笃学尚行  扬美崇善</span>
        </div>
        """, unsafe_allow_html=True)