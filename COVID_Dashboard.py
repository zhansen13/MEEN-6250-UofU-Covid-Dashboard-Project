# Necessary imports
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from ScrapeWebsite import scrape_country
import json



title_today = {'TotalDeaths':'Total COVID Deaths by Country as of Today', 'NewDeaths':'COVID Deaths By Country as of Today',
              'ActiveCases':'Active COVID Cases by Country as of Today', 'Serious,Critical':'Critical COVID Cases by Country as of Today',
              'TotalCases':'Total COVID Cases by Country as of Today', 'NewCases': 'New COVID Cases by Country as of Today',
              'New Deaths/1M pop':'New COVID Deaths per 1M People Country as of Today',
              'Deaths/1M pop':'Total COVID Deaths per 1M People per Country as of Today',
              'Population':'Population by Country as of Today'
            }
title_yesterday = {'TotalDeaths':'Total COVID Deaths by Country as of Yesterday', 'NewDeaths':'COVID Deaths By Country as of Yesterday',
              'ActiveCases':'Active COVID Cases by Country as of Yesterday', 'Serious,Critical':'Critical COVID Cases by Country as of Yesterday',
              'TotalCases':'Total COVID Cases by Country as of Yesterday', 'NewCases': 'New COVID Cases by Country as of Yesterday',
              'New Deaths/1M pop':'New COVID Deaths per 1M People Country as of Yesterday',
              'Deaths/1M pop':'Total COVID Deaths per 1M People per Country as of Yesterday',
              'Population':'Population by Country as of Yesterday'
            }
title_two_days_ago = {'TotalDeaths':'Total COVID Deaths by Country as of Two Days Ago', 'NewDeaths':'COVID Deaths By Country as of Two Days Ago',
              'ActiveCases':'Active COVID Cases by Country as of Two Days Ago', 'Serious,Critical':'Critical COVID Cases by Country as of Two Days Ago',
              'TotalCases':'Total COVID Cases by Country as of Two Days Ago', 'NewCases': 'New COVID Cases by Country as of Two Days Ago',
              'New Deaths/1M pop':'New COVID Deaths per 1M People Country as of Two Days Ago',
              'Deaths/1M pop':'Total COVID Deaths per 1M People per Country as of Two Days Ago',
              'Population':'Population by Country as of Two Days Ago'
            }
xlabel = {'TotalDeaths':'Deaths', 'NewDeaths':'New Deaths',
              'ActiveCases':'Active Cases', 'Serious,Critical':'Critical Cases', 'TotalCases':'Total Cases', 'NewCases': 'New Cases',
              'New Deaths/1M pop':'New Deaths/1M', 'Deaths/1M pop':'Total Deaths/1M', 'Population':'People'
            }

def selectDay(day = 'today'):
    """The selectDay() function accepts a single string input. Valid
    inputs are 'today', 'yesterday', and 'two_days_ago'. The function
    will retrieve COVID data from a .json file corresponding to the
    selected day and store it as a list of dictionaries. This
    function will also initiate an output .html file named
    Dashboard.html"""
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
        return f"{day} is not a valid input for selectDay(). Please input exactly one of the following values: 'today', 'yesterday', or 'yesterday2'."
    return jsonData

def selectDataType(jsonData, dataType = 'Total Deaths'):
    # Collect Data from .json file
    allCountries = list()
    allDisplayData = list()
    for i in range(len(jsonData)-1):
        # If the data field is blank, skip that country
        if jsonData[i]['TotalDeaths'] == '':
            pass
        else:
            allCountries.append(jsonData[i]['Country,Other'])
            allDisplayData.append(int(jsonData[i]['TotalDeaths'].replace('+','').replace(',','')))
    return dict(zip(allCountries, allDisplayData))

def selectCountryData(countries, allDataType):
    values = list()
    for i in range(len(countries)):
        values.append(allDataType[countries[i]])
    dict_data = dict(zip(countries, values))
    return dict_data

def selectChart(chartType, dict_data, day, dataType):
    if day == 'today':
        title = title_today[dataType]
    elif day == 'yesterday':
        title = title_yesterday[dataType]
    elif day == 'two_days_ago':
        title = title_two_days_ago[dataType]
    countries = list(dict_data.keys())
    displayData = list(dict_data.values())
    if chartType == 'hbar':
        # Set figure specifications
        chart = figure(
            y_range = countries,
            width = 800,
            height = int(len(countries)/2*100),
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
        chart.add_tools(HoverTool(tooltips = [("Country", "@y"),("TotalDeaths", "@right")]))
        return chart
        

def dashboardGenerator(day1, countries1, dataType1, chartType1):
    jsonData = selectDay(day1)
    allDataType1 = selectDataType(jsonData, dataType1)
    dict_data1 = selectCountryData(countries1, allDataType1)
    # allDataType2 = selectDataType(dataType2)
    chart1 = selectChart(chartType1, dict_data1, day1, dataType1)
    #chart2 = selectChart('pie')
    
    # Show Results
    show(chart1)

countries1 = ['USA','Chile','Mexico','France']
# countries2 = ['India','Germany','Brazil','Japan','Italy']
dashboardGenerator('yesterday', countries1, 'NewDeaths', 'hbar')


