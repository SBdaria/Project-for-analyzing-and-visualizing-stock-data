Описание проекта
=====================
Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков. Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.

Структура и модули проекта
-----------------------------------
1. data_download.py:

- Отвечает за загрузку данных об акциях.
- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.


2. main.py:

- Является точкой входа в программу.
- Запрашивает у пользователя тикер акции и временной период, загружает данные, обрабатывает их и выводит результаты в виде графика.


3. data_plotting.py:

- Отвечает за визуализацию данных.
- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.


Основной функционал
-----------------------------------
Программа запрашивает у пользователя тикер акции и временной интервал. После чего обрабтывает введенные данные и сохраняет график зависимости цены от даты в папке проекта.
Также в консоль выводится средняя цена закрытия акций за заданный период.
<img width="1430" alt="image" src="https://github.com/user-attachments/assets/8c99b6d5-8ef3-428b-8528-e35d0785b531" />
![AAPL_1mo_stock_price_chart](https://github.com/user-attachments/assets/75f072b9-bba0-4cba-aa44-75a9ee467b9d)


Пошаговое использование
-----------------------------------
1. Запустите main.py.
2. Введите интересующий вас тикер акции (например, 'AAPL' для Apple Inc).
3. Введите желаемый временной период для анализа (например, '1mo' для данных за один месяц).
4. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее и отобразит график
