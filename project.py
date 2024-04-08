from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import BasicTickFormatter

with open('data.txt', 'r') as file:
    data = file.readlines()

years = []
col2 = []
col4 = []
col5 = []
col7 = []
for line in data:
    line_data = line.strip().split('\t')
    if len(line_data) >= 5:
        year = line_data[0].split('-')[0]
        years.append(year)
        col2.append(float(line_data[1].replace(',', ''))) if line_data[1] else col2.append(0)
        col4.append(float(line_data[3].replace(',', ''))) if line_data[3] else col4.append(0)
        col5.append(float(line_data[4].replace(',', ''))) if line_data[4] else col5.append(0)
        col7.append(float(line_data[6].replace(',', ''))) if line_data[6] else col7.append(0)

output_file("plot.html")

p = figure(title="Number of Computer Science Degrees Per Year", x_axis_label='Year', y_axis_label='Number of Degrees')

p.line(years, col2, legend_label="Total Bachelor Degrees", line_width=2, line_color="blue")
p.line(years, col4, legend_label="Men Bachelor Degrees", line_width=2, line_color="red")
p.line(years, col5, legend_label="Women Bachelor Degrees", line_width=2, line_color="green")
p.line(years, col7, legend_label="Total Master Degrees", line_width=2, line_color="purple")

p.yaxis.formatter = BasicTickFormatter(use_scientific=False)

show(p)