# Import required Libraries
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook
import pandas as pd

# Function to get the search term
def get_url(search_term):
    """Generate a URL from search term"""
    template = 'https://www.amazon.com/s?k={}'
    search_term = search_term.replace(' ', '+')

    #add term query to url
    url = template.format(search_term)

    #add page query placeholder
    url += '&page={}'

    return url

def extract_record(item):
    try:
        atag = item.h2.a
        description = atag.text.strip()
        url = 'https://www.amazon.com'+atag.get('href')
    except:
        pass


    try:
        # Price
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return

    try:
        #Ratings
        rating = item.i.text
        # Ratings Count
        review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = {description, price, rating, review_count, url}
    return result

def main(search_term):
    # start the driver
    driver = webdriver.Chrome()

    records = []
    url = get_url(search_term)

    for page in range(1, 5):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type':'s-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    driver.close()

    #save results in .csv
    #with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    #    writer = csv.writer(f)
    #    writer.writerow(['Description', 'Price', 'Rating', 'Review_count','URL'])
    #    writer.writerows(records)
    try:
        wb = Workbook()
        ws = wb.worksheets[0]
        ws.append(['Description', 'Price', 'Rating', 'Review_count','URL'])

        for row in records:
            ws.append(row)

            ws.save(f'data.xlsx')
            wb.close()
    except:
        df = pd.DataFrame({'Product Name':records})
        print(df)
        df.to_csv('data.csv', index=False, encoding='utf-8')


main('cutting board')
