import streamlit as st
from PIL import Image

from page.show_about_me import show_about_me
from page.show_blog import show_blog, show_full_article
from page.show_project import show_project
from page.show_skills import show_skills
from page.show_experience import show_experience
from page.show_education import show_education


def main():
    st.set_page_config(
        page_title="Резюме Кулаков Антон",
        page_icon=":briefcase:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Настройка меню
    st.sidebar.title("Меню")
    selection = st.sidebar.radio("Перейти к", ["Обо мне", "Мой блог", "Проекты", "Навыки", "Образование", "Опыт работы"], label_visibility='collapsed')

    if selection == "Обо мне":
        show_about_me()
    elif selection == "Мой блог":
        st.session_state.page = "blog"
        show_blog()
    elif selection == "Проекты":
        show_project()
    elif selection == "Навыки":
        show_skills()
    elif selection == "Образование":
        show_education()
    elif selection == "Опыт работы":
        show_experience()


if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "blog"

    if st.session_state.page == "article":
        show_full_article()
    else:
        main()
