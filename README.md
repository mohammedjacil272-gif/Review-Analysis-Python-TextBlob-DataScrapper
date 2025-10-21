# Review-Analysis-TextBlob-DataScrapper-Python   

A Python-based project that shows how to use **Web Scraping** and **Natural Language Processing (NLP)** to examine the tone of user or critical reviews that have been scraped from a website that is accessible to the public (such as Wikipedia).

This project demonstrates: * Ethical web scraping with `BeautifulSoup` and `requests`.
* The **TextBlob** library is used for sentiment scoring.
* Analytical reasoning that adapts to the volume of data.
 ### 🛠️ Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/Review-Analysis-Python-TextBlob-DataScrapper.git](https://github.com/mohammedjacil272-gif/Review-Analysis-Python-TextBlob-DataScrapper.git)
    cd Review-Analysis-Python-TextBlob-DataScrapper
    ```

2.  **Create and Activate Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1   # On Windows PowerShell
    # source venv/bin/activate    # On Mac/Linux
    ```

3.  **Install Dependencies:**
    ```bash
    pip install requests beautifulsoup4 textblob
    ```

4.  **Download TextBlob Corpora:**
    * *Note: This downloads the necessary data for TextBlob to function.*
    ```bash
    python -m textblob.download_corpora
    ```
### ▶️ Execution Workflow

The project consists of two separate scripts:

#### **1. Scrape the Data**

Run the scraper to extract review paragraphs from the target URL (add your url in the "add your wikipedia link" section of the code, targeting the 'Critical_response' section).

```bash
python data_scrapper.py
python data_analyzer.py
***

## Analysis Parameters and Logic.

```markdown
### 📊 Sentiment Logic Explained

The `data_analyzer.py` uses adaptive thresholds based on the quantity of scraped reviews (`i`):

* **Polarity Score:** A float between -1.0 (Negative) and +1.0 (Positive).
* **Small Sample (i < 80):** A conservative threshold is used (e.g., +/- 0.05) to classify sentiment, as the average is less reliable.
* **Large Sample (i ≥ 80):** A wider threshold is applied (e.g., +/- 0.2) because the large number of samples provides higher confidence in the average result.
### ⚖️ Ethical Scraping Note

This project adheres to ethical scraping guidelines:

* Uses a descriptive `User-Agent` header.
* Includes a `time.sleep()` delay to avoid overloading server resources.
* The code is designed for educational practice on public domain or intentionally open content (like Wikipedia). Users are advised to review the `robots.txt` file of any new target site before scraping.
