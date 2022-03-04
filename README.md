# Currency Converter web app
https://mycurrencyconverterproject.herokuapp.com

Website overview:
The project website is a simple forex calculator, able to convert 5 currencies. 

### Features
- currency conversion
- login/registration
- conversion history - only for registered users
- profile update functionality - ability to change username, profile picture, email & password

### Project Summary:
The website is built using the Django framework and is deployed using Heroku (cloud platform as a service). User authentication, profile information and currency exchange rates are stored in PostgreSQL database tables. Images are stored in AWS S3 bucket service.
The repo contains an exchange rate database population script in the scripts directory, which requests data from a stock API (https://www.alphavantage.co/) and inserts formatted information into the database. The script is scheduled to run every 10 mins, updating existing rows. Due to row limitations from the Heroku PostgreSQL database service, only the most recent exchange rates are saved. 

Heroku scheduler:

![274684570_673886677400175_4655635201722705675_n](https://user-images.githubusercontent.com/90049004/156538736-0072b119-0822-4400-bcc2-8748e8189be6.png)

The app uses a free web dyno. Therefore, if the dyno doesn't receive any web traffic in a 30-minute period, it will sleep. In order to avoid this, the website is pinged every 15 minutes using New Relic add-on.

![image](https://user-images.githubusercontent.com/90049004/156754907-e2cd3c11-961d-4e69-967a-5bb1286cb84f.png)

> Website structure and design inspired by CoreyMSchafer and Django documentation.

### Features to be added:
- Delete profile functionality
- Conversion history pagination
- Responsive web design for mobile compatibility
- Currency fluctuation charts

*Disclaimer:
Please refer to the postgres-deployment branch for the deployed version of the website!
The main branch version of the project collects and stores time series data in a Cassandra database with an interval of 15 minutes, tracking currency fluctuations 
for a long period of time, which were initially intended for deployment, however due to some deployment issues, the active website uses only PostgreSQL database.
