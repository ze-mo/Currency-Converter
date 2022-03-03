# Currency Converter webapp
https://mycurrencyconverterproject.herokuapp.com

Website overview:
The project website is a simple forex calculator, able to convert up to 5 currencies with an accurracy of 10 mins. It offers conversion history of registered users and profile updates, such as changing profile picture, email, username and password.

### Features
- currency conversion
- login/registration
- conversion history
- profile update functionality

### Project Summary:
The website is built using the Django framework and is deployed using Heroku (cloud platform as a service). User authentication, profile information and currency exchange rates are stored in PostgreSQL database tables. Images are stored in AWS S3 bucket service.
The repo contains an exchange rate database population script in the scripts directory, which requests data from a stock API (https://www.alphavantage.co/) and inserts formatted information into the database. The script is scheduled to run every 10 mins, updating existing rows. Due to row limitations from the Heroku PostgreSQL database service, only the most recent exchange rates are saved. 

Heroku scheduler:

![274684570_673886677400175_4655635201722705675_n](https://user-images.githubusercontent.com/90049004/156538736-0072b119-0822-4400-bcc2-8748e8189be6.png)

The app uses a free web dyno. Therefore, if the dyno doesn't receive no web traffic in a 30-minute period, it will sleep. In order to avoid this, the website is pinged every 15 minutes.

![274204619_930172414342331_8691057965165666922_n](https://user-images.githubusercontent.com/90049004/156539231-9436bd96-259d-4e80-86c0-d87e220ab79e.png)

> Website structure and design inspired by CoreyMSchafer and Django documentation.

### Features to be added:
- delete profile functionality
- Conversion history pagination
- Responsive web design for mobile compatibility
- Currency fluctuation charts

Known issues:
- Email used for sending password confirmation emails is unreliable, due to Gmail policy which automatically disables sending emails from 3rd party apps after a certain amount of time. Issue is temporarily handled by a cron job.


*Disclaimer:
Please refer to the postgres-deployment branch for the deployed version of the website!
The main branch contains a project structure with a MySQL, SQLite3 and Cassandra databases, which were initially intended for deployment,
however due to some deployment issues, the active website uses only PostgreSQL database.
