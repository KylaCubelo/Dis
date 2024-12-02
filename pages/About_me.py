import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Overthinking Out Loud",
    page_icon="📜",
)

img=Image.open('./assets/Ky.png')

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(img, width=230)

with col2:
    st.title('Kyla Cubelo', anchor=False)
    st.write('Surigao State University, Bachelor of Science in Computer Engineering, a 2nd Year Student')


st.write("\n\n")
st.subheader("Short Discription About me:")
st.write(
    """
I’m Kyla, a 20-year-old Computer Engineering student in my 2nd year, driven by a passion for coding and solving complex problems. I’ve honed my programming skills and enjoy not only creating innovative solutions but also mentoring others and contributing to impactful projects.

Outside of my professional journey, I’m equal parts dreamer and doer. I love playing volleyball, journaling, exploring cute bookstores, and baking cookies (even if they don’t always turn out perfect!). You’ll often find me embracing spontaneous road trips, long coffee dates, and deep late-night conversations.

Life, to me, is a blend of chasing big dreams and finding joy in everyday moments. Whether it’s conquering my career goals or cherishing little adventures, I aim to make a positive impact in my community and stay curious about all the possibilities the world has to offer. 💕    """
)

st.sidebar.success("Select pages above")