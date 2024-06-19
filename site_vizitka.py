from pathlib import Path
import streamlit as st
from PIL import Image


#---PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"GIT.pdf"
profile_pic = current_dir/"assets"/"profile_pic.jpg"


#Основные настройки
page_title = "Кулаков Антон"
page_icon = ":wave:"
name = "Кулаков Антон"
description = """Программист Python"""
email = "kulakov_3000@mail.ru"
social_media = {
    "GitHub": "https://github.com/WebEzhik"
}
projects = {
    "Мой проект": "ссылка на этот проект"
}


st.set_page_config(page_title = page_title, page_icon = page_icon)

#st.title("Hello world!")

#загрузка стилей и пдф и фото профиля
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    pdf_bite = pdf_file.read()
profile_pic = Image.open(profile_pic)

#Первая секция сайта
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Резюме",
        data = pdf_bite,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("", email)

#Социальные сети
st.write("#")
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

#Блок достижений
st.write("#")
st.subheader("Достижения:")
st.write(
    '''
    -То чего я достиг.
    '''
)

#Блок навыков
st.write("#")
st.subheader("Навыки:")
st.write(
    '''
    -То что я умею.
    '''
)
