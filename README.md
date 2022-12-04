# MEEN-6250-UofU-Covid-Dashboard-Project
This project is for the programming for engineers course project and aims to create a dynamic dashboard that displays COVID case and death count information

Instructions for running the ScrapeWebsite
-----------------------------------------------------------------
To run this project, please first install the following package:
1. bs4
2. lxml
3. requests
4. json
-----------------------------------------------------------------

1. Import scrape_country from ScrapeWebsite module
2. scrape_country has three parameters: country, url, day
	2.1 country is the name of the country, this variable is not case-sensitive
	2.2 url is the website address of the data source. 
	2.3 day has three valid values: 'today' will return today's covid data, 'yesterday' will retrun yesterday's covid data, 'yesterday2' will return the covid data form the day before yesterday. 
3. After run the scrape_country, it will automatically print out the raw data of the total case and normalized data of the total case. The function will also return other detailed covid data of the input country. The covid data for all countries will be saved in a Json file.
