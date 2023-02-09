import streamlit as st

def main():
    st.title("E Letter Transformation")
    size = st.slider("Select the size of the letter E", min_value=10, max_value=100, value=20, step=1)
    orientation = st.radio("Select the orientation of the letter E", ('Horizontal', 'Vertical'))
    color = st.selectbox("Select the color of the letter E", ('Red', 'Green', 'Blue'))

    if orientation == 'Horizontal':
        if color == 'Red':
            st.write("<span style='color:red; font-size:{}px'>E</span>".format(size),unsafe_allow_html=True)
        elif color == 'Green':
            st.write("<span style='color:green; font-size:{}px'>E</span>".format(size),unsafe_allow_html=True)
        elif color == 'Blue':
            st.write("<span style='color:blue; font-size:{}px'>E</span>".format(size),unsafe_allow_html=True)
    elif orientation == 'Vertical':
        if color == 'Red':
            st.write("<div style='writing-mode: vertical-lr; color:red; font-size:{}px'>E</div>".format(size),unsafe_allow_html=True)
        elif color == 'Green':
            st.write("<div style='writing-mode: vertical-lr; color:green; font-size:{}px'>E</div>".format(size),unsafe_allow_html=True)
        elif color == 'Blue':
            st.write("<div style='writing-mode: vertical-lr; color:blue; font-size:{}px'>E</div>".format(size),unsafe_allow_html=True)

if __name__ == '__main__':
    main()
