import requests
from  bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
def user_choice():
    try:
        user_input= input("Please choose:\n1. CONVERT RUB to EUr\n2. CONVERT EUR to RUB\n3. EXIT \n -->")
        if user_input == "1":
            ammount= float(input("PLease insert amount:\n-->"))
            result_string = '{result:2f}, EUr'
            result= ammount * get_currency_value()
            print(result_string.format(result=result))
            # print(result, 'Euro')
        elif user_input== '2':
            ammount = float(input("PLease insert amount:\n-->"))
            result_string= '{result:2f}, RUB'
            result = ammount / get_currency_value()
            print(result_string.format(result=result))

        elif user_input== '3':
            print('Good bye')
        else:
            print("choice out of range")
            user_choice()# chtobi vernut v nachalo funkcii v sluchae esli ne to nabrali
    except:
        print('Error')
        user_choice()

def get_currency_value():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    url = "https://www.google.com/search?sxsrf=ALeKk02ZBWWmwww6fUlL_XTXiQItktvdVQ%3A1615398242884&ei=YgVJYKzGNe6jrgT87bKABw&q=rub+to+eur&oq=rub+to+eur&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEEMQRhCCAjICCAAyBQgAEMsBMgUIABDLATIHCAAQhwIQFDICCAAyAggAMgIIADICCAAyAggAOgQIIxAnOgQIABBDOggILhDHARCjAjoCCC46BAguECc6CAguEMcBEK8BUOKKA1jolANgnZsDaABwAngAgAGxAogB3AuSAQgwLjEwLjAuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwis_7-zo6bvAhXukYsKHfy2DHAQ4dUDCA0&uact=5"
    full_page= requests.get(url, timeout=5, headers=headers)
    soup = BS(full_page.content, 'html.parser')
    # print(soup.prettify())
    # currency_value = soup.findAll("span", class_='DFlfde SwHCTb')
    currency_value = soup.findAll("span", {'class':'DFlfde SwHCTb'})
    result = currency_value[0].text.replace(',','.')

    return float(result)

# get_currency_value()
user_choice()