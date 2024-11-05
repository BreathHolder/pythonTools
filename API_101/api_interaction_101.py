import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def get_exchange_rates(base_currency):
    url= f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']

print(get_exchange_rates('GBP'))

def convert_currency(source_currency, target_currency, amount):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}/{amount}'
    response = requests.get(url)
    data = response.json()
    return data['conversion_result']

## Intro Menu

def intro_menu():
    print('Welcome to the Currency Converter')
    print('For a list of all currency symbols, visit https://en.wikipedia.org/wiki/ISO_4217')
    print('1. Get Exchange Rates')
    print('2. Convert Currency')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        base_currency = input('Enter the base currency: ')
        print(get_exchange_rates(base_currency))
    elif choice == '2':
        source_currency = input('Enter the source currency: ')
        target_currency = input('Enter the target currency: ')
        amount = float(input('Enter the amount: '))
        print(convert_currency(source_currency, target_currency, amount))
    elif choice == '3':
        exit()
    else:
        print('Invalid choice')
        intro_menu()

intro_menu()

