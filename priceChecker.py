import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

URL="amazon URL"
price_threshold = int(input())
header_ting={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
#check if it works without header
def get_page():
    desired_page=requests.get(URL,headers=header_ting)
    soup=BeautifulSoup(desired_page.content,'html.parser')

    product_title=soup.find(id="productTitle").get_text() #this has to be exact wrt html id
    print(product_title.strip())

    product_price=soup.find(id="priceblock_ourprice").get_text()
    product_price_int = int(product_price)
    print(product_price_int)
    if product_price_int < price_threshold:
        send_mail()

def send_mail():
    fromMy = 'senderEmail@emailProvider.com' # fun-fact: from is a keyword in python
    to  = 'receiverEmail@emailProvider.com'
    subj='PRICE CHANGE'
    date='1/1/2020'
    message_text='This mail will be sent when the product price goes below a certain threshold.'

    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )

    username = str('senderEmail@emailProvider.com')
    password = str('appPassword') #this is app password
    server = smtplib.SMTP("smtp.mail.yahoo.com",587)
    server.starttls()
    server.login(username,password)
    server.sendmail(fromMy,to,msg)
    server.quit()
    print('ok the email has sent')

get_page()