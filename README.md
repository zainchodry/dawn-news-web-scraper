# 📰 Dawn News Web Scraper

A lightweight, efficient Python scraper for extracting the latest headlines and article links from [Dawn News](https://www.dawn.com/), one of Pakistan’s leading news websites.

This project uses **BeautifulSoup**, **requests**, and **pandas** to scrape and store real-time news data in **CSV** and **Excel** formats — perfect for data analysis, automation, or news aggregation.

---

## 🚀 Features

- 🔍 Scrapes headlines and URLs from Dawn.com homepage
- 📅 Captures date and time of scraping
- 📄 Saves data to `CSV` and `XLSX` formats
- 🧰 Clean, modular, beginner-friendly code
- 💼 Ideal for learning, automation, or news bots

---

## 🧰 Tech Stack

| Technology       | Purpose                       |
|------------------|-------------------------------|
| **Python 3.8+**   | Programming Language          |
| **requests**      | Make HTTP requests            |
| **BeautifulSoup** | HTML parsing & scraping       |
| **pandas**        | Data manipulation and export  |

---

## 📁 Project Structure

dawn-news-web-scraper/
├── venv/ # Virtual environment (ignored in Git)
├── webscraper.py # Main scraper script
├── news.csv # Output: CSV data
├── news.xlsx # Output: Excel data
├── requirements.txt # Project dependencies
├── .gitignore # Ignored files/folders
└── README.md # Project documentation


---

## 📦 Installation & Setup

### ✅ Prerequisites

- Python 3.8 or above
- Git installed
- (Optional) `virtualenv` for project isolation

---

### 🔧 Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/zainchodry/dawn-news-web-scraper.git
cd dawn-news-web-scraper

#Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

#Install Dependencies
pip install -r requirements.txt

#Run the Scraper
python scrapping.py
