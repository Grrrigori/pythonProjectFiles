import requests
from  bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}


def user_choice():
    try:
        user_input= input("Please choose:\n1. If You want to know some random fact press 1\n2. If You don't want to know some random fact press 2\n3. EXIT \n -->")
        if user_input== "1":
            random_facts()
        elif user_input== '2':
            print('May be next time')

        elif user_input== '3':
            print('Good bye')
        else:
            print("choice out of range")
            user_choice()# chtobi vernut v nachalo funkcii v sluchae esli ne to nabrali
    except:
        print('Error')
        user_choice()

def random_facts():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = "https://www.google.com/search?q=random+facts&oq=random+fac&aqs=chrome.0.0l2j69i57j0l7.2799j0j15&sourceid=chrome&ie=UTF-8"
    full_page= requests.get(url, timeout=5, headers=headers)
    soup = BS(full_page.content, 'html.parser')
    print(soup.title.value)
    # print(soup.prettify())
    question = soup.findAll("div", class_='sW6dbe')
    answer = soup.findAll("div", class_='EikfZ')

    print(type(answer))
    print(len(answer))
    # result1 = question.text[0]
    # result2= answer.text[0]


    print('Did You know?')
    print('Question:' + str(question))
    print('Answer:' + str(answer))


random_facts()
user_choice()

