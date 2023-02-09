import streamlit as st

# 设置E的大小
st.slider("大小", min_value=10, max_value=100, value=20, step=10)

# 设置E的方向
st.selectbox("方向", options=["正向", "反向"])

# 生成E的图片
img = "<style>img{width:100px; height:100px;}</style><img src='https://via.placeholder.com/100x100.png'>"

# 将E的图片显示在streamlit上
st.write(img, unsafe_allow_html=True)
