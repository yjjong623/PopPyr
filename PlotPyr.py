import matplotlib.pyplot as plt
import numpy as np

data_list = [[0, 0, 0.1], [0, 1, 0.2], [5, 0, 0.3], [5, 1, 0.4], [10, 0, 0.6], [10, 1, 0.4]]

men_count = 0
women_count = 0
womens_list = []
mens_list = []
w_age = []
m_age = []
width = 5

length = len(data_list)
i = 0
while i < length:
    if data_list[i][1] == 1:
        womens_list.insert(women_count, data_list[i][2])
        w_age.insert(women_count, data_list[i][0])
        women_count = women_count + 1
        i = i + 1
    else:
        mens_list.insert(men_count, data_list[i][2])
        m_age.insert(men_count, data_list[i][0])
        men_count = men_count + 1
        i = i + 1


fig, axis= plt.subplots(ncols = 2, sharey = True, tight_layout=True)
fig.suptitle('Population Pyramid')
plt.setp(axis, yticks=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
yticklabels=['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74',
'75-79', '80-89', '90-94', '95-100', '100+'])
axis[0].xmin, axis[0].xmax, axis[0].ymin, axis[0].ymax = axis[0].axis([0, 1, 0, 100])
axis[1].xmin, axis[1].xmax, axis[1].ymin, axis[1].ymax = axis[1].axis([0, 1, 0, 100])
axis[0].barh(m_age, mens_list, width, align = 'edge', color = 'brown', edgecolor = 'black')
axis[0].invert_xaxis()
axis[0].set(title = 'Men')
axis[1].barh(w_age, womens_list, width, align = 'edge', color = 'gray', edgecolor = 'black')
axis[1].set(title = 'Women')
axis[0].set_ylabel('Age')
axis[0].set_xlabel('Percent of Population')
axis[1].set_xlabel('Percent of Population')

plt.show()
