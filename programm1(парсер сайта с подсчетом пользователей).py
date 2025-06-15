from urllib import response
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from json import dumps


def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[✓] {url} — доступен (статус: {response.status_code})")
            return True
        else:
            print(f"[✗] {url} — недоступен (статус: {response.status_code})")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[✗] {url} — ошибка при запросе: {e}")
        return False

def get_online_user_count(url): # подсчет количества пользователей сайта онлайн
        # Выполняем HTTP запрос к сайту
        response = requests.get(url)
        collected_data = []
        # Проверяем код ответа
        if response.status_code == 200:
            # Создаем объект BeautifulSoup для парсинга HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            for item in soup.find_all('div', class_='item'):
                title = item.find('h2').text
                description = item.find('p').text
                keywords = [kw.text for kw in item.find_all('span', class_='keyword')]
                collected_data.append({"title": title, "description": description, "keywords": keywords})
            
            # Пример: Находим элемент, где указано количество пользователей
            # Предполагаем, что количество пользователей находится в элементе с классом "user-count"
            user_count_element = soup.find(class_='user-count')

            if user_count_element:
                # Получаем текст и выводим его
                user_count = user_count_element.text.strip()
                print(f'Количество пользователей на сайте: {user_count}')
                return int(user_count)  # Возвращаем количество пользователей как целое число
            else:
                print('Не удалось найти элемент с количеством пользователей.')
                return 0
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')
            return 0
   

def reading_information_from_the_site(url): # считывание информации с сайта
    try:
        response = requests.get(url)
        response.raise_for_status()  # проверка на ошибки HTTP
        content = response.text.lower()

        # Используем BeautifulSoup для извлечения текста
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы {url}: {e}")
        return None


def check_keywords(content): # проверка соотвествия полученных данных и сохранение их
    # Проверка наличия ключевых слов в содержимом
    keywords = ['python', 'documentation', 'api', 'tutorial', 'java', 'javaScript', 'html', 'java', ]
    if content:
        return any(keyword in content for keyword in keywords)
    return False

def check_url_in_browser(browser_name, url):
    if browser_name == "Chrome":
        driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver установлен и добавлен в PATH
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()  # Убедитесь, что GeckoDriver установлен и добавлен в PATH
    elif browser_name == "Edge":
        driver = webdriver.Edge()  # Убедитесь, что EdgeDriver установлен и добавлен в PATH
    else:
        print(f"Браузер {browser_name} не поддерживается.")
        return
    try:
        driver.get(url)
        print(f"Страница успешно загружена в {browser_name}.")
        # Пример проверки наличия элемента на странице
        if driver.find_element(By.TAG_NAME, "body"):
            print(f"Элемент 'body' найден на странице в {browser_name}.")
    except Exception as e:
        print(f"Ошибка при загрузке страницы в {browser_name}: {e}")
    finally:
        driver.quit()

def save_data_conservation(data):
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)
      
def main():
    # Объявляем переменную collected_data внутри функции
    collected_data = []
    # Список URL-адресов
    urls = [
        # Python
        'https://docs.python.org/3/',
        'https://docs.python.org/3/tutorial/index.html/',
        'https://pypi.org/',
        'https://realpython.com/',
        'https://www.programiz.com/python-programming/examples/',
        # Java
        'https://docs.oracle.com/javase/8/docs/',
        'https://docs.oracle.com/javase/tutorial/',
        'https://www.javatpoint.com/java-programs/',
        'https://spring.io/projects/spring-framework/',
        'https://mvnrepository.com/',
        # HTML
        'https://developer.mozilla.org/en-US/docs/Web/HTML/',
        'https://www.w3schools.com/html/',
        'https://html.spec.whatwg.org/',
        'https://www.w3schools.com/html/html_examples.asp/',
        'https://validator.w3.org/',
        # CSS
        'https://developer.mozilla.org/en-US/docs/Web/CSS/',
        'https://www.w3schools.com/css/',
        'https://css-tricks.com/',
        'https://getbootstrap.com/docs/',
        'https://tailwindcss.com/docs',
        # Javascript
        'https://developer.mozilla.org/en-US/docs/Web/JavaScript/',
        'https://javascript.info/',
        'https://www.w3schools.com/js/',
        'https://nodejs.org/en/docs/',
        'https://reactjs.org/docs/getting-started.html/',
        'https://vuejs.org/v2/guide/',
        'https://angular.io/docs/',
        'https://www.typescriptlang.org/docs/',
        'https://d3js.org/',
        # Kotlin
        'https://kotlinlang.org/docs/home.html/',
        'https://play.kotlinlang.org/byExample/overview/',
        'https://developer.android.com/kotlin/',
        'https://kotlinlang.org/docs/coroutines-guide.html/',
        'https://kotlinlang.org/api/latest/jvm/stdlib/',
        # C++
        'https://isocpp.org/',
        'https://en.cppreference.com/w/',
        'https://www.learncpp.com/',
        'https://www.programiz.com/cpp-programming/examples',
        'https://www.boost.org/doc/libs/',
        # C
        'https://devdocs.io/c/',
        'https://www.gnu.org/software/libc/manual/',
        'https://www.programiz.com/c-programming/examples',
        'https://www.learn-c.org/',
        'https://en.cppreference.com/w/c/header',
        # C#
        'https://learn.microsoft.com/en-us/dotnet/csharp/',
        'https://learn.microsoft.com/en-us/dotnet/',
        'https://docs.unity3d.com/ScriptReference/',
        'https://www.programiz.com/csharp-programming/examples/',
        'https://learn.microsoft.com/en-us/aspnet/core/',
        # Rust
        'https://www.rust-lang.org/learn/',
        'https://doc.rust-lang.org/book/',
        'https://doc.rust-lang.org/rust-by-example/',
        'https://doc.rust-lang.org/cargo/',
        'https://doc.rust-lang.org/std/'
    ]

    # Обработка каждого URL
    for url in urls:
        if check_url(url):
            user_count = get_online_user_count(url)
            if user_count >= 15000:  # Если онлайн-пользователей больше или равно 15000
                print(f"Количество онлайн-пользователей на сайте {url}: {user_count}")
                collected_data.append({"url": url, "user_count": user_count})  # Сохраняем URL в список

            # Проверяем наличие ключевых слов на сайте
            content = reading_information_from_the_site(url)
            if content and check_keywords(content):
                print(f"Ключевые слова найдены на сайте: {url}")
                collected_data.append({"url": url, "content": content})  # Сохраняем URL в список

            browsers = ["Chrome", "Firefox", "Edge", "Brave"]
            for browser in browsers:
                check_url_in_browser(browser, url)
            

    # Сохраняем собранные данные в файл
    save_data_conservation(collected_data)

    # Проверка, были ли собраны данные
    if collected_data:
        print("Данные успешно сохранены в output.json")
    else:
        print("Ключевые слова не найдены, сайт не подходит!")


if __name__ == "__main__":
    main()