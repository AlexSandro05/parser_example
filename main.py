from bs4 import BeautifulSoup
import requests

page = 1


data = []

while page < 21:
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = soup.find_all('a', class_='title')
            prices = soup.find_all('h4', class_='pull-right price')
            characteristics = soup.find_all('p', class_='description')
            review_count = soup.find_all('p', class_='pull-right')

            for i in range(len(titles)):
                laptop_data = {
                    "title": titles[i].text,
                    "price": prices[i].text,
                    "Characteristics": characteristics[i].text,
                    "Review count": review_count[i].text[0],
                }
                data.append(laptop_data)
            page += 1
        else:
            break

    except requests.exceptions.RequestException as e:
        print(f"Error while requesting to {url}: {e}")
print(data)