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


# x = [1,2,3,4,5]
# y = [4,6,2,4,3]

# output_file('index.html')

# # Add Plot
# p = figure(
#     title = 'Simple Example',
#     x_axis_label = 'X Axis',
#     y_axis_label = 'Y Axis'
# )

# # Render glyph
# p.line(x,y,line_width = 2)

# # Show results
# show(p)