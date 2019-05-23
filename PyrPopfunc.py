def PlotPyr(data_list, xlim, ylim):
    import matplotlib.pyplot as plt
    import numpy as np

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

    fig, axes = plt.subplots(ncols = 2, sharey = True)
    xmin, xmax, ymin, ymax = axis([0, xlim, 0, ylim])
    axes[0].barh(m_age, mens_list, align = 'center', color = 'yellow')
    axes[0].invert_xaxis()
    axes[0].set(title = 'Men')
    axes[1].barh(w_age, womens_list, align = 'center', color = 'gray')
    axes[1].set(title = 'Women')

    plt.show()
