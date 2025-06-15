from bs4 import BeautifulSoup
import json
from transformers import pipeline

def reading_information():
    try:
        # Открываем файл output.json для чтения
        with open('D:\Python и прочее\Информатика и код на Python\output.json', 'r', encoding='utf-8') as file:
            data = json.load(file)  # Загружаем данные из файла
            print(f"[✓] Файл output.json успешно прочитан.")
            return data  # Возвращаем данные из файла
    except FileNotFoundError:
        print(f"[✗] Файл output.json не найден.")
        return False
    except json.JSONDecodeError as e:
        print(f"[✗] Ошибка при декодировании JSON: {e}")
        return False
    except Exception as e:
        print(f"[✗] Произошла ошибка при чтении файла: {e}")
        return False

def sorting_and_bringing_to_normal_condition(data):
    result = reading_information()  # Вызываем функцию и сохраняем её результат
    if result == data:              # Сравниваем результат с переменной data
        print("Данные совпадают.")
    else:
        print("Данные не совпадают.")

# Пример вызова функции
expected_data = {"key": "value"}  # Ваши ожидаемые данные
sorting_and_bringing_to_normal_condition(expected_data)

def neural_network():

# Загружаем пайплайн для задачи "Вопрос/Ответ"
    qa_pipeline = pipeline("question-answering")

# Пример контекста и вопроса
    context = str(input())

    question = str(input())

# Получаем ответ на вопрос
    result = qa_pipeline(question=question, context=context)

# Выводим результат
    print(f"Ответ: {result['answer']}")
    print(f"Оценка уверенности: {result['score']:.4f}")