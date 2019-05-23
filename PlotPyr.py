import matplotlib.pyplot as plt
import numpy as np

data_list = [[0, 0, 0.1], [0, 1, 0.2], [5, 0, 0.3], [5, 1, 0.4], [10, 0, 0.6], [10, 1, 0.4]]

men_count = 0
women_count = 0
womens_list = []
mens_list = []
w_age = []
m_age = []

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

#y = range(0, 1)

fig, axes = plt.subplots(ncols = 2, sharey = True)
axes[0].barh(m_age, mens_list, align = 'center', color = 'yellow')
axes[0].invert_xaxis()
axes[0].set(title = 'Men')
axes[1].barh(w_age, womens_list, align = 'center', color = 'gray')
axes[1].set(title = 'Women')

plt.show()
