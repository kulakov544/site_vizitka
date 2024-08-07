import streamlit as st
from PIL import Image


def show_skills():
    st.header("Навыки")
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)

    st.markdown("""
            ### Программирование и библиотеки Python ###
            - <img src="https://img.icons8.com/color/48/000000/python.png" width="24"/> Python
                - Язык программирования на котором я пишу все свои проекты.
            - <img src="https://img.icons8.com/color/48/000000/git.png" width="24"/> GIT
                - Система контроля версий. Позволяет создавать точки сохранения кода и возвращатся к ним. 
                Работать командой над одним кодом, создавая ветки и сливая их с основным кодом.
            - <img src="https://cdn.hackersandslackers.com/2020/08/sqlalchemy2.png" width="24"/> SQLAlchemy
                - Библиотека для работы с базой данных.
            - <img src="https://img.icons8.com/color/48/000000/pandas.png" width="24"/> Pandas
                - Библиотека для обработки и анализа данных.
            - <i class="fas fa-robot"></i> telebot
                - Библиотека для создания телеграмм-ботов.
            - <img src="https://img.icons8.com/color/48/000000/python.png" width="24"/> Requests
                - Библиотека позволяющая работать со всеми видами запросов к серверу.
            - <img src="https://global.discourse-cdn.com/business7/uploads/prefecthq/original/2X/4/4551612629fb3d641edb1263395b39fac2ef04ca.svg" width="24"/> Prefect
                - Оркестратор. Позволяет автоматизировать запуск программ и контроль работы.

            ### Работа с базами данных ###
            - <img src="https://cdn-icons-png.flaticon.com/512/4299/4299956.png" width="24"/> SQL 
                - Язык для написания запросов к базе данных.      
            - <img src="https://cdn.iconscout.com/icon/free/png-256/free-postgresql-8-1175119.png?f=webp" width="24"/> PostgreSQL
                - База данных которой я пользуюсь.
            - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DBeaver_logo.svg/1200px-DBeaver_logo.svg.png" width="24"/> DBeaver
                - Удобное приложение для работы с базой данных.
            - <img src="https://odbcmanager.net/images/icon256.gif" width="24"/> ODBC
                - Драйвер для создания подключения к базе данных в Windows.

            ### Деплой ###
            - <img src="https://img.icons8.com/color/48/000000/docker.png" width="24"/> Docker
                - Программа для деплоя приложений с контейнеризацией.
            - <img src="https://img.icons8.com/color/48/000000/filezilla.png" width="24"/> FileZilla
                - Программа для FTP подключения к серверу.
            - <img src="https://research.reading.ac.uk/act/wp-content/uploads/sites/2/Unorganized/ssh.png" width="24"/> SSH
                - Подключение к командной строке удаленного сервера.

            ### Веб-серверы и сети ###
            - <img src="https://img.icons8.com/color/48/000000/nginx.png" width="24"/> Nginx
                - Прокси-сервер позволяющий настроить доступ к приложениям и страницам на сервере по доменным именам.
            - <img src="https://img.icons8.com/color/48/000000/shield.png" width="24"/> WireGuard
                - Протокол на котором построена моя домашняя VPN сеть.
            - <img src="https://img.icons8.com/color/48/000000/remote-desktop.png" width="24"/> RDP
                - Подключение к удаленному рабочему столу Windows. В моем случае это домашний сервер.

            ### Инструменты для разработки и тестирования ###
            - <img src="https://img.icons8.com/color/48/000000/pycharm.png" width="24"/> Pycharm
                - Мощьное IDE которым я пользуюсь.
            - <img src="https://cdn.iconscout.com/icon/free/png-256/free-postman-3521648-2945092.png?f=webp&w=256" width="24"/> Postman
                - Программа для тестирования API. Так же удобно когда нужно делать одиночные запросы и ответы.
            - <img src="https://static-00.iconduck.com/assets.00/window-dev-tools-icon-2048x1903-h6vcfy5j.png" width="24"/> DevTools
                - Инструмент для работы с кодами веб-страниц. 
            - <img src="https://static-00.iconduck.com/assets.00/file-type-drawio-icon-2048x2048-dxjfklgq.png" width="24"/> Draw.io
                - Приложение для рисования схем.

            ### Визуализация данных и отчеты ###
            - <img src="https://1000logos.net/wp-content/uploads/2022/08/Microsoft-Power-BI-Logo.png" width="24"/> Power BI
            - <img src="https://336118.selcdn.ru/Gutsy-Culebra/products/Yandex-DataLens-Logo.png" width="24"/> Yandex DataLens

            ### Другое ###
            - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Logo_Yandex.Tracker_2018.svg/1200px-Logo_Yandex.Tracker_2018.svg.png" width="24"/> Yandex Tracker
                - Сервис для управления проектами и контроля выполнения задач. Активно пользуюсь Канбан доской данного сервиса.
            - <img src="https://img.icons8.com/color/48/000000/ubuntu.png" width="24"/> Ubuntu
                - Система достаточно часто встречающаяся на серверах как и другие linux системы. Как правило для настройки 
                сервера требуется знание командной строки этой операционной системы.
            - <img src="https://img.icons8.com/color/48/000000/windows-10.png" width="24"/> Windows 10
                - Операционная система на которой я работаю.
            """, unsafe_allow_html=True)

