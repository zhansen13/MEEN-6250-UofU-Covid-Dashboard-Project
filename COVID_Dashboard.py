# Necessary imports
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from ScrapeWebsite import scrape_country
import json



# Open the .json file
f = open('today.json')
data = json.load(f)

# Specify output .html file
output_file('Dashboard.html')

# Collect Data from .json file
countries = list()
totalDeaths = list()
newDeaths = list()
for i in range(len(data)-1):
    # If the data field is blank, skip that country
    if data[i]['TotalDeaths'] == '':
        pass
    else:
        countries.append(data[i]['Country,Other'])
        totalDeaths.append(int(data[i]['TotalDeaths'].replace(',','')))
        # newDeaths.append(data[i]['NewDeaths'].replace('+','').replace(',',''))

# Set figure specifications
totalDeathsPerCountry = figure(
    y_range = countries,
    width = 1500,
    height = 4000,
    title = 'COVID Deaths by Country',
    x_axis_label = 'Deaths',
    tools = "pan, box_select, zoom_in, zoom_out, save, reset"
)

# Render Glyph
totalDeathsPerCountry.hbar(
    y = countries,
    right = totalDeaths,
    left = 0,
    height = 0.2,
    color = 'blue',
    fill_alpha = 0.5
)

# Add Tooltips (HoverTool)
totalDeathsPerCountry.add_tools(HoverTool(tooltips = [("Country", "@y"),("Total Deaths", "@right")]))

# Show Results
show(totalDeathsPerCountry)
