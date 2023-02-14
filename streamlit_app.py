import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

# st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Rakesh Shaw, Open-Source Enthusiast')

st.info('👋Upcoming Dev👋, \n Success requires persistent practice, guided by patience.')

icon_size = 20

st_button('resume','https://drive.google.com/file/d/1aBuysfNWHlq4BqacD-DVKsfDqglh6Drl/view?usp=share_link', 'View my Resume', icon_size)
st_button('github', 'https://github.com/dev-rakeshshaw', 'Follow me on Github', icon_size)
st_button('twitter', 'https://twitter.com/dev_rakeshshaw', 'Follow me on Twitter', icon_size)
st_button('telegram', 'https://t.me/dev_rakeshshaw', 'Chat with me on Telegram', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/rakesh-shaw-937514263/', 'Connect with me on LinkedIn', icon_size)



