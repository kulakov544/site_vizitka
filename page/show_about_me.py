import streamlit as st
from PIL import Image


def show_about_me():
    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open('file/photo.jpg')
        st.image(image, caption='Кулаков Антон', width=250)

    with col2:
        st.title("Резюме Кулаков Антон")
        st.subheader("Начинающий программист Python")

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
    Моя цель — развиваться в области программирования. Занимаюсь разработкой pet-проектов на Python.

    Готовые проекты:
    1. Телеграмм-бот, который находит артикулы деталей для ТО автомобилей.
    2. Сайт-визитка написанный на streamlit.
    3. Создание dwh.
        - Построил базу DWH на PostgreSQL.
        - Получил данные о вакансиях с сайта hh.ru
        - Провел первичную обработка данных для загрузки в базу.
        - Загрузил данные в Stage слой DWH.
        - Трансформировал данные для укладки на долговременное хранение.
        - Заполнил справочники и таблицу вакансий в Core слое DWH, с сохранением обновленных записей в таблицу истории.
        - Оркестрация процесса через Prefect.
        - Сделал View и материализацию таблиц в DataMart слое DWH.
        - По данным из DataMart построил дашборды в Yandex Data Lens и Power BI.

    Подробные схемы есть в портфолио и на сайте.

    Все проекты доступны на моем GitHub:
    https://github.com/kulakov544

    Также провел настройку инфраструктуры, подробности можно увидеть по следующей ссылке: 
    [Инфраструктура](https://disk.yandex.ru/i/2V6WNHQszEwMgw)
    """)
