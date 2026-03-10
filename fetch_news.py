import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import os

def fetch_tapestry_news():
    """Fetch latest Tapestry news"""
    try:
        # Using a news API (you'll need to sign up for an API key)
        # Alternative: Use web scraping with BeautifulSoup
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(
            'https://www.bing.com/news/search?q=Tapestry+company',
            headers=headers,
            timeout=10
        )
        return response.text
    except Exception as e:
        return f"Error fetching news: {str(e)}"

def send_email(content):
    """Send email with news content"""
    sender_email = os.getenv('GMAIL_USER')
    sender_password = os.getenv('GMAIL_PASSWORD')
    receiver_email = 'sharon.wong@wisetechglobal.com'
    
    msg = MIMEMultipart()
    msg['Subject'] = f"Daily Tapestry News Report - {datetime.date.today()}"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    msg.attach(MIMEText(content, 'html'))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

if __name__ == '__main__':
    news = fetch_tapestry_news()
    send_email(news)
