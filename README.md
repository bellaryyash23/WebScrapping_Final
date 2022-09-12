# 🏡Housing Rental Data Collection using BeautifulSoup and Selenium of Python

🌟A program which helps you collects rental housing data of a particular location using web scraping and then uses google form to format this data so that the responses can be
viewed in google spreadsheet for easy analysis. 

🌟It uses Beautiful Soup package for web scrraping i.e. getting the data like rental price, address, link of listing and the process of filling of google form is automated
using the Selenium driver package.

👉In the 'main.py' file, first the data is scraped from the website using Beautiful Soup. The requests module is used to load the html data from website which is stored 
as response.

![Website for Data Scraping](https://github.com/bellaryyash23/WebScrapping_Final/blob/master/samples/website.jpg?raw=true)

👆Website used for Data Scraping👆

👉This collected raw html data is parsed using the BeautifulSoup object. During this the required data is collected and stored in python lists. This process of data
collection is achieved using the '.find_all()' method of the BeautifulSoup.

👉Now in order for better visualization of this acquired data we can use google spreadsheet but, the process of data entry is quite tiring and repetitive. This can be automated
using the Selenium to design a bot to fill these details for us.

👉For this a Google form is created which can be used to format the data. Then the Selenium driver can be made to fill this form using the data previously collected by Web scraping
using BeautifulSoup.

👉The Google form is as follows:

![Google Form to Format collected Data](https://github.com/bellaryyash23/WebScrapping_Final/blob/master/samples/form.JPG?raw=true)

👆Google Form to Format collected Data👆

👉The Selenium driver is passed the URL of the Google Form and it can be filled automatically with the data collected previously using '.send_keys()', '.click()' and other methods.

![Automated Data Entry](https://github.com/bellaryyash23/WebScrapping_Final/blob/master/samples/add_data.gif?raw=true)

👆Automated Data Entry Bot👆

👉Thus, using Web Scraping by BeautifulSoup and Automated Data Entry by Selenium package, the unorganized and scattered data gets formated into a well oriented and 
organized Google Sheet which the user can use to analyse the data.

![Response gathered from Google form stored in Google Sheet](https://github.com/bellaryyash23/WebScrapping_Final/blob/master/samples/response.jpg?raw=true)

👆Response gathered from Google form stored in Google Sheet👆
