from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import BasicTickFormatter
from bokeh.layouts import gridplot

with open('data1.txt', 'r') as file:
    data1 = file.readlines()

years = []
col2 = []
col4 = []
col5 = []
col7 = []
for line in data1:
    line_data = line.strip().split('\t')
    if len(line_data) >= 5:
        year = line_data[0].split('-')[0]
        years.append(year)
        col2.append(float(line_data[1].replace(',', ''))) if line_data[1] else col2.append(0)
        col4.append(float(line_data[3].replace(',', ''))) if line_data[3] else col4.append(0)
        col5.append(float(line_data[4].replace(',', ''))) if line_data[4] else col5.append(0)
        col7.append(float(line_data[6].replace(',', ''))) if line_data[6] else col7.append(0)


p = figure(title="Number of Computer Science Degrees Per Year", x_axis_label='Year', y_axis_label='Number of Degrees')

p.line(years, col2, legend_label="Total Bachelor Degrees", line_width=2, line_color="blue")
p.line(years, col4, legend_label="Men Bachelor Degrees", line_width=2, line_color="red")
p.line(years, col5, legend_label="Women Bachelor Degrees", line_width=2, line_color="green")
p.line(years, col7, legend_label="Total Master Degrees", line_width=2, line_color="purple")

p.yaxis.formatter = BasicTickFormatter(use_scientific=False)

years2 = []
jobs = []
pay = []

with open('data2.txt', 'r') as file:
    data2 = file.readlines()

for line in data2:
    line_data = line.strip().split('    ')
    if len(line_data) >= 3:
        year = line_data[0].split('-')[0]
        years2.append(year)
        jobs.append(float(line_data[1].replace(',', '')))
        pay_value = line_data[2].replace(',', '')
        pay.append(float(pay_value))



with open('data3.txt', 'r') as file:
    data3 = file.readlines()

years3 = []
jobs2 = []
pay2 = []

for line in data3:
    line_data = line.strip().split('    ')
    if len(line_data) >= 3:
        year = line_data[0].split('-')[0]
        years3.append(year)
        jobs2.append(float(line_data[1].replace(',', '')))
        pay2.append(float(line_data[2].replace(',', '')))

with open('data4.txt', 'r') as file:
    data4 = file.readlines()

years4 = []
pay3 = []

for line in data4:
    line_data = line.strip().split()
    if len(line_data) >= 2:
        year = line_data[0]
        years4.append(year)
        cost = float(line_data[1].replace(',', ''))
        pay3.append(cost)

t = figure(title="Number of Computer Jobs Per Year", x_axis_label='Year', y_axis_label='Number of Jobs')
u = figure(title="Annual Income of Computer Jobs Per Year", x_axis_label='Year', y_axis_label='Annual Income')
t.line(years3, jobs2, legend_label="Number of Software Development Jobs", line_width=2, line_color="red")
t.line(years2, jobs, legend_label="Number of Computer Science Jobs", line_width=2, line_color="blue")
u.line(years3, pay2, legend_label="Annual Pay of Software Development", line_width=2, line_color="red")
u.line(years2, pay, legend_label="Annual Pay of Computer Sceince", line_width=2, line_color="green")
u.line(years4, pay3, legend_label="Annual Pay of Other Jobs", line_width=2, line_color="blue")

t.yaxis.formatter = BasicTickFormatter(use_scientific=False)
u.yaxis.formatter = BasicTickFormatter(use_scientific=False)


output_file("plot.html")

grid = gridplot([[p, None], [t, u]])

show(grid)



#Sources:
#https://nces.ed.gov/programs/digest/d22/tables/dt22_325.35.asp
#https://codesubmit.io/blog/the-evolution-of-developer-salaries/
#https://www.ssa.gov/oact/cola/awidevelop.html