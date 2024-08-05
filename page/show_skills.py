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
            - <img src="https://img.icons8.com/color/48/000000/git.png" width="24"/> GIT
            - <img src="https://cdn.hackersandslackers.com/2020/08/sqlalchemy2.png" width="24"/> SQLAlchemy
            - <img src="https://img.icons8.com/color/48/000000/pandas.png" width="24"/> Pandas
            - <i class="fas fa-robot"></i> telebot
            - <img src="https://img.icons8.com/color/48/000000/python.png" width="24"/> Requests
            - <img src="https://global.discourse-cdn.com/business7/uploads/prefecthq/original/2X/4/4551612629fb3d641edb1263395b39fac2ef04ca.svg" width="24"/> Prefect

            ### Работа с базами данных ###
            - <img src="https://img.icons8.com/color/48/000000/sql.png" width="24"/> SQL       
            - <img src="https://cdn.iconscout.com/icon/free/png-256/free-postgresql-8-1175119.png?f=webp" width="24"/> PostgreSQL
            - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DBeaver_logo.svg/1200px-DBeaver_logo.svg.png" width="24"/> DBeaver
            - <img src="https://odbcmanager.net/images/icon256.gif" width="24"/> ODBC

            ### Деплой ###
            - <img src="https://img.icons8.com/color/48/000000/docker.png" width="24"/> Docker
            - <img src="https://img.icons8.com/color/48/000000/filezilla.png" width="24"/> FileZilla
            - <img src="https://research.reading.ac.uk/act/wp-content/uploads/sites/2/Unorganized/ssh.png" width="24"/> SSH

            ### Веб-серверы и сети ###
            - <img src="https://img.icons8.com/color/48/000000/nginx.png" width="24"/> Nginx
            - <img src="https://img.icons8.com/color/48/000000/shield.png" width="24"/> WireGuard
            - <img src="https://img.icons8.com/color/48/000000/remote-desktop.png" width="24"/> RDP

            ### Инструменты для разработки и тестирования ###
            - <img src="https://img.icons8.com/color/48/000000/pycharm.png" width="24"/> Pycharm
            - <img src="https://cdn.iconscout.com/icon/free/png-256/free-postman-3521648-2945092.png?f=webp&w=256" width="24"/> Postman
            - <img src="https://static-00.iconduck.com/assets.00/window-dev-tools-icon-2048x1903-h6vcfy5j.png" width="24"/> DevTools
            - <img src="https://static-00.iconduck.com/assets.00/file-type-drawio-icon-2048x2048-dxjfklgq.png" width="24"/> Draw.io

            ### Визуализация данных и отчеты ###
            - <img src="https://img.icons8.com/color/48/000000/power-bi.png" width="24"/> Power BI
            - <img src="https://336118.selcdn.ru/Gutsy-Culebra/products/Yandex-DataLens-Logo.png" width="24"/> Yandex DataLens

            ### Другое ###
            - <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Logo_Yandex.Tracker_2018.svg/1200px-Logo_Yandex.Tracker_2018.svg.png" width="24"/> Yandex Tracker
            - <img src="https://img.icons8.com/color/48/000000/ubuntu.png" width="24"/> Ubuntu
            - <img src="https://img.icons8.com/color/48/000000/windows-10.png" width="24"/> Windows 10
            """, unsafe_allow_html=True)

