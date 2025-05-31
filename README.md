
## 📉 Amazon Price Tracker (India)

This is a simple Python script that checks the price of a product on Amazon India and alerts you if it drops below a specified threshold. It also saves the daily price to a CSV file for historical tracking.

## 🔧 Features

- Scrapes the product name and price from Amazon
- Logs price history to a `.csv` file
- Notifies with a beep sound when the price is below your set limit
- Easy to customize and extend

## 📦 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

Install the dependencies:

```bash
pip install -r requirements.txt

```
## 📝 Usage

1. Open `price_tracker.py`
2. Replace the `base_url` with your Amazon India product URL.
3. Set your desired `threshold_price`.

```python
base_url = 'https://amzn.in/your-product-link'
threshold_price = 25000
```

4. Run the script:

```bash
python price_tracker.py
```

If the price is below the threshold, you'll get a beep alert and it will log the price in a CSV file.

## 📊 Output

* A CSV file with the product's name will be created (e.g., `Macbook.csv`)
* It stores the price with the current date

## 🚀 To-Do / Improvements

* Add support for email or Telegram alerts
* Track multiple products from a list
* Handle CAPTCHA and Amazon blocking more gracefully

## ⚠️ Disclaimer

This tool is for educational purposes only. Scraping Amazon may violate their terms of service.

---

Made with 💻 by Charan

