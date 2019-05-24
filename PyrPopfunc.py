import numpy as np
import matplotlib.pyplot as plt

def PlotPyr(data_list, numSim, xlim, ylim, title):
    men_count = 0
    women_count = 0
    womens_list = []
    mens_list = []
    w_age = []
    m_age = []
    #width of the bars
    width = 5

    #sort into womens_list and mens_list to plot
    length = len(data_list)
    i = 0
    women_count = 0
    men_count = 0
    m_num_age = []
    w_num_age = []
    while i < length:
        if data_list[i][1] == 1:
            womens_list.insert(women_count, data_list[i][2] * 100)
            w_age.insert(women_count, data_list[i][0])
            women_count = women_count + 1
            i = i + 1
        else:
            mens_list.insert(men_count, data_list[i][2] * 100)
            m_age.insert(men_count, data_list[i][0])
            men_count = men_count + 1
            i = i + 1

    #plot
    fig, axis= plt.subplots(ncols = 2, sharey = True, tight_layout=True)
    st = fig.suptitle(title)
    plt.setp(axis, yticks=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
    yticklabels=['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74',
    '75-79', '80-89', '90-94', '95-100', '100+'])
    axis[0].xmin, axis[0].xmax, axis[0].ymin, axis[0].ymax = axis[0].axis([0, xlim, -0.5, ylim])
    axis[1].xmin, axis[1].xmax, axis[1].ymin, axis[1].ymax = axis[1].axis([0, xlim, -2.5, ylim])
    axis[0].barh(m_age, mens_list, width, align = 'center', color = 'brown', edgecolor = 'black')
    axis[0].invert_xaxis()
    axis[0].set(title = 'Men')
    axis[1].barh(w_age, womens_list, width, align = 'center', color = 'gray', edgecolor = 'black')
    axis[1].set(title = 'Women')
    axis[0].set_ylabel('Age')
    axis[0].set_xlabel('Percent of Population')
    axis[1].set_xlabel('Percent of Population')

    #accounting for numSim
    men_count = 0
    women_count = 0
    if len(numSim) > 1:
        num_length = len(numSim)
        j = 0
        k = 0
        while j < num_length:
            while k < len(numSim[j]):
                if numSim[j][k][1] == 1:
                    axis[0].plot(numSim[j][k][2] * 100, numSim[j][k][0], marker = 'o', markersize = 3, color = "blue")
                    k = k + 1
                else:
                    axis[1].plot(numSim[j][k][2] * 100, numSim[j][k][0], marker = 'o', markersize = 3, color = "blue")
                    k = k + 1
            k = 0
            j = j + 1
    else:
        pass

    fig.tight_layout()
    st.set_y(1.0)
    fig.subplots_adjust(top=0.6)
    return fig

#testing 
data_table = [[0, 0, 0.1], [0, 1, 0.2], [5, 0, 0.3], [5, 1, 0.4], [10, 0, 0.6], [10, 1, 0.4]]
num_table = [[[0, 0, 0.5], [0, 1, 0.3], [5, 0, 0.5], [5, 1, 0.6]],
[[0, 0, 0.2], [0, 1, 0.4], [5, 0, 0.9], [5, 1, 0.4]]]
pyrfig = PlotPyr(data_table, num_table, 100, 20, 'Population Pyramid')
plt.show(pyrfig)
