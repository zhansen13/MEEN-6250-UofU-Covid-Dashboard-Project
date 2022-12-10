# Necessary imports
from math import pi
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
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
allCountries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina',
                'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
                'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
                'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'CAR',
                'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Caribbean Netherlands', 'Cayman Islands', 'Chad',
                'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica',
                'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czechia', 'DPRK', 'DRC', 'Denmark', 'Diamond Princess',
                'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
                'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe Islands', 'Falkland Islands', 'Fiji', 'Finland',
                'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
                'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guinea', 'Guinea-Bissau',
                'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
                'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
                'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
                'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam', 'Macao', 'Madagascar', 'Malawi', 'Malaysia',
                'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte',
                'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco',
                'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
                'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau',
                'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
                'Qatar', 'Romania', 'Russia', 'Rwanda', 'Réunion', 'S. Korea', 'Saint Helena', 'Saint Kitts and Nevis',
                'Saint Lucia', 'Saint Martin', 'Saint Pierre Miquelon', 'Samoa', 'San Marino', 'Sao Tome and Principe',
                'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia',
                'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Barth',
                'St. Vincent Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
                'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
                'Turks and Caicos', 'Tuvalu', 'UAE', 'UK', 'USA', 'Uganda', 'Ukraine', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                'Vatican City', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe'
                ]

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
title_yesterday = {'TotalDeaths':'Total COVID Deaths by Country as of Yesterday',
                'NewDeaths':'New COVID Deaths By Country as of Yesterday',
                'ActiveCases':'Active COVID Cases by Country as of Yesterday',
                'Serious,Critical':'Critical COVID Cases by Country as of Yesterday',
                'TotalCases':'Total COVID Cases by Country as of Yesterday',
                'NewCases': 'New COVID Cases by Country as of Yesterday',
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
title_two_days_ago = {'TotalDeaths':'Total COVID Deaths by Country as of Two Days Ago',
                'NewDeaths':'New COVID Deaths By Country as of Two Days Ago',
                'ActiveCases':'Active COVID Cases by Country as of Two Days Ago',
                'Serious,Critical':'Critical COVID Cases by Country as of Two Days Ago',
                'TotalCases':'Total COVID Cases by Country as of Two Days Ago',
                'NewCases': 'New COVID Cases by Country as of Two Days Ago',
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
labels = {'TotalDeaths':'Total Deaths', 'NewDeaths':'New Deaths',
                'ActiveCases':'Active Cases', 'Serious,Critical':'Critical Cases', 'TotalCases':'Total Cases',
                'NewCases': 'New Cases', 'New Deaths/1M pop':'New Deaths/1M', 'Deaths/1M pop':'Total Deaths/1M',
                'Population':'Population', 'TotalRecovered':'Total Recovered', 'NewRecovered':'New Recovered',
                'TotCases/1M pop':'Total Cases/1M', 'TotalTests':'Total Tests', 'Tests/1M pop':'Total Tests/1M',
                '1 Caseevery X ppl':'People per Case', '1 Deathevery X ppl':'People per Death',
                '1 Testevery X ppl':'People per Test', 'New Cases/1M pop':'New Cases/1M',
                'Active Cases/1M pop':'Active Cases/1M'
                }

allDataTypes = list(labels.keys())

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
        return f"""\n'{day}' is not a valid input for the first argument of the dashboardGenerator() function. Please
input exactly one of the following values: 'today', 'yesterday', or 'two_days_ago'. Use the
format dashboardGenerator(day, countries, dataType, chartType)."""
    return jsonData

def selectDataType(jsonData, dataType):
    """_Extract full list of countries and corresponding data type values from jsonData_

    Args:
        jsonData (_list_): _List of dictionaries including all COVID related data for every country_
        
        dataType (_str_): _Specifies the data type of interest for the figure in the COVID dashboard. Print
            the variable allDataTypes for a list of valid inputs.
    
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
            if jsonData[i][dataType] == "" or jsonData[i][dataType] == "N/A":
                pass
            else:
                # Collect json data for each country
                allCountries.append(jsonData[i]['Country,Other'])
                # Clean the string to save as type int
                allDisplayData.append(float(jsonData[i][dataType].replace('+','').replace(',','')))
        except KeyError:
            error = f"""\nInvalid input for the dataType argument of the dashboardGenerator() function.
No such dataType as '{dataType}'. Please input exactly one of the values from the following list:

    ['TotalDeaths', 'NewDeaths', 'ActiveCases', 'Serious,Critical', 'TotalCases', 'NewCases',
    'New Deaths/1M pop', 'Deaths/1M pop', 'Population', 'TotalRecovered', 'NewRecovered',
    'TotCases/1M pop', 'TotalTests', 'Tests/1M pop', '1 Caseevery X ppl', '1 Deathevery X ppl',
    '1 Testevery X ppl', 'New Cases/1M pop', 'Active Cases/1M pop']

Use the format dashboardGenerator(day, countries, dataType, chartType)."""
            return error
    # return a dictionary of countries and the values of the specific data type of interest
    return dict(zip(allCountries, allDisplayData))

def selectCountryData(allDataType, dataType, day, countries, chartType):
    """_Extracts data of the desired type corresponding only to countries of interest_

    Args:
        allDataType (_dict_): _dictionary where the keys are all of the countries and the values contain
            the specific data type of interest_
        
        dataType (_str_): _Specifies the data type of interest for the figure. Print the variable
            allDataTypes for a list of valid inputs.
        
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
        except KeyError:
            values.append('No Data Available')
            print(f"Unfortunately the '{labels[dataType]}' data for {countries[i]} is not available for {day.replace('_',' ')}.")
            errors.append(i)
    # Combine the countries of interest with the values of interest in a dictionary.
    if len(countries) < 1:
        return f"\nUnfortunately the requested {chartType} chart cannot be built due to insufficient '{dataType}' data."
    dict_data = dict(zip(countries, values))
    # Remove any countries that have error statements.
    for i in range(len(errors)):
        del dict_data[countries[errors[i]]]
    return dict_data

def generateTitle(day, dataType):
    """_Generate figure title based on day and data type_

    Args:
        day (_str_): _Specify the day of interest. Valid inputs include 'today', 'yesterday', and 'two_days_ago'_
        
        dataType (_str_): _Specifies the data type of interest for the figure. Print the list variable
            allDataTypes for a list of valid inputs.

    Returns:
        _str_: _Specific title for the figure based on day and data type_
    """
    # Set chart title based on day and dataType
    if day == 'today':
        if type(dataType) == list:
            title = f"{labels[dataType[1]]} as a Function of {labels[dataType[0]]} as of Today"
        else:
            title = title_today[dataType]
    elif day == 'yesterday':
        if type(dataType) == list:
            title = f"{labels[dataType[1]]} as a Function of {labels[dataType[0]]} as of Yesterday"
        else:
            title = title_yesterday[dataType]
    elif day == 'two_days_ago':
        if type(dataType) == list:
            title = f"{labels[dataType[1]]} as a Function of {labels[dataType[0]]} as of Two Days Ago"
        else:
            title = title_two_days_ago[dataType]
    return title

def hbarChart(title, dataType, countries, displayData):
    """_Generate a horizontal bar chart_

    Args:
        title (_str_): _the title for the figure_
        
        dataType (_str_): _the data type of interest. For a list of valid data types print the variable allDataTypes_
        
        countries (_list_): _list containing the countries of interest_
        
        displayData (_list_): _list containing values corresponding to the data type and countries of interest_

    Returns:
        _bokeh.plotting._figure.figure_: _a variable containing all information for the hbar chart_
    """
    # Set dynamic height for hbar figure
    if int(len(countries)/2*100) < 400:
        height = 400
    else:
        height = int(len(countries)*50)
    # Set figure specifications
    chart = figure(y_range = countries, width = 800, height = height, title = title,
        x_axis_label = labels[dataType], tools = "pan, wheel_zoom, box_zoom, save, reset")
    # Render Glyph
    chart.hbar(y = countries, right = displayData, left = 0, height = 0.2, color = 'blue',
        fill_alpha = 0.5)
    # Add Tooltips (HoverTool)
    chart.add_tools(HoverTool(tooltips = [("Country", "@y"),(dataType, "@right")]))
    return chart

def vbarChart(title, dataType, countries, displayData):
    """_Generate a vertical bar chart_

    Args:
        title (_str_): _the title for the figure_
        
        dataType (_str_): _the data type of interest. For a list of valid data types print the variable allDataTypes_
        
        countries (_list_): _list containing the countries of interest_
        
        displayData (_list_): _list containing values corresponding to the data type and countries of interest_

    Returns:
        _bokeh.plotting._figure.figure_: _a variable containing all information for the hbar chart_
    """
    # Set dynamic height for vbar figure
    if int(len(displayData)*80) < 600:
        width = 600
    else:
        width = int(len(displayData)*80)
    # Set figure specifications
    chart = figure(x_range = countries, width = width, height = 400, title = title, y_axis_label = labels[dataType])
    # Render Glyph
    chart.vbar(x = countries, width = 0.5, bottom = 0, top = displayData, color = "Cyan")
    # Add Tooltips (HoverTool)
    chart.add_tools(HoverTool(tooltips = [("Country", "@x"),(dataType, "@top")]))
    return chart

def pieChart(dict_data, title, dataType):
    """_Generate a pie chart_

    Args:
        dict_data (_dict_): _dictionary where keys represent countries and values represent the data corresponding 
            to the data type of interest for the corresponding country_
        
        title (_str_): _the title for the figure_
        dataType (_str_): _the data type of interest. For a list of valid data types print the variable allDataTypes_

    Returns:
        _bokeh.plotting._figure.figure_: _a variable containing all information for the pie chart_
    """
    # Generate pie figure
    # Return error for more than 20 countries
    if len(dict_data) > 20:
        return f"""\nMaximum countries for pie chart exceded. Length of input countries list is limited
to 20 for chartType pie. Consider an hbar plot to display more countries."""
    # Return error for fewer than 3 countries
    elif len(dict_data) < 3:
        print("\nMust have a minimum of 3 countries for a pie plot. Consider hbar plot instead.")
        return
    # Set dynamic height for figure
    if int(len(dict_data)*29) < 500:
        height = 500
    else:
        height = int(len(dict_data)*29)
    # Format data using pandas
    data = pd.Series(dict_data).reset_index(name='value').rename(columns={'index': 'country'})
    data['angle'] = data['value']/data['value'].sum()*2*pi
    data['color'] = Category20c[len(dict_data)]
    # Set figure specifications
    chart = figure(height=height, width = 600, title=title, tools= "pan, wheel_zoom, box_zoom, save, reset, hover",
        tooltips=[("Country","@country"),(dataType, "@value")], x_range=(-0.5, 1.0))
    # Render Glyph
    chart.wedge(x=0, y=1, radius=0.4, start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)
    chart.axis.axis_label = None; chart.axis.visible = False; chart.grid.grid_line_color = None
    return chart

def scatterChart(dataType, title, countries, displayData):
    """_Generate a scatter plot_

    Args:
        dataType (_list_): _a list containing two strings. Each string represents a data type of interest. For a
            list of valid data types print the variable allDataTypes_
        
        title (_str_): _the title for the figure_
        
        countries (_list_): _list containing countries of interest_
        
        displayData (_list_): _list containing two sublists that each contain values corresponding to the data
            type and countries of interest_
        
    Returns:
        _bokeh.plotting._figure.figure_: _a variable containing all information for the circle plot_
    """
    # Create a source variable to call all of the data for the plot from
    data = {'Countries': countries, 'dataType1': displayData[0], 'dataType2': displayData[1]}
    # Set figure specifications
    chart = figure(width=600, height=400, title = title, x_axis_label = labels[dataType[0]],
            y_axis_label = labels[dataType[1]], tools = "pan, wheel_zoom, box_zoom, save, reset")
    # Render Glyph
    chart.scatter(x = 'dataType1', y = 'dataType2', name = 'Countries', marker = "square", size = 7, fill_color = "red", source = data)
    # Add Tooltips (HoverTool)
    chart.add_tools(HoverTool(tooltips = [('Country', '@Countries'), (labels[dataType[0]], "@dataType1"), (labels[dataType[1]], "@dataType2")]))
    return chart

def circleChart(dataType, title, countries, displayData):
    """_Generate a circle plot_

    Args:
        dataType (_list_): _a list containing two strings. Each string represents a data type of interest. For a
            list of valid data types print the variable allDataTypes_
        
        title (_str_): _the title for the figure_
        
        countries (_list_): _list containing countries of interest_
        
        displayData (_list_): _list containing two sublists that each contain values corresponding to the data
            type and countries of interest_
        
    Returns:
        _bokeh.plotting._figure.figure_: _a variable containing all information for the circle plot_
    """
    # Create a source variable to call all of the data for the plot from
    data = {'Countries': countries, 'dataType1': displayData[0], 'dataType2': displayData[1]}
    # Set figure specifications
    chart = figure(width=600, height=400, title = title, x_axis_label = labels[dataType[0]],
        y_axis_label = labels[dataType[1]], tools = "pan, wheel_zoom, box_zoom, save, reset")
    # Render Glyph
    chart.circle(x = 'dataType1', y = 'dataType2', name = 'Countries', alpha=0.6, size=10, source = data)
    # Add Tooltips (HoverTool)
    chart.add_tools(HoverTool(tooltips = [('Country', '@Countries'), (labels[dataType[0]], "@dataType1"), (labels[dataType[1]], "@dataType2")]))
    return chart

def lineChart(dataType, title, countries, displayData):
    """_Generate a line plot_

    Args:
        dataType (_list_): _a list containing two strings. Each string represents a data type of interest. For a
            list of valid data types print the variable allDataTypes_
        
        title (_str_): _the title for the figure_
        
        countries (_list_): _list containing countries of interest_
        
        displayData (_list_): _list containing two sublists that each contain values corresponding to the data
            type and countries of interest_
        
    Returns:
        _bokeh.plotting._figure.figure_: _a variable containing all information for the circle plot_
    """
    # Create a source variable to call all of the data for the plot from
    data = {'Countries': countries, 'dataType1': displayData[0], 'dataType2': displayData[1]}
    # Set figure specifications
    chart = figure(width=600, height=400, title = title, x_axis_label = labels[dataType[0]],
        y_axis_label = labels[dataType[1]], tools = "pan, wheel_zoom, box_zoom, save, reset")
    # Render Glyph
    chart.line(x = 'dataType1', y = 'dataType2', name = 'Countries', source = data)
    # Add Tooltips (HoverTool)
    chart.add_tools(HoverTool(tooltips = [('Country', '@Countries'), (labels[dataType[0]], "@dataType1"), (labels[dataType[1]], "@dataType2")]))
    return chart

def generateChart(chartType, dict_data, day, dataType):
    """_generateChart() generates a plot from the dictionary key-value pairs provided as dict_data_

    Args:
        chartType (_str_): _specify the type of plot to display for the first figure in the COVID
            dashboard. Valid inputs include 'hbar', 'vbar', 'scatter 'pie', 'line' and 'circle'_
        
        dict_data (_dict_): _dictionary with countries of interest and values of the specified
            data type from arg4_
        
        day (_int_): _specify the day to extract the data from. Valid inputs include 'today',
            'yesterday', and 'two_days_ago'_
        
        dataType (_str_ or _list_): _Specifies the data type of interest for the first figure in
            the COVID dashboard. Print the list variable allDataTypes for a list of valid inputs.
            NOTE: If chartType == 'circle', 'line', or 'scatter' then dataType must be a list of 
            two strings where each string specifies a data type from the variable allDataTypes.
            The first element in the list will be placed on the x axis and the second element in
            the list will be placed on the y axis_
    Returns:
        _bokeh.plotting._figure.figure_: _returns a figure. Use show() to generate the figure._
    """
    # Call separateDict() to separate dict_data keys and values into seperate lists
    countries, displayData = separateDict(dict_data)
    # Call generateTitle to return a title for the figure
    title = generateTitle(day, dataType)
    # Call the respective chart generator function for the requested chart type
    if chartType == 'hbar':
        chart = hbarChart(title, dataType, countries, displayData)
    elif chartType == 'vbar':
        chart = vbarChart(title, dataType, countries, displayData)
    elif chartType == 'pie':
        chart = pieChart(dict_data, title, dataType)
        # Check to see if an error message was returned
        if type(chart) == str:
            return chart
    elif chartType == 'scatter':
        chart = scatterChart(dataType, title, countries, displayData)
    elif chartType == 'circle':
        chart = circleChart(dataType, title, countries, displayData)
    elif chartType == 'line':
        chart = lineChart(dataType, title, countries, displayData)
    return chart

def separateDict(dict_data):
    """_separateDict() accepts a dictionary or a list of dictionaries as an input and returns two
    lists. One list contains all of the keys from the dictionary and the other list contains all
    of the values from the dictionary if only one dictionary was input. If a list of dictionaries
    was input then the returned lists will contain sublists containing keys and values from all
    of the dictionaries in the input list._

    Args:
        dict_data (_dict or list_): _enter a dictionary or a list of dictionaries from which you
            would like to seperate the keys and values_

    Returns:
        _list_: _list of keys from the input dictionary or a list of sublists from the input list
            of dictionaries_
        
        _list_: _list of values from the input dictionary or a list of sublists from the input list
            of dictionaries_
    """
    displayData = list()
    # Check to see if the input argument was a dictionary or a list of dictionaries
    if type(dict_data) == list:
        # If the input argument was a list of dictionaries, iterate through each dictionary and
        # separate keys and values from each one.
        for i in range(len(dict_data)):
            countries = list(dict_data[0].keys())
            displayData.append(list(dict_data[i].values()))
    else:
        # If the input argument was a single dictionary, separate the keys and the values
        countries = list(dict_data.keys())
        displayData = list(dict_data.values())
    return countries, displayData

def dictEqualizer(dict1, dict2):
    """_dictEqualizer() takes two dictionaries as inputs and removes any keys from both dictionaries
    that are only present in one of the two dictionaries. The end result will be two dictionaries
    that both contain the same keys._

    Args:
        dict1 (_dict_): _enter two dictionaries which you want to contain the same keys_
        
        dict2 (_dict_): _enter two dictionaries which you want to contain the same keys_
    """
    # Create lists containing only the keys that are not present in both dictionaries
    list1 = list(dict1.keys() - dict2.keys())
    list2 = list(dict2.keys() - dict1.keys())
    # Remove any keys that only appear in one dictionary
    for i in range(len(list1)):
        dict1.pop(list1[i])
    for i in range(len(list2)):
        dict2.pop(list2[i])

def figureGenerator(day, countries, dataType, chartType):
    """_Will generate a figure for the COVID dashboard from the specified input arguments_

    Args:
        day (_str_): _specify the day to extract the data from. Valid inputs include 'today',
            'yesterday', and 'two_days_ago'_
        
        countries (_list_): _list containing countries of interest. Can also use the list
            variable allCountries. Print list variable allCountries for a list of valid countries_
        
        dataType (_str_ or _list_): _Specifies the data type of interest for the first figure in
            the COVID dashboard. Print the list variable allDataTypes for a list of valid inputs.
            NOTE: If chartType == 'circle', 'line', or 'scatter' then dataType must be a list of 
            two strings where each string specifies a data type from the variable allDataTypes.
            The first element in the list will be placed on the x axis and the second element in
            the list will be placed on the y axis_
        
        chartType (_str_): _specify the type of plot to display for the first figure in the COVID
            dashboard. Valid inputs include 'hbar', 'vbar', 'scatter 'pie', 'line' and 'circle'_
    """
    # Call each of the applicable functions in order to generate a figure for the COVID dashboard
    jsonData = selectDay(day)
    # Perform check to see if day was input correctly
    if type(jsonData) == str:
        # Return an error message if day was input incorrectly
        return jsonData
    else:
        # Check the type of dataType to see if we need to run the functions once or more than once depending on chart type.
        if type(dataType) == str:
            # Call the selectDataType() function to create a dictionary that contains all countries as keys
            # and the data of interest as values
            allDataType = selectDataType(jsonData, dataType)
            # Check to see if an error message was returned
            if type(allDataType) == str:
                # Return an error message if dataType was input incorrectly
                return allDataType
            # Call the selectCountryData to create a dictionary that contains only the countries of interest
            # as keys and the corresponding data of interest as values
            dict_data = selectCountryData(allDataType, dataType, day, countries, chartType)
            # Check to see if an error message was returned
            if type(dict_data) == str:
                print(dict_data)
                return
            # Call the generateChart() function to generate the desired charts
            chart = generateChart(chartType, dict_data, day, dataType)
        # If we need to run each function more than once for a circle chart, then we need to run through this else statement.
        else:
            allDataType = list()
            dict_data = list()
            # Run the selectDataType() function multiple times to create a list containing a dictionary for each of
            # the data types of interest. These dictionaries will contain data for all countries.
            for i in range(len(dataType)):
                allDataType.append(selectDataType(jsonData, dataType[i]))
                # Perform a check to see if dataType was input correctly
                if type(allDataType[i]) == str:
                    # Return an error message if dataType was input incorrectly
                    return allDataType[i]
                # Run the selectCountryData() function multiple times to create a list containing a dictionary for each of
                # the data types of interest. These dictionaries will contain all data only for the countries of interest.
                dict_data.append(selectCountryData(allDataType[i], dataType[i], day, countries, chartType))
                # Check to see if any error messages were returned
                if type(dict_data) == str:
                    return dict_data
            # Run the dictEqualizer() function to ensure that the dictionaries are all the same size.
            dictEqualizer(dict_data[0], dict_data[1])
            # Run the generateChart() function to build the desired chart
            chart = generateChart(chartType, dict_data, day, dataType)
    return chart

def dashboardGenerator(input_list):
    """_Will generate a dashboard from the specified input arguments regarding COVID data_

    Args:
        input_list (_list_): _input_list must be entered as a list where each element of the list
            is a sub list. Each sublist represents a figure to be displayed on the COVID Dashboard.
            Each sublist must contain exactly 4 elements in the following format:
            [day, countries, dataType, chartType]
            Each variable within the sublist must represent the following arguments in order:
        
                day (_str_): _specify the day to extract the data from for the first figure in the 
                    COVID dashboard. Valid inputs include 'today', 'yesterday', and 'two_days_ago'_
        
                countries (_list_): _list containing countries of interest for the first figure in the
                    COVID dashboard. Can also use the list type variable allCountries. Print list variable
                    allCountries for a list of valid countries_
        
                dataType (_str_ or _list_): _Specifies the data type of interest for the first figure in
                    the COVID dashboard. Print the list variable allDataTypes for a list of valid inputs.
                    NOTE: If chartType == 'circle', 'line', or 'scatter' then dataType must be a list of 
                    two strings where each string specifies a data type from the variable allDataTypes.
                    The first element in the list will be placed on the x axis and the second element in
                    the list will be placed on the y axis_
        
                chartType (_str_): _specify the type of plot to display for the first figure in the COVID
                    dashboard. Valid inputs include 'hbar', 'vbar', 'scatter 'pie', 'line' and 'circle'_
    """
    chart = list()
    # Generate a list of charts to display
    for i in range(len(input_list)):
        # Check to make sure that the dataType argument was entered as a list of two elements for figures that require that type of formatting.
        if input_list[i][3] == 'circle' and (type(input_list[i][2]) != list or  len(input_list[i][2]) != 2):
            # Print an error statement if the dataType formatting is incorrect.
            print(f"""\n'{input_list[i][2]}' is not a valid input argument while chartType == '{input_list[i][3]}'. If chartType == '{input_list[i][3]}'
then dataType must be a list of exactly two strings that each specify a data type. For a list
of valid data types print the variable allDataTypes.""")
            return
        if input_list[i][3] == 'line' and (type(input_list[i][2]) != list or  len(input_list[i][2]) != 2):
            # Print an error statement if the dataType formatting is incorrect.
            print(f"""\n'{input_list[i][2]}' is not a valid input argument while chartType == '{input_list[i][3]}'. If chartType == '{input_list[i][3]}'
then dataType must be a list of exactly two strings that each specify a data type. For a list
of valid data types print the variable allDataTypes.""")
            return
        if input_list[i][3] == 'scatter' and (type(input_list[i][2]) != list or  len(input_list[i][2]) != 2):
            # Print an error statement if the dataType formatting is incorrect.
            print(f"""\n'{input_list[i][2]}' is not a valid input argument while chartType == '{input_list[i][3]}'. If chartType == '{input_list[i][3]}'
then dataType must be a list of exactly two strings that each specify a data type. For a list
of valid data types print the variable allDataTypes.""")
            return
        # Add an element to the chart list for every sub_list within the input_list
        chart.append(figureGenerator(input_list[i][0], input_list[i][1], input_list[i][2], input_list[i][3]))
        # Check to see if any errors were returned.
        if type(chart[i]) == str:
            # Print error statements
            print(chart[i])
            return
    # Create a grid of charts with 2 columns and len(charts)/2 rows
    grid = gridplot(chart, ncols=2)
    # Show plots
    show(grid)



countries = ['USA','Chile','Mexico','France','Niue']
countries1 = ['India','Germany','Brazil','Japan','Italy']
countries2 = ['USA', 'China', 'UK', 'Spain', 'S. Korea', 'Hong Kong','South Africa', 'Italy', 'Japan', 'France', 'Mexico']
countries3 = ['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam',
                'Australia', 'Argentina', 'Netherlands', 'Taiwan', 'Iran', 'Mexico', 'Indonesia']

dashboardGenerator([['today', allCountries, ['TotalDeaths','NewDeaths'], 'scatter'],
                    ['yesterday', ['USA', 'S. Korea'], 'ActiveCases', 'vbar'],
                    ['two_days_ago', allCountries[:20], 'TotalDeaths', 'pie'],
                    ['two_days_ago', countries, ['TotalCases', 'NewCases'], 'circle'],
                    ['yesterday', countries1, 'New Deaths/1M pop', 'hbar'],
                    ['two_days_ago', allCountries[:3], ['Population','New Cases/1M pop'], 'line'],
                    ['two_days_ago', countries2, 'Deaths/1M pop', 'vbar'],
                    ['today', allCountries, ['Population', 'TotalRecovered'], 'scatter'],
                    ['yesterday', countries3, 'NewRecovered', 'pie'],
                    ['two_days_ago', allCountries, ['TotCases/1M pop','TotalTests'], 'circle'],
                    ['today', countries, 'Tests/1M pop', 'hbar'],
                    ['yesterday', countries2, '1 Caseevery X ppl', 'pie'],
                    ['two_days_ago', allCountries, ['1 Deathevery X ppl', '1 Testevery X ppl'], 'line'],
                    ['today', allCountries, ['New Cases/1M pop', 'Population'], 'scatter'],
                    ['yesterday', allCountries, 'Active Cases/1M pop', 'hbar']
                    ])

# print(allDataTypes)
# print(allCountries)
