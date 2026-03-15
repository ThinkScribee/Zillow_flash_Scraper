import os
import smtplib
from email.message import EmailMessage

# 1. Configuration (Update these emails)
SENDER_EMAIL = "tuboksmicheal@gmail.com"
RECEIVER_EMAIL = "mtubokeyi@gmail.com"
# GitHub Actions will securely inject this password from your Secrets
PASSWORD = os.environ.get("EMAIL_PASSWORD")
FILE_PATH = "todays_leads.csv"


def send_leads():
    # 2. Safety check: Did Scrapy actually create the file?
    if not os.path.exists(FILE_PATH):
        print("No CSV file found. The spider might have crashed.")
        return

    # 3. Check if there are actual leads (Line 1 is the header)
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lead_count = len(lines) - 1

        if lead_count <= 0:
            print("No new flash leads found in this run. Skipping email.")
            return

    # 4. Build the Email
    print(f"Found {lead_count} leads. Preparing email...")
    msg = EmailMessage()
    msg['Subject'] = f"🚨 {lead_count} New Real Estate Flash Leads"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content(
        f"Good morning,\n\nYour scraper found {lead_count} new underpriced properties that just hit the market.\n\nSee the attached CSV for the full data breakdown.\n\nBest,\nYour Data Engine")

    # 5. Attach the CSV
    with open(FILE_PATH, 'rb') as f:
        msg.add_attachment(f.read(), maintype='text', subtype='csv', filename="Flash_Leads.csv")

    # 6. Send it via Gmail SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, PASSWORD)
            smtp.send_message(msg)
        print("✅ Email delivered successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


if __name__ == "__main__":
    send_leads()