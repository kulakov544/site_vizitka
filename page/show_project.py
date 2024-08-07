import streamlit as st
from PIL import Image


def show_project():
    st.header("Проекты")

    with st.expander("Проект: Телеграмм бот для получения артикулов деталей с сайта"):
        st.markdown("""
        ## О проекте
Телеграмм бот получает VIN номер автомобиля от пользователя. Ищет по нему информацию об автомобиле на сайте AutoDoc.ru. 
Выдает пользователю информацию об автомобиле и спрашивает какие детали для ТО требуются. 
Находит артикулы этих деталей и выдает пользователю.

Если вы хотите протестировать работу бота вы можете использовать следующие VIN номера:

-WAUBH54B11N111054  
-VF1LA0H5324321010  
-Z8NAJL00050366148  


### Техническое задание
Написать телеграмм-бота который будет принимать vin номер автомобиля и выдавать 
артикулы деталей для ТО взятые с сайта autodoc.ru.

### Решение
1. Бот запрашивает у пользователя VIN номер автомобиля(vin_car). 
2. Делает запрос на сайт и получает по нему данные для поиска машины в каталоге сайта.
   (catalog_number_car и ssd_car)
3. Делает запросы с этими данными и получает данные о машине(car_info) и 
данные по деталям которые необходимы для ТО этой машины(car_details).
4. Выводит в чат информацию о машине и кнопки с названиями деталей.
5. Пользователь выбирает какая деталь ему понадобится и нажимает кнопку.
6. Бот делает новый запрос к сайту в котором передает порядковый номер детали(quick_group_id),
и данные для поиска машины(catalog_number_car и ssd_car)
7. В ответ на запрос получает данные по выбранной детали(article_details)
8. Выводит в чат названия деталей и артикулы. Если для ТО выбранного узла нужно несколько деталей 
выведет их все в разных строчках.
9. После чего предложит выбрать другую деталь для этой машины.
10. В меню бота можно отправить команду старт, чтобы вернуться к началу работы с ботом.


""")
        image = Image.open('file/shema_autodoc_bot.png')  # Замените на путь к вашей картинке
        st.image(image, caption='Схема работы Телеграмм-бота')

        st.markdown("""

## Используемые технологии

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Telebot](https://img.shields.io/badge/Telebot-0.0.5+-yellow?logo=telegram)
![Requests](https://img.shields.io/badge/Requests-2.32.3+-orange?logo=python)

## Установка
Бот уже запущен на VPS сервере и работает постоянно. Его нужно просто найти: https://t.me/autodoc_articles_bot

Если вы хотите запустить его у себя следуйте инструкции:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/kulakov544/bot_autodoc_telebot.git
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте `venv\\Scripts\\activate`
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Создайте файл .env в котором будет храниться токен телеграмм-бота
   ```
   BOT_TOKEN = "TOKEN"
   ```
5. Запустите программу.
   ```bash
   python main.py
   ```
        
        """)

    st.write("---")

    with st.expander("Проект: Анализ вакансий на hh.ru. ETL"):
        st.markdown("""
        ## Анализ вакансий на hh.ru        
        Все три репозитория по этому проекту размещены на GitHab:
        1. pars_hh_ETL https://github.com/kulakov544/pars_hh_ETL.git
        2. pars_hh_DWH https://github.com/kulakov544/pars_hh_DWH.git
        3. pars_hh_Report https://github.com/kulakov544/pars_hh_report.git
        
        ### Бизнес требование
        Нужно узнать какие навыки требуются на рынке вакансий.
        
        ### Техническое задание
        Получить аналитику по требованиям к соискателям вакансий на сайте hh.ru по IT направлению.
        
        ### Решение
        1. Построить базу DWH на PostgreSQL.
        2. Получить данные о вакансиях с сайта hh.ru
        3. Провести первичную обработка данных для загрузки в базу.
        4. Загрузить данные в Stage слой DWH.
        5. Трансформировать данные для укладки на долговременное хранение.
        6. Заполнить справочники и таблицу вакансий в Core слое DWH, с сохранением обновленных записей в таблицу истории.
        7. Оркестрация процесса через Prefect.
        8. Сделать View и материализацию таблиц в DataMart слое DWH
        9. По данным из DataMart построить дашборды в Yandex Data Lens и Power BI
        
        
        ### План реализации
        Схема работы программы:
        <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_ETL/master/flow_pars_hh_dir/file/DWH.png' style='width: 100%; height: auto;'><br>
        Подробную схему DWH можно посмотреть в соответствующем проекте:  
        https://github.com/kulakov544/pars_hh_DWH.git
        
        ### Работа программы:
        1. Создание списка наборов параметров search_params_list.
        2. Создание сета для отбора уникальных id вакансий uniq_id
        3. Разбивка наборов параметров на пакеты по 100 штук.
        4. Формирование списка id вакансий.(vacancies_id_df)
           1. Получает 100 наборов параметров
           2. В цикле запрашивает данные по каждому набору параметров
           3. Получает вакансии по этому набору и проверяет есть ли id вакансий
           в uniq_id. Если нет, то добавляет его туда и в массив vacancies_data.
           4. Когда пройдет по всем вакансиям из этого набора параметров добавляет их
           в all_vacancies_id_df и берет следующий набор параметров.
           5. Полученный датафрейм возвращается в vacancies_id_df
        5.  По полученному списку id начинает собирать информацию о вакансиях.
              1. Запросы делаются отдельно для каждого id.
              2. В all_vacancies_data собирается основная информация о вакансии. 
              В all_vacancies_skill собираются скилы необходимые для этой вакансии.
            3. Тут же проходит первичная обработка. Проверки на наличие данных, добавление 
            хеша вакансии, изменение форматов дат...
            4. Полученные датафреймы возвращаются в vacancies_data_df и vacancies_skill_df
        6. Если данные были собраны они загружаются в соответствующие таблицы с помощью put_data.
        Это происходит с помощью replace по этому при каждой загрузке таблицы очищаются.
        7. Когда данные загружены запускаются функции переноса данных из stage в core c
        помощью функции update_core
           1. В таблицу stage_pars_hh добавляется столбец статуса. Он зависит от того есть 
           эта вакансия в базе и совпадают ли хеши с теми которые уже есть.
           2. Заполняются справочники включая скилы, если для них есть новые данные.
           3. Переносятся вакансии которых ещё не было в базе.
           4. Вакансии которые обновились, переносятся в fact_history и удаляются из основной таблицы.
           5. Вместо них загружаются новые записи.
           6. Обновляется таблица мапинга скилов и вакансий.
        8. Всё это является потоком Prefect и в основных функциях проставлены таски.
        9. Отдельным потоком является получение курсов валют.
        10. В слое Data Mart созданы представления, которые строят таблицы с нужными данными.
        По этим таблицам построен дашборд в PowerBI. Так же эти таблицы можно просто просмотреть любой 
        программой для работы с базами данных.
        
        
        ## Используемые технологии
        
        ![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
        ![Pandas](https://img.shields.io/badge/Pandas-1.3.3+-yellow?logo=pandas)
        ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.22+-orange?logo=python)
        ![Prefect](https://img.shields.io/badge/prefect-2.19.8+-green?logo=prefect)
        ![Requests](https://img.shields.io/badge/Requests-2.32.3+-green?logo=python)
        ![numpy](https://img.shields.io/badge/numpy-2.0.1+-green?logo=python)
        
        ## Установка
        
        1. Клонируйте репозиторий:
           ```bash
           git clone https://github.com/kulakov544/prefect_dev.git 
           ```
        2. Создайте виртуальное окружение и активируйте его:
           ```bash
           python -m venv venv
           source venv/bin/activate  # Для Windows используйте `venv\\Scripts\\activate`
           ```
        3. Установите необходимые зависимости:
           ```bash
           pip install -r requirements.txt
           ```
        4. В папке проекта создайте файл .env с данными для подключения к вашей базе данных.
        access_token можно получить с помощью скриптов Authorization.py и authorization_code.py
        если у вас есть коды для его получения, которые можно запросить на https://dev.hh.ru/
           ```bash
           conn_string = 'postgresql+psycopg2://user:password@localhost:port/mydatabase'
           access_token = "APP*"
           ```
        5. Авторизуйтесь на сервере prefect
        ```
        prefect cloud login
        ```
        5. Запустите программу.
           ```bash
           python main.py
           ```

        """, unsafe_allow_html=True)

    st.write("---")

    with st.expander("Проект: Анализ вакансий на hh.ru. DWH"):
        st.markdown("""
            ## Анализ вакансий на hh.ru

            Данный репозиторий является частью проекта по анализу вакансий с hh.ru.  
            Здесь будут размещены данные о ETL.
            Всего таких репозиториев три:
            1. pars_hh_ETL https://github.com/kulakov544/pars_hh_ETL.git
            2. pars_hh_DWH https://github.com/kulakov544/pars_hh_DWH.git
            3. pars_hh_Report https://github.com/kulakov544/pars_hh_report.git
            
            ### Бизнес требование
            Нужно узнать какие навыки требуются на рынке вакансий.
            
            ### Техническое задание
            Получить аналитику по требованиям к соискателям вакансий на сайте hh.ru по IT направлению.
            
            ### Решение
            1. Построить базу DWH на PostgreSQL.
            2. Получить данные о вакансиях с сайта hh.ru
            3. Провести первичную обработка данных для загрузки в базу.
            4. Загрузить данные в Stage слой DWH.
            5. Трансформировать данные для укладки на долговременное хранение.
            6. Заполнить справочники и таблицу вакансий в Core слое DWH, с сохранением обновленных записей в таблицу истории.
            7. Оркестрация процесса через Prefect.
            8. Сделать View и материализацию таблиц в DataMart слое DWH
            9. По данным из DataMart построить дашборды в Yandex Data Lens и Power BI  

            <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_DWH/master/file/DWH.png' style='width: 100%; height: auto;'><br>
            
            ### План DWH
            Таблицы слоя Stage:
            Слой Stage содержит две таблицы. stage_pars_hh и stage_pars_hh_skill.  
            stage_pars_hh основная таблица с данными о вакансии. В неё попадает информация из 
            ответа Api HH после небольшой обработки.
            stage_pars_hh_skill это навыки указанные в вакансии. Они специально вынесены в отдельную таблицу.
            Навыков в одной вакансии может быть много и их надо, либо хранить в неудобном формате, либо загружать 
            отдельной таблицей и сразу отправлять в справочник.
            <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_DWH/master/file/stage.png' style='width: 70%; height: auto;'><br>
            
            
            Таблицы слоя Core и схема переноса старых данных:
            Таблицы и связи между ними изображены на схеме. Справа на схеме логика работы с 
            устаревшими записями. Зеленым выделено то что реализовано в данный момент. В 
            будущем планируется реализация третьего варианта работы с устаревшими записями.
            Все процедуры по переносу данных присутствуют в папке func_core.
            Запускаются они в ETL следующим кодом:
            ```
            def update_core():
                # Обновление столбца статуса
                sqlt_stmt = "select core.add_status();"
                execute_stmt(sqlt_stmt)
            
                # Обновление справочников
                sqlt_stmt = "select core.update_core_ref();"
                execute_stmt(sqlt_stmt)
            
                # Добавление новых записей
                sqlt_stmt = "SELECT core.add_fact_vacancy_0();"
                execute_stmt(sqlt_stmt)
            
                # Перенос записей в историю и удаление перенесенных вакансий
                sqlt_stmt = "SELECT core.update_fact_history();"
                execute_stmt(sqlt_stmt)
            
                # Обновление записей
                sqlt_stmt = "SELECT core.add_fact_vacancy_2();"
                execute_stmt(sqlt_stmt)
            
                # Обновление таблицы мапинга скилы-вакансии
                sqlt_stmt = "select core.add_skill_vacancy_map();"
                execute_stmt(sqlt_stmt)
            ```

            <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_DWH/master/file/core.png' style='width: 100%; height: auto;'><br>
            
            Представление в слое Data Mart:
            Этот слой нужен для того, чтобы подготовить данные для предоставления пользователям.
            К нему же выдаются права доступа. Чтобы пользователь имел доступ только к тем данным к 
            которым должен.
            <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_DWH/master/file/data_mart.png' style='width: 70%; height: auto;'><br>
            
            ## Используемые технологии
            
            ![PosgreSQL](https://img.shields.io/badge/PosgreSQL-blue?logo=posgres)
            ![SQL](https://img.shields.io/badge/SQL-yellow?logo=SQL)


            """, unsafe_allow_html=True)

    st.write("---")

    with st.expander("Проект: Анализ вакансий на hh.ru. Report"):
        st.markdown("""
                ## Анализ вакансий на hh.ru

                Данный репозиторий является частью проекта по анализу вакансий с hh.ru.  
                Здесь будут размещены данные о ETL.
                Всего таких репозиториев три:
                1. pars_hh_ETL https://github.com/kulakov544/pars_hh_ETL.git
                2. pars_hh_DWH https://github.com/kulakov544/pars_hh_DWH.git
                3. pars_hh_Report https://github.com/kulakov544/pars_hh_report.git
                
                ### Бизнес требование
                Нужно узнать какие навыки требуются на рынке вакансий.
                
                ### Техническое задание
                Получить аналитику по требованиям к соискателям вакансий на сайте hh.ru по IT направлению.
                
                ### Решение
                1. Построить базу DWH на PostgreSQL.
                2. Получить данные о вакансиях с сайта hh.ru
                3. Провести первичную обработка данных для загрузки в базу.
                4. Загрузить данные в Stage слой DWH.
                5. Трансформировать данные для укладки на долговременное хранение.
                6. Заполнить справочники и таблицу вакансий в Core слое DWH, с сохранением обновленных записей в таблицу истории.
                7. Оркестрация процесса через Prefect.
                8. Сделать View и материализацию таблиц в DataMart слое DWH
                9. По данным из DataMart построить дашборды в Yandex Data Lens и Power BI  

                <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_report/master/file/DWH.png' style='width: 100%; height: auto;'><br>
                                
                ### Power BI
                Дашборд призван ответить какие навыки и по каким типам вакансий требуются чаще всего.
                Дополнительно добавлены счетчики для понимания количества вакансий выборке. Чем больше 
                вакансий тем точнее данные.
                <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_report/master/file/report_1.png' style='width: 100%; height: auto;'><br>
                  
                На второй странице размещена карта с местом нахождения вакансий. Она должна была показать в 
                каких городах больше скопление вакансий. А за одно могла позволить выбирать вакансии 
                по местонахождению и получать о них информацию. К сожалению вакансий с заполненными данными
                о местонахождении крайне мало.
                <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_report/master/file/report_2.png' style='width: 100%; height: auto;'><br>
                В идеале должна была получиться похожая картина во многих городах и скопления точек разной 
                плотности на карте страны.
                <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_report/master/file/report_3.png' style='width: 100%; height: auto;'><br>
                На третьей странице можно посмотреть топ компаний по количеству вакансий с различными 
                параметрами.
                <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_report/master/file/report_4.png' style='width: 100%; height: auto;'><br>
                Четвертая страница сделана для поиска вакансий по некоторым параметрам. После чего их можно 
                отсортировать в одном списке.
                <img src='https://raw.githubusercontent.com/kulakov544/pars_hh_report/master/file/report_5.png' style='width: 100%; height: auto;'><br>
                  
                Файл отчета для PowerBI есть в репозитории. 
                """, unsafe_allow_html=True)
