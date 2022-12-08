# Necessary imports
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from ScrapeWebsite import scrape_country
import json

def selectDay(day = 'today'):
    """The selectDay() function accepts a single string input. Valid
    inputs are 'today', 'yesterday', and 'yesterday2' (yesterday2
    refers to data from 2 days ago). The function will retrieve COVID
    data from a .json file corresponding to the selected day and
    store it as a list of dictionaries. This function will also
    initiate an output .html file named Dashboard.html"""
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
        f = open('yesterday2.json')
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

def selectChart(chartType, dict_data):
    countries = list(dict_data.keys())
    displayData = list(dict_data.values())
    if chartType == 'hbar':
        # Set figure specifications
        global chart
        chart = figure(
            y_range = countries,
            width = 800,
            height = 200,
            title = 'COVID Deaths by Country',
            x_axis_label = 'Deaths',
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
        

def dashboardGenerator(day1, countries1, dataType1, chartType1):
    jsonData = selectDay(day1)
    allDataType1 = selectDataType(jsonData, dataType1)
    dict_data1 = selectCountryData(countries1, allDataType1)
    # allDataType2 = selectDataType(dataType2)
    selectChart(chartType1, dict_data1)
    #chart2 = selectChart('pie')
    show(chart)
    # Show Results
    

# dashboardGenerator(day, chart1, chart2, dataType)
# Show Results

countries1 = ['USA','Chile','Mexico']
dashboardGenerator('today', countries1, 'TotalDeaths', 'hbar')
