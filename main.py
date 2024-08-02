import streamlit as st

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

    # Настройка меню с кнопками
    st.sidebar.title("Меню")
    menu_options = ["Обо мне", "Мой блог", "Проекты", "Навыки", "Образование", "Опыт работы"]

    for option in menu_options:
        if st.sidebar.button(option, key=option):
            st.session_state.page = option
            st.session_state.selected_article = None
            st.rerun()

    # Отображение содержимого в зависимости от выбранной страницы
    if st.session_state.page == "Обо мне":
        show_about_me()
    elif st.session_state.page == "Мой блог":
        show_blog()
    elif st.session_state.page == "Проекты":
        show_project()
    elif st.session_state.page == "Навыки":
        show_skills()
    elif st.session_state.page == "Образование":
        show_education()
    elif st.session_state.page == "Опыт работы":
        show_experience()

    # Добавление строчки о правах
    st.markdown('''
    ---
    © 2024 Кулаков Антон. Все права защищены.
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "Обо мне"

    if st.session_state.page == "article":
        show_full_article()
    else:
        main()
