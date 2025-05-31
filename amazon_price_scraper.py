import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
import winsound

base_url = 'https://amzn.in/d/aqZptI8'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.amazon.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}
threshold_price = 25000

def get_amazon_price(url):
    data = requests.get(url, headers=headers)

    if data.status_code != 200:
        print("Failed to retrieve the page.")
        return None
    if "captcha" in data.text.lower():
        print("Blocked by Amazon. Try using proxies or rotating headers.")
        return None, None

    soup = BeautifulSoup(data.content, 'html.parser')
    try:
        name = soup.find(id="productTitle")
        price = soup.find("span",class_="a-price-whole")
    except AttributeError:
        print("Could not find product name or price in the HTML.")
        return None, None
    
    return name,price
    
def save_to_csv(name, price):
    filename = f'{name.split()[0]}.csv'
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date.today(), price])
    if int(price) < threshold_price:
        print(f"Price alert! {name} is now {price}")
        winsound.Beep(1000, 1000)

if __name__ == "__main__":
    n,p = get_amazon_price(base_url)
    if n and p:
        name = n.get_text(strip=True)
        price = int(p.get_text(strip=True).replace(',', '').replace('.', '')) 
        save_to_csv(name,price)
    else:
        print("Could not find product name or price.")
