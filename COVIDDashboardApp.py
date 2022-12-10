# Necessary imports
from math import pi
from bokeh.layouts import row, column
from bokeh.plotting import figure, output_file, show
from bokeh.models.tools import HoverTool
from bokeh.models import FactorRange
from bokeh.transform import cumsum,linear_cmap
from bokeh.palettes import Category20c,Turbo256
from bokeh.io import curdoc
from ScrapeWebsite import scrape_country
from bokeh.models import CustomJS, MultiSelect, ColumnDataSource, RadioButtonGroup, BuiltinIcon, Button, SetValue
import pandas as pd
import json
from NameSort import NameSort

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
    elif day == 'yesterday2':
        # Retrieve the .json file corresponding to 2 days ago
        f = open('two_days_ago.json')
        jsonData = json.load(f)
    else:
        # Display error message
        return f"""{day} is not a valid input for the first argument of the dashboardGenerator() function. Please
input exactly one of the following values: 'today', 'yesterday', or 'two_days_ago'. Use the
format dashboardGenerator(day, countries, dataType, chartType)."""
    return jsonData

todayJSON = selectDay('today')
yesterdayJSON = selectDay('yesterday')
yesterday2JSON = selectDay('yesterday2')

def selectDataType(jsonData, dataType = 'Total Deaths'):
    """_Extract full list of countries and corresponding data type values from jsonData_

    Args:
        jsonData (_list_): _List of dictionaries including all COVID related data for every country_
        
        dataType (_str_ or _list_): _Specifies the data type of interest for the first figure in
            the COVID dashboard. Print the list variable allDataTypes for a list of valid inputs.
            NOTE: If chartType == 'circle' then dataType must be a list of two strings where
            each string specifies a data type from the variable allDataTypes. The first element
            in the list will be placed on the x axis and the second element in the list will be
            placed on the y axis_

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
            return f"""Invalid input for the dataType argument of the dashboardGenerator() function.
No such dataType as {dataType}. Please input exactly one of the values from the following list:

    ['TotalDeaths', 'NewDeaths', 'ActiveCases', 'Serious,Critical', 'TotalCases', 'NewCases',
    'New Deaths/1M pop', 'Deaths/1M pop', 'Population', 'TotalRecovered', 'NewRecovered',
    'TotCases/1M pop', 'TotalTests', 'Tests/1M pop', '1 Caseevery X ppl', '1 Deathevery X ppl',
    '1 Testevery X ppl', 'New Cases/1M pop', 'Active Cases/1M pop']

Use the format dashboardGenerator(day, countries, dataType, chartType)."""
    # return a dictionary of countries and the values of the specific data type of interest
    return dict(zip(allCountries, allDisplayData))


#Total Death data 
tTotDeath = selectDataType(todayJSON,'TotalDeaths')
yTotDeath = selectDataType(yesterdayJSON,'TotalDeaths')
y2TotDeath = selectDataType(yesterday2JSON,'TotalDeaths')

#print(y2TotDeath)
#print(tTotDeath)

# Death per 1m population
tDeaths = selectDataType(todayJSON,'Deaths/1M pop')
yDeaths = selectDataType(yesterdayJSON,'Deaths/1M pop')
y2Deaths = selectDataType(yesterday2JSON,'Deaths/1M pop')

# Total Cases 
tCases = selectDataType(todayJSON,'TotalCases')
yCases = selectDataType(yesterdayJSON,'TotalCases')
y2Cases = selectDataType(yesterday2JSON,'TotalCases')

#print(tCases)

def selectCountryData(allDataType, dataType, day, countries = 'all'):
    """_Extracts only data corresponding to countries of interest_

    Args:
        allDataType (_dict_): _dictionary where the keys are all of the countries and the values contain
            the specific data type of interest_
        
        dataType (_str_ or _list_): _Specifies the data type of interest for the first figure in
            the COVID dashboard. Print the list variable allDataTypes for a list of valid inputs.
            NOTE: If chartType == 'circle' then dataType must be a list of two strings where
            each string specifies a data type from the variable allDataTypes. The first element
            in the list will be placed on the x axis and the second element in the list will be
            placed on the y axis_
        
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

defaultCountries = ['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam',
                'Australia', 'Argentina', 'Netherlands', 'Taiwan', 'Iran', 'Mexico', 'Indonesia']


tTDFilt = selectCountryData(tTotDeath, 'TotalDeaths','today',defaultCountries)
tCFilt = selectCountryData(tCases,'TotalCases','today', defaultCountries)
print(tCFilt)

countries = list(tTDFilt.keys())
TDvalues = list(tTDFilt.values())
tCValues = list(tCFilt.values())
print(tCValues)

   
TDdata = dict(x = TDvalues,
            y = countries,
            )  

#print(tTDFiltdata)
radii = [x/max(tCValues)*2 for x in tCValues]
#Define Color mapping for circles: 
#mapper = linear_cmap(field_name='Total Deaths', palette = Turbo256, low=min(TCTDdata['y']), high=max(TCTDdata['y']))
colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / max(tCValues))), 255) for value in tCValues]

TCTDdata = dict(x = tCValues,
                y = TDvalues,
                countries = countries,
                color = colors)

TCTDsource = ColumnDataSource(data = TCTDdata)


TDsource = ColumnDataSource(data=TDdata)


# Create figure for total deaths
TDp = figure(
    y_range = FactorRange(factors = TDdata['y']),
    width = 800,
    title = 'Total COVID Deaths by Country',
    x_axis_label = 'Total Deaths',
    y_axis_label = 'Countries',
    tools = "pan, wheel_zoom, box_zoom, save, reset",
)

#Render Glyph
TDp.hbar(
    y = 'y',
    right = 'x',
    left = 0,
    height = 0.2,
    color = 'blue',
    fill_alpha = 0.5,
    source = TDsource,
)

#Add Hover tool functionality
TDp.add_tools(HoverTool(tooltips = [('Country',"@y"),('Total Deaths',"@x")]))


#Create a scatter plot of total deaths vs. total cases
TDvTCp = figure(
    width = 600,
    title = 'Total Deaths vs Total Cases by Country',
    x_axis_label = 'Total Cases',
    y_axis_label = 'Total Deaths',
    height = 400,
    tools = "pan, wheel_zoom, box_zoom, save, reset",
    tooltips = [("Country","@countries"),('Total Cases','@x'),('Total Deaths','@y')],
)

#Create Glyph 
TDvTCp.circle(
    x = 'x',
    y = 'y',
    size = 10,
    fill_color = 'blue',
    line_color = "lightgrey",
    fill_alpha = 0.6,
    source = TCTDsource,    
)

# Define Multiselect tool 
# Create a tupled alphabetical list of the options in the drop down
Countries_sorted = NameSort(list(allCountries))

OPTIONS = []
for i in range(len(Countries_sorted)-1):
    OPTIONS.append(tuple((f'{i}',Countries_sorted[i])))

#print(OPTIONS)


#['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam',
#                'Australia', 'Argentina', 'Netherlands', 'Taiwan', 'Iran', 'Mexico', 'Indonesia']

# Create Input options for the chart.
multi_select = MultiSelect(title = "Countries:",
                           value=['216','94','72','78','26','171','104','101','215','168','211','193','224','10','7','146','202','96','133','95'], 
                           options = OPTIONS,
                           width = 200,
                           height = 200)

#Data selection Option
DateLabels = ['Today','Yesterday','Two Days Ago']

date_select = RadioButtonGroup(labels=DateLabels,active=0)

#Button for updating all data
UpdateData = Button(label='Update Data', button_type = 'primary')


# Define Dynamic Update Behavior
def update():
    #Update Country shown
    index = multi_select.value
    countries = [multi_select.options[int(x)][1] for x in index]
    
    #Update date for data set
    dateActive = date_select.active
    if dateActive == 0:
        day = 'today'
        inputData = tTotDeath
        inputData2 = tCases
    if dateActive == 1:
        day = 'yesterday'
        inputData = yTotDeath
        inputData2 = yCases
    if dateActive == 2:
        day = 'yesterday2'
        inputData = y2TotDeath
        inputData2 = y2Cases
    
    TDFilt = selectCountryData(inputData, 'TotalDeaths', day, countries)
    tCFilt = selectCountryData(inputData2,'TotalCases', day, countries)
    
    TDcountries = list(TDFilt.keys())
    TotDeath = list(TDFilt.values())
    TotCase = list(tCFilt.values())
    
    TDdata = dict(x = TotDeath,
            y = TDcountries,) 
    
    TDsource.data = TDdata
    TDp.y_range.factors = list(TDdata['y'])
    
    radii = [x/max(TotCase)*2 for x in TotCase]

    TCTDdata = dict(x = TotCase,
                y = TotDeath,
                countries = TDcountries,
                radius = radii)
    
    TCTDsource.data = TCTDdata

    
#Degine Button update    
def ButtonUpdate():
    # Pull New json files using scrape_website
    scrape_country('USA','https://www.worldometers.info/coronavirus/','today')
    scrape_country('USA','https://www.worldometers.info/coronavirus/','yesterday')
    scrape_country('USA','https://www.worldometers.info/coronavirus/','yesterday2') 
     
    #Process new json files
    todayJSON = selectDay('today')
    yesterdayJSON = selectDay('yesterday')
    yesterday2JSON = selectDay('yesterday2')
    
    
    
    
 
    
multi_select.on_change('value', lambda attr, old, new: update())
date_select.on_change('active', lambda attr,old, new: update())
#UpdateData.on_click(
update()

curdoc().add_root(column(row(date_select),row(TDp,multi_select,TDvTCp)))




