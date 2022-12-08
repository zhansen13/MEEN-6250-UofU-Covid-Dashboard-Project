# Necessary imports
from math import pi
from bokeh.layouts import row, column
from bokeh.plotting import figure, output_file, show
from bokeh.models.tools import HoverTool
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
from ScrapeWebsite import scrape_country
import pandas as pd
import json

# Scrape fresh data from the worldometers site
scrape_country('USA','https://www.worldometers.info/coronavirus/','today')
scrape_country('USA','https://www.worldometers.info/coronavirus/','yesterday')
scrape_country('USA','https://www.worldometers.info/coronavirus/','yesterday2')

# Generate a list of all valid countries
allCountries = ['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam',
                'Australia', 'Argentina', 'Netherlands', 'Taiwan', 'Iran', 'Mexico', 'Indonesia', 'Poland', 'Colombia', 'Austria',
                'Portugal', 'Greece', 'Ukraine', 'Malaysia', 'Chile', 'DPRK', 'Israel', 'Thailand', 'Belgium', 'Czechia', 'Canada',
                'Switzerland', 'Peru', 'Philippines', 'South Africa', 'Romania', 'Denmark', 'Sweden', 'Iraq', 'Serbia', 'Hong Kong',
                'Singapore', 'Hungary', 'Bangladesh', 'New Zealand', 'Slovakia', 'Georgia', 'Jordan', 'Ireland', 'Pakistan', 'Norway',
                'Finland', 'Kazakhstan', 'Bulgaria', 'Lithuania', 'Morocco', 'Slovenia', 'Croatia', 'Lebanon', 'Guatemala', 'Costa Rica',
                'Tunisia', 'Bolivia', 'Cuba', 'UAE', 'Ecuador', 'Panama', 'Nepal', 'Uruguay', 'Belarus', 'Mongolia', 'Latvia',
                'Saudi Arabia', 'Azerbaijan', 'Paraguay', 'Bahrain', 'Sri Lanka', 'Kuwait', 'Dominican Republic', 'Myanmar', 'Palestine',
                'Cyprus', 'Estonia', 'Moldova', 'Venezuela', 'Egypt', 'Libya', 'Ethiopia', 'Qatar', 'Réunion', 'Honduras', 'Armenia',
                'Bosnia and Herzegovina', 'Oman', 'North Macedonia', 'Kenya', 'Zambia', 'Albania', 'Botswana', 'Luxembourg', 'Montenegro',
                'Algeria', 'Nigeria', 'Zimbabwe', 'Uzbekistan', 'Brunei', 'Mozambique', 'Martinique', 'Laos', 'Iceland', 'Kyrgyzstan',
                'Afghanistan', 'El Salvador', 'Guadeloupe', 'Maldives', 'Trinidad and Tobago', 'Ghana', 'Namibia', 'Uganda', 'Jamaica', 
                'Cambodia', 'Rwanda', 'Cameroon', 'Malta', 'Angola', 'Barbados', 'French Guiana', 'Channel Islands', 'DRC', 'Senegal',
                'Malawi', 'Ivory Coast', 'Suriname', 'French Polynesia', 'New Caledonia', 'Eswatini', 'Guyana', 'Belize', 'Fiji',
                'Madagascar', 'Sudan', 'Mauritania', 'Cabo Verde', 'Bhutan', 'Syria', 'Burundi', 'Seychelles', 'Gabon', 'Andorra',
                'Papua New Guinea', 'Curaçao', 'Aruba', 'Mayotte', 'Mauritius', 'Tanzania', 'Togo', 'Guinea', 'Isle of Man', 'Bahamas',
                'Faeroe Islands', 'Lesotho', 'Haiti', 'Mali', 'Cayman Islands', 'Saint Lucia', 'Benin', 'Somalia', 'Congo',
                'Solomon Islands', 'Timor-Leste', 'San Marino', 'Micronesia', 'Burkina Faso', 'Liechtenstein', 'Gibraltar', 'Grenada',
                'Bermuda', 'Nicaragua', 'South Sudan', 'Tajikistan', 'Equatorial Guinea', 'Tonga', 'Samoa', 'Dominica', 'Djibouti',
                'Monaco', 'Marshall Islands', 'CAR', 'Gambia', 'Saint Martin', 'Greenland', 'Vanuatu', 'Yemen', 'Caribbean Netherlands',
                'Sint Maarten', 'Eritrea', 'Niger', 'Antigua and Barbuda', 'Comoros', 'Guinea-Bissau', 'Liberia', 'Sierra Leone', 'Chad',
                'British Virgin Islands', 'St. Vincent Grenadines', 'Saint Kitts and Nevis', 'Turks and Caicos', 'Cook Islands',
                'Sao Tome and Principe', 'Palau', 'St. Barth', 'Nauru', 'Anguilla', 'Kiribati', 'Saint Pierre Miquelon', 'Tuvalu',
                'Falkland Islands', 'Saint Helena', 'Montserrat', 'Macao', 'Wallis and Futuna', 'Diamond Princess', 'Niue',
                'Vatican City', 'Western Sahara', 'MS Zaandam', 'China']

# Create a dictionary of chart titles for each day
title_today = {'TotalDeaths':'Total COVID Deaths by Country as of Today', 'NewDeaths':'New COVID Deaths By Country as of Today',
              'ActiveCases':'Active COVID Cases by Country as of Today', 'Serious,Critical':'Critical COVID Cases by Country as of Today',
              'TotalCases':'Total COVID Cases by Country as of Today', 'NewCases': 'New COVID Cases by Country as of Today',
              'New Deaths/1M pop':'New COVID Deaths per 1M People by Country as of Today',
              'Deaths/1M pop':'Total COVID Deaths per 1M People by Country as of Today',
              'Population':'Population by Country as of Today',
              'TotalRecovered':'Total Number of People Who have Recovered from COVID by Country as of Today', 
              'NewRecovered':'Number of People Who Recovered from COVID Today by Country',
              'TotCases/1M pop':'Total Number of COVID Cases per 1M People by Country as of Today',
              'TotalTests':'Total Number of COVID Tests Taken by Country as of Today',
              'Tests/1M pop':'Number of COVID Tests Taken per 1M People by Country as of Today',
              '1 Caseevery X ppl':'1 COVID Case per X People by Country as of Today',
              '1 Deathevery X ppl':'1 COVID Related Death per X People by Country as of Today',
              '1 Testevery X ppl':'1 COVID Test per X People by Country as of Today',
              'New Cases/1M pop':'Number of New COVID Cases per 1M People by Country as of Today',
              'Active Cases/1M pop':'Number of Active COVID Cases per 1M People by Country as of Today'
            }
title_yesterday = {'TotalDeaths':'Total COVID Deaths by Country as of Yesterday', 'NewDeaths':'New COVID Deaths By Country as of Yesterday',
              'ActiveCases':'Active COVID Cases by Country as of Yesterday', 'Serious,Critical':'Critical COVID Cases by Country as of Yesterday',
              'TotalCases':'Total COVID Cases by Country as of Yesterday', 'NewCases': 'New COVID Cases by Country as of Yesterday',
              'New Deaths/1M pop':'New COVID Deaths per 1M People by Country as of Yesterday',
              'Deaths/1M pop':'Total COVID Deaths per 1M People by Country as of Yesterday',
              'Population':'Population by Country as of Yesterday',
              'TotalRecovered':'Total Number of People Who have Recovered from COVID by Country as of Yesterday', 
              'NewRecovered':'Number of People Who Recovered from COVID Yesterday by Country',
              'TotCases/1M pop':'Total Number of COVID Cases per 1M People by Country as of Yesterday',
              'TotalTests':'Total Number of COVID Tests Taken by Country as of Yesterday',
              'Tests/1M pop':'Number of COVID Tests Taken per 1M People by Country as of Yesterday',
              '1 Caseevery X ppl':'1 COVID Case per X People by Country as of Yesterday',
              '1 Deathevery X ppl':'1 COVID Related Death per X People by Country as of Yesterday',
              '1 Testevery X ppl':'1 COVID Test per X People by Country as of Yesterday',
              'New Cases/1M pop':'Number of New COVID Cases per 1M People by Country as of Yesterday',
              'Active Cases/1M pop':'Number of Active COVID Cases per 1M People by Country as of Yesterday'
            }
title_two_days_ago = {'TotalDeaths':'Total COVID Deaths by Country as of Two Days Ago', 'NewDeaths':'New COVID Deaths By Country as of Two Days Ago',
              'ActiveCases':'Active COVID Cases by Country as of Two Days Ago', 'Serious,Critical':'Critical COVID Cases by Country as of Two Days Ago',
              'TotalCases':'Total COVID Cases by Country as of Two Days Ago', 'NewCases': 'New COVID Cases by Country as of Two Days Ago',
              'New Deaths/1M pop':'New COVID Deaths per 1M People by Country as of Two Days Ago',
              'Deaths/1M pop':'Total COVID Deaths per 1M People by Country as of Two Days Ago',
              'Population':'Population by Country as of Two Days Ago',
              'TotalRecovered':'Total Number of People Who have Recovered from COVID by Country as of Two Days Ago', 
              'NewRecovered':'Number of People Who Recovered from COVID Two Days Ago by Country',
              'TotCases/1M pop':'Total Number of COVID Cases per 1M People by Country as of Two Days Ago',
              'TotalTests':'Total Number of COVID Tests Taken by Country as of Two Days Ago',
              'Tests/1M pop':'Number of COVID Tests Taken per 1M People by Country as of Two Days Ago',
              '1 Caseevery X ppl':'1 COVID Case per X People by Country as of Two Days Ago',
              '1 Deathevery X ppl':'1 COVID Related Death per X People by Country as of Two Days Ago',
              '1 Testevery X ppl':'1 COVID Test per X People by Country as of Two Days Ago',
              'New Cases/1M pop':'Number of New COVID Cases per 1M People by Country as of Two Days Ago',
              'Active Cases/1M pop':'Number of Active COVID Cases per 1M People by Country as of Two Days Ago'
            }
# Create a dictionary of x labels
xlabel = {'TotalDeaths':'Total Deaths', 'NewDeaths':'New Deaths',
              'ActiveCases':'Active Cases', 'Serious,Critical':'Critical Cases', 'TotalCases':'Total Cases', 'NewCases': 'New Cases',
              'New Deaths/1M pop':'New Deaths/1M', 'Deaths/1M pop':'Total Deaths/1M', 'Population':'People', 
              'TotalRecovered':'Total Recovered', 'NewRecovered':'New Recovered', 'TotCases/1M pop':'Total Cases/1M',
              'TotalTests':'Total Tests', 'Tests/1M pop':'Total Tests/1M', '1 Caseevery X ppl':'People', '1 Deathevery X ppl':'People',
              '1 Testevery X ppl':'People', 'New Cases/1M pop':'New Cases/1M', 'Active Cases/1M pop':'Active Cases/1M'
            }

allDataTypes = list(xlabel.keys())

def selectDay(day = 'today'):
    """_Retrieves COVID data from a .json file corresponding to the day input argument and stores it as a
            list of dictionaries. Also initaites an output .html file named Dashboard.html_

    Args:
        day (_str_): _Specify the day of interest. Valid inputs are 'today', 'yesterday', and 'two_days_ago'.
            Default value is 'today'._

    Returns:
        _list_: _a list of dictionaries including all COVID related data for every country_
    """
    # Specify output .html file
    output_file('Dashboard.html')
    if day == 'today':
        # Retrieve the .json file corresponding to today
        f = open('today.json')
        jsonData = json.load(f)
    elif day == 'yesterday':
        # Retrieve the .json file corresponding to yesterday
        f = open('yesterday.json')
        jsonData = json.load(f)
    elif day == 'two_days_ago':
        # Retrieve the .json file corresponding to 2 days ago
        f = open('two_days_ago.json')
        jsonData = json.load(f)
    else:
        # Display error message
        return f"""{day} is not a valid input for the first argument of the dashboardGenerator() function. Please
input exactly one of the following values: 'today', 'yesterday', or 'two_days_ago'. Use the
format dashboardGenerator(day, countries, dataType, chartType)."""
    return jsonData

def selectDataType(jsonData, dataType = 'Total Deaths'):
    """_Extract full list of countries and corresponding data type values from jsonData_

    Args:
        jsonData (_list_): _List of dictionaries including all COVID related data for every country_
        
        dataType (_str_): _Specifies the data type of interest. Print the list variable allDataTypes
            for a list of valid inputs for dataType_

    Returns:
        _dict_: _A dictionary where the keys are all countries and the values contain the data from the
            specific data type of interest specified from dataType_
    """
    # Collect Data from .json file
    allCountries = list()
    allDisplayData = list()
    for i in range(len(jsonData)-1):
        try:
            # If the data field is blank, skip that country
            if jsonData[i][dataType] == "":
                pass
            else:
                # Collect json data for each country
                allCountries.append(jsonData[i]['Country,Other'])
                # Clean the string to save as type int
                allDisplayData.append(int(jsonData[i][dataType].replace('+','').replace(',','')))
        except Exception as e:
            return f"""Invalid input for the third argument of the dashboardGenerator() function.
No such dataType as {dataType}. Please input exactly one of the values from the following list:

    ['TotalDeaths', 'NewDeaths', 'ActiveCases', 'Serious,Critical', 'TotalCases', 'NewCases',
    'New Deaths/1M pop', 'Deaths/1M pop', 'Population', 'TotalRecovered', 'NewRecovered',
    'TotCases/1M pop', 'TotalTests', 'Tests/1M pop', '1 Caseevery X ppl', '1 Deathevery X ppl',
    '1 Testevery X ppl', 'New Cases/1M pop', 'Active Cases/1M pop']

Use the format dashboardGenerator(day, countries, dataType, chartType)."""
    # return a dictionary of countries and the values of the specific data type of interest
    return dict(zip(allCountries, allDisplayData))

def selectCountryData(allDataType, dataType, day, countries = 'all'):
    """_Extracts only data corresponding to countries of interest_

    Args:
        allDataType (_dict_): _dictionary where the keys are all of the countries and the values contain
            the specific data type of interest_
        
        dataType (_str_): _Specifies the data type of interest. Print the list variable allDataTypes
            for a list of valid inputs for dataType_
        
        day (_str_): _Specify the day of interest. Valid inputs are 'today', 'yesterday', and 'two_days_ago'_
        
        countries (_list_): _list containing countries of interest_

    Returns:
        _dict_: _returns a dictionary where the keys are only countries of interest specified in the countries list
            and the values contain the data from the specific data type of interest specified from dataType_
    """
    # Extract only the values from the master list that correspond to the countries of interest
    values = list()
    errors = list()
    for i in range(len(countries)):
        # If no data is available for a county of interest, print an error statement.
        try:
            values.append(allDataType[countries[i]])
        except Exception as e:
            values.append('No Data Available')
            print(f"Unfortunately the {xlabel[dataType]} data for {countries[i]} is not available for {day.replace('_',' ')}.")
            errors.append(i)
    # Combine the countries of interest with the values of interest in a dictionary.
    dict_data = dict(zip(countries, values))
    # Remove any countries that have error statements.
    for i in range(len(errors)):
        del dict_data[countries[errors[i]]]
    return dict_data

def selectChart(chartType, dict_data, day, dataType):
    """selectChart() generates a plot from the dictionary key-value pairs provided as dict_data.

    Args:
        chartType (_str_): _specify the desired chart style. Valid inputs include _
        
        dict_data (_dict_): _dictionary with countries of interest and values of the specified
            data type from arg4_
        
        day (_int_): _specify the day to extract the data from. Valid inputs include 'today',
            'yesterday', and 'two_days_ago'_
        
        dataType (_str_): _Specifies the data type of interest. Print the list variable allDataTypes
            for a list of valid inputs for dataType_

    Returns:
        _bokeh.plotting._figure.figure_: _returns a figure assignment. Use show() to generate the figure_
    """
    # Seperate dict_data keys and values into seperate lists
    countries = list(dict_data.keys())
    displayData = list(dict_data.values())
    # Set chart title based on day and dataType
    if day == 'today':
        title = title_today[dataType]
    elif day == 'yesterday':
        title = title_yesterday[dataType]
    elif day == 'two_days_ago':
        title = title_two_days_ago[dataType]
    # Set dynamic height for h_bar figure
    if int(len(countries)/2*100) < 400:
        height_hbar = 400
        height_pie = 400
    else:
        height_hbar = int(len(countries)*50)
        height_pie = int(len(countries)*28)
    # Generate hbar figure
    if chartType == 'hbar':
        # Set figure specifications
        chart = figure(
            y_range = countries,
            width = 800,
            height = height_hbar,
            title = title,
            x_axis_label = xlabel[dataType],
            tools = "pan, box_select, zoom_in, zoom_out, save, reset"
        )
        # Render Glyph
        chart.hbar(
            y = countries,
            right = displayData,
            left = 0,
            height = 0.2,
            color = 'blue',
            fill_alpha = 0.5
        )
        # Add Tooltips (HoverTool)
        chart.add_tools(HoverTool(tooltips = [("Country", "@y"),(dataType, "@right")]))
        return chart
    # Generate pie figure
    elif chartType == 'pie':
        # Return error if more than 20 countries
        if len(dict_data) > 20:
            return f"""Maximum number of countries exceded. Length of input countries list is limited to 20 for chartType pie.
Consider an hbar plot to display more countries."""
        else:
            # Format data using pandas
            data = pd.Series(dict_data).reset_index(name='value').rename(columns={'index': 'country'})
            data['angle'] = data['value']/data['value'].sum() * 2*pi
            data['color'] = Category20c[len(dict_data)]
            # Format pie chart
            chart = figure(height=height_pie, title=title,
            tools= "pan, zoom_in, zoom_out, save, reset, hover",
            tooltips=[("Country","@country"),(dataType, "@value")], x_range=(-0.5, 1.0))
            chart.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=data)
            chart.axis.axis_label = None
            chart.axis.visible = False
            chart.grid.grid_line_color = None
            return chart
        
def figureGenerator(day, countries, dataType, chartType):
    """_Will generate a COVID dashboard from the specified input arguments_

    Args:
        day (_str_): _specify the day to extract the data from. Valid inputs include 'today',
            'yesterday', and 'two_days_ago'_
        
        countries (_list_): _list containing countries of interest. Can also use the list variable allCountries. Print
        list variable allCountries for a list of valid countries_
        
        dataType (_str_): _Specifies the data type of interest. Print the list variable allDataTypes
            for a list of valid inputs for dataType_
        
        chartType (_string_): _specify the type of plot to display. Valid inputs include 'hbar' and 'pie'._
    """
    jsonData = selectDay(day)
    if type(jsonData) == str:
        print(jsonData)
    else:
        allDataType = selectDataType(jsonData, dataType)
        if type(allDataType) == str:
            print(allDataType)
        else:
            dict_data = selectCountryData(allDataType, dataType, day, countries)
            # allDataType2 = selectDataType(dataType2)
            chart = selectChart(chartType, dict_data, day, dataType)
            if type(chart) == str:
                return chart
            else:
                #chart2 = selectChart('pie')
                # Show Results
                return chart

def dashboardGenerator(day1, countries1, dataType1, chartType1,
                       day2, countries2, dataType2, chartType2):
    chart1 = figureGenerator(day1, countries1, dataType1, chartType1)
    chart2 = figureGenerator(day2, countries2, dataType2, chartType2)
    if type(chart1) == str:
        print(chart1)
    elif type(chart2) == str:
        print(chart2)
    else:
        show(row(chart1, chart2))
    
    

#countries1 = ['USA','Chile','Mexico','France','Niue']
countries2 = ['India','Germany','Brazil','Japan','Italy']
countries = ['USA', 'China', 'UK', 'Spain', 'S. Korea', 'Hong Kong','South Africa', 'Italy', 'Japan', 'France', 'Mexico']
countries3 = ['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam',
                'Australia', 'Argentina', 'Netherlands', 'Taiwan', 'Iran', 'Mexico', 'Indonesia']

dashboardGenerator('two_days_ago', countries2, 'TotalCases', 'pie',
                   'today', allCountries, 'TotalDeaths', 'hbar')
