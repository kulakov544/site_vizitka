import streamlit as st
from PIL import Image


def show_about_me():
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open('file/photo.jpg')
        st.image(image, caption='Кулаков Антон', width=250)

    with col2:
        st.title("Резюме Кулаков Антон")
        st.subheader("Программист Python")

        st.write("[GitHub](https://github.com/kulakov544)")
        st.write("[HeadHunter](https://krasnodar.hh.ru/resume/2682750cff0b90d32e0039ed1f645858514e45)")

        with open("file/Kulakov.pdf", "rb") as file:
            st.download_button(
                label="Скачать резюме",
                data=file,
                file_name="file/Kulakov.pdf",
                mime="application/pdf"
            )

    st.header("Обо мне")
    st.write("""
    Я преподаватель информатики с опытом работы в институте. В данный момент перехожу в область разработки приложений.   
    Моя цель — развиваться в области программирования.  
    Ищу работу в области бекенд-разработки на python, разработки DWH, тестирования, дата инженера.  
    
    Проекты, которые я реализовал, можно посмотреть в разделе проекты или на моем GitHub:
    https://github.com/kulakov544
    """)
