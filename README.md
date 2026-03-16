
```markdown
# 🏠 Automated Real Estate ETL Pipeline

## 📌 Overview
This project is a fully automated, serverless ETL (Extract, Transform, Load) pipeline designed to aggregate real-time real estate market data. It scrapes newly listed properties ("flash leads") across 15 major US housing markets and delivers a clean, formatted CSV report via email every morning.

The system is built to autonomously bypass enterprise-grade anti-bot protections (PerimeterX) using residential proxy routing, and it runs on a strict CI/CD cron schedule requiring zero manual intervention.

## ⚙️ Architecture & The ETL Process

* **Extract:** Utilizes **Scrapy** to intercept and parse hidden backend JSON payloads from Zillow, bypassing brittle HTML parsing. Traffic is routed through the **ScrapeOps Proxy API** to rotate IP addresses and avoid 403/401 datacenter blocks.
* **Transform:** Python logic filters unstructured JSON data to isolate properties listed within the last few minutes or hours. It cleanses the data and maps specific key-value pairs (Price, Address, Zillow ID, URL).
* **Load:** The clean data is loaded into a structured `.csv` format and automatically distributed to stakeholders using a custom **SMTP email script** directly from the cloud.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Framework:** Scrapy (Web Scraping / Data Extraction)
* **Cloud Infrastructure:** GitHub Actions (Serverless CI/CD Automation)
* **Network Routing:** ScrapeOps (Residential Proxy API)
* **Delivery:** SMTP Protocol / Standard Python Email Library

## 🚀 Cloud Automation (GitHub Actions)
This engine is deployed to the cloud and runs automatically at 9:00 AM UTC every day. 
The automation is handled by `.github/workflows/scraper.yml`.

### Required GitHub Secrets
To deploy this pipeline securely, the following credentials must be added to your repository's **Secrets and variables**:
* `EMAIL_PASSWORD`: A 16-letter Google App Password used to securely authenticate the SMTP delivery script.

## 💻 How to Run Locally

If you wish to test the pipeline on your local machine:

**1. Clone the repository and install dependencies:**
```bash
git clone [https://github.com/YOUR-USERNAME/real-estate-flash-scraper.git](https://github.com/YOUR-USERNAME/real-estate-flash-scraper.git)
cd real-estate-flash-scraper
python -m venv .venv
source .venv/Scripts/activate  # (On Windows Git Bash)
pip install -r requirements.txt

```

**2. Update API Keys:**

* Open `real_estate_scraper/spiders/zillow.py`.
* Insert your ScrapeOps API key into the `payload` dictionary.
* Open `send_email.py` and update the sender and receiver email addresses.

**3. Set your local environment variable for the email:**

```bash
export EMAIL_PASSWORD="your_16_letter_google_app_password"

```

**4. Run the Extractor & Trigger the Email:**

```bash
# Run the scraper and output the data to a CSV
scrapy crawl zillow -O todays_leads.csv

# Run the delivery system
python send_email.py

```

## ⚠️ Disclaimer

This project was built strictly for educational and portfolio purposes to demonstrate ETL architecture, proxy network routing, and cloud automation. Please review and respect the Terms of Service of any website before scraping it at scale.

```

***

### How to add this to your project:
1. Open your terminal and make sure you are in the root folder of your project.
2. Type `touch README.md`.
3. Open that file in PyCharm, paste the exact markdown above, and save it. (Make sure to change `YOUR-USERNAME` in the clone link to your actual GitHub username!).
4. Run your standard Git commands: `git add README.md` -> `git commit -m "Added professional README"` -> `git push`.

Once you push that, your GitHub repository will instantly transform from a basic code folder into a highly professional portfolio piece. 

**You now have the code, the cloud architecture, the LinkedIn profile, and the GitHub documentation. Are you officially ready to start sending this out to recruiters?**

```