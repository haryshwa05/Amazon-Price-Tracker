import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


#Enter the url of the product from amazon

url = "https://www.amazon.in/Sony-PS5-PlayStation-Console/dp/B0BRCP72X8/ref=sr_1_1?crid=387661GREKJWA&keywords=ps5&qid=1702136960&s=videogames&sprefix=ps%2Cvideogames%2C189&sr=1-1&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_without_comma = price_without_currency.replace(",","",)
price_as_float = float(price_without_comma)
print(f"Current price is: {price_as_float}")

target_price = price_as_float - ((10/100)*price_as_float) #Taking target price as 10% discount of the original product price
print(f"Target price is: {target_price}")


from_email = "" #Enter your from mail id
to_mail = "" #Enter your to mail id
password = "abc123" #Enter password

#Uncomment the below lines according to the mail id you are using

connection = smtplib.SMTP("smtp.gmail.com")   #G-mail
# connection = smtplib.SMTP("smtp.live.com") #Hotmail
# connection = smtplib.SMTP("smtp.mail.yahoo.com") #Yahoo

connection.starttls()
connection.login(user=from_email, password=password)


if price_as_float <= target_price:
    print("There is a price drop in the product you are interested to buy in Amazon!!!")
    connection.sendmail(from_addr=from_email, to_addrs=to_mail, msg="There is a price drop in the product you are interested to buy in Amazon!!!")

