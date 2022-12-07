from bokeh.plotting import figure, output_file, show, ColumnDataSource
from ScrapeWebsite import scrape_country
import json

f = open('today.json')
data = json.load(f)

output_file('Dashboard.html')

countries = list()
totalDeaths = list()
newDeaths = list()
for i in range(len(data)-1):
    if data[i]['TotalDeaths'] == '':
        pass
    else:
        countries.append(data[i]['Country,Other'])
        totalDeaths.append(int(data[i]['TotalDeaths'].replace(',','')))
        # newDeaths.append(data[i]['NewDeaths'].replace('+','').replace(',',''))

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

# Show Results
show(totalDeathsPerCountry)

