import datetime
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_data(city_code='1801'):
    datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    ua = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': ua.random
    }

    cookies = {
        'mg_geo_id': f'{city_code}'
    }

    response = requests.get(url='https://magnit.ru/promo/', headers=headers, cookies=cookies)

    with open(f'index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    with open('index.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    city = soup.find('a', class_='header__contacts-link_city').text.strip()
    cards = soup.find_all('a', class_='card-sale_catalogue')
    print(city, len(cards))

    cards_catalog = {}

    for card in cards:
        card_title = card.find('div', class_='card-sale__title')
        card_title_1 = str(card_title).replace('<div class="card-sale__title"><p>', '')
        card_title_2 = card_title_1.replace('</p></div>', '')

        try:
            card_discount = card.find('div', class_='card-sale__discount').text.strip()
        except AttributeError:
            continue

        card_price_old_integer = card.find('div', class_='label__price_old').find('span',
                                                                                  class_='label__price-integer').text.strip()
        card_price_old_decimal = card.find('div', class_='label__price_old').find('span',
                                                                                  class_='label__price-decimal').text.strip()
        card_old_price = f'{card_price_old_integer}.{card_price_old_decimal}'

        card_price_integer = card.find('div', class_='label__price_new').find('span',
                                                                              class_='label__price-integer').text.strip()
        card_price_decimal = card.find('div', class_='label__price_new').find('span',
                                                                              class_='label__price-decimal').text.strip()
        card_price = f'{card_price_integer}.{card_price_decimal}'

        card_img_in = card.find('div', class_='card-sale__col_img').find('source').get('data-srcset')
        card_img = f'https://magnit.ru{card_img_in}'
        card_sale_date = card.find('div', class_='card-sale__date').text.strip().replace('\n', ' ')

        article_id = card_img.split('/')[-1]
        article_id = article_id[:-6]

        print(f'{card_title_2}, {card_img}')

        if card_discount == "−50%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−53%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−30%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−37%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−31%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−43%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−49%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−38%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−36%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−61%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−37%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−52%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−33%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

        elif card_discount == "−32%":

            cards_catalog[article_id] = {
                'card_title_2': card_title_2,
                'card_discount': card_discount,
                'card_old_price': card_old_price,
                'card_price': card_price,
                'card_img': card_img,
                'card_sale_date': card_sale_date,
            }
            with open('Dzubga.json', 'w', encoding="utf-8") as file:
                json.dump(cards_catalog, file, indent=4, ensure_ascii=False)

    return cards_catalog


def main():
    collect_data(city_code='1801')



if __name__ == '__main__':
    main()
