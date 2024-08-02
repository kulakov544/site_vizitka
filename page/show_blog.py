import streamlit as st

# Структура данных для хранения информации о статьях
articles = [
    {
        "title": "Статья 1",
        "description": "Краткое описание статьи 1.dfghfgdh",
        "full_text": "Полный ddddddтекст статьи 1.xcvbgfcxhb"
    },
    {
        "title": "Статья 2",
        "description": "Краткое ddddddописание статьи 2.xgdhbfgd",
        "full_text": "Полный текст статьи 2.fdghfdgh"
    }
]

def show_blog():
    st.header("Мой блог")
    for index, article in enumerate(articles):
        st.subheader(article["title"])
        st.write(article["description"])
        button_key = f"read_more_{index}"
        if st.button("Читать дальше", key=button_key):
            st.session_state.page = "article"
            st.session_state.selected_article = article
            st.rerun()

def show_full_article():
    if 'selected_article' in st.session_state:
        article = st.session_state.selected_article
        st.sidebar.title("Меню")
        menu_options = ["Обо мне", "Мой блог", "Проекты", "Навыки", "Образование", "Опыт работы"]

        for option in menu_options:
            if st.sidebar.button(option, key=option):
                st.session_state.page = option
                st.session_state.selected_article = None
                st.rerun()

        st.title(article["title"])
        st.write(article["full_text"])
        if st.button("Назад", key="back_button"):
            st.session_state.page = "Мой блог"
            del st.session_state.selected_article
            st.rerun()
