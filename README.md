# MEEN-6250-UofU-Covid-Dashboard-Project
This project is for the Programming for Engineers course project and aims to create a dynamic dashboard that displays COVID case and death count information

Package Installs Required for Project
-----------------------------------------------------------------
To run this project, please first install the following packages:
1. bs4
2. html5lib
3. requests
4. json
5. bokeh
6. pandas

Instructions for running the ScrapeWebsite
-----------------------------------------------------------------

1. Import scrape_country from ScrapeWebsite module
2. scrape_country has three parameters: country, url, day <br>
	2.1 country is the name of the country, this variable is not case-sensitive <br>
	2.2 url is the website address of the data source. <br>
	2.3 day has three valid inputs: 'today' will return today's covid data, 'yesterday' will retrun yesterday's covid data, 'yesterday2' will return the covid data form the day before yesterday. 
3. After running the scrape_country, it will automatically print out both the the raw and normalized total case data. The function will also return other detailed COVID data about the input country. The COVID data for all countries will be saved in a JSON file.

Instructions for running the COVIDDashboardApp in Bokeh Server
-----------------------------------------------------------------
The COVID Dashboard App runs from the COVIDDashboardApp.py and is designed to be run on a local bokeh server. To successfully launch and utilize the COVID dashboard do the following:

1. Download the file repository into a zip file. 
2. Extract all files into a folder of your choice. 
3. Launch dashboard using command - bokeh serve --show COVIDDashboardApp.py <br>
	3.1 You can launch the dashboard directly from folder location by opening a command window and entering bokeh serve --show COVIDDashboardApp.py <br>
	3.2 If you are running the code in and VSCode, enter command - bokeh serve --show COVIDDashboardApp.py in the terminal <br>

NOTE: The JSON files included in the repository are not guranteed to be up to date. Upon launching the dashboard in the server, click the update data button 	to pull the most recent three days of data from Worldometer. 
	
Following these steps should launch the dashboard in your browser and will be ready for user interaction. 

Interaction Options Available to User: 

1. Toggle between which day of data to display from the 3 available days of data from JSON files.
2. Select which and how many countries to display data for. 
