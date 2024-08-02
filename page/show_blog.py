import streamlit as st
from PIL import Image


# Структура данных для хранения информации о статьях
articles = [
    {
        "title": "Статья 1",
        "description": "Краткое описание статьи 1.",
        "full_text": "Полный текст статьи 1."
    },
    {
        "title": "Статья 2",
        "description": "Краткое описание статьи 2.",
        "full_text": "Полный текст статьи 2."
    }
]


def show_blog():
    st.header("Мой блог")
    for index, article in enumerate(articles):
        st.subheader(article["title"])
        st.write(article["description"])
        button_key = f"read_more_{index}"
        if st.button(f"Читать дальше - {article['title']}", key=button_key):
            st.session_state.page = "article"
            st.session_state.selected_article = article
            st.experimental_rerun()


def show_full_article():
    if 'selected_article' in st.session_state:
        article = st.session_state.selected_article
        st.title(article["title"])
        st.write(article["full_text"])
        if st.button("Назад", key="back_button"):
            st.session_state.page = "blog"
            del st.session_state.selected_article
            st.experimental_rerun()
