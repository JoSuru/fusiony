import streamlit as st

st.set_page_config("FusionY", "🖼️", layout="wide")


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(spec=[1.5, 5, 5])

with col1:
    with st.expander('Nested Expander 1', expanded=True):
        st.markdown('Some More Stuff Here')
with col2:
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col3:
    st.image("https://static.streamlit.io/examples/cat.jpg")
