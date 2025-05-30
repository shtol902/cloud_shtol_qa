# Тестовое задание

## Часть №1 

Задание в файле task_1.py

---

## Часть №2

### Структура проекта
1. Базовое действие (открыть страницу) вынесено в фикстуру conftest.py.
2. Для более удобной поддержки тестов используется паттерн проектирования Page Object Model.

---------------------
### Установка

Для начала работы с проектом вам потребуется установить необходимые зависимости. Рекомендуется использовать виртуальное окружение.

#### Установите зависимости:
```sh
pip install -r requirements.txt
```
---------------------
### Запуск всех тестов

Для запуска тестов используйте следующую команду:
```sh
pytest -v tests 
```

### Запуск тестов по разделу (пример)

Для запуска тестов используйте следующую команду:
```sh
pytest -v tests/test_example.py
```

### Запуск кокретного теста (пример)

Для запуска тестов используйте следующую команду:
```sh
pytest -v tests/test_ui.py -k'test_login_example'
```

### Генерация отчета в Allure
```sh
pytest tests --alluredir=allure_results
allure serve allure_results  
```
