#!/usr/bin/python3
import numpy as np
from operator import itemgetter
from day import norm_days, norm_day, get_high, get_low, get_open, get_close
from data import read_csv, read_tdx, match_all, read_dir
from draw import draw_box, plot_row, plot_target
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

if __name__ == "__main__":
    data, dates = read_csv('./csv1')
    exit()

    data, dates = read_tdx('./testdata/testdata_1.txt')
    factor = 1

    # data, dates = read_tdx('./sample1.txt')
    # data, dates = read_tdx('./600030.txt')
    
    # factor = 100

    print(len(data))
    print(len(dates))
    total_days = len(data)

    ldays = 5
    target = data[total_days - ldays:,:]

    data, dates = read_dir('./stock/', -1, read_tdx)

    # cands = data[:total_days - ldays,:]
    cands = data
    print('matching ... ...')
    matches = match_all(target, cands)
    print(('min:', min(matches)))
    print('sorting ... ...')
    top = sorted(enumerate(matches), key=itemgetter(1))
    for i in range(3):
        index, score = top[i]
        print(('date:', dates[3:][index], ', score:', score))


    # plt.yticks(range(-10, 40, 5))
    num_subplots = 6
    fig1 = plt.figure(figsize=figaspect(5.))
    ax1 = fig1.add_subplot(num_subplots, 1, 1)
    print((type(ax1)))

    x = 1
    row = norm_day(target[0,:])
    print(("row:", row))

    # plot_row(ax1, x, row, factor=1)
    # norm_target = norm_days(target)
    # plot_target(ax1, x, norm_target, factor=1)

    norm_target = norm_days(target)
    plot_target(ax1, x, norm_target, factor=factor)

    for i in range(num_subplots - 1):
        index, score = top[-i-1]
        index, score = top[i]
        # cand = cands[index:index+len(target),:]
        # norm_cand = norm_days(cand)

        # x += len(target)
        # plot_target(ax1, x, norm_cand, factor=factor)

        print(('date:', dates[3:][index], ', score:', score))

        # ax = fig1.add_subplot(1, 2, 2)
        cand = cands[index:index+len(target) + 5,:]
        norm_cand = norm_days(cand)
        ax = fig1.add_subplot(num_subplots, 1, i+2)
        plot_target(ax, 1, norm_cand, factor=factor)
        ax.set_xlim([0, ldays + 5])
        ax.set_ylim([-10, 20])

    ax1.set_xlim([0, ldays + 5])
    ax1.set_ylim([-10, 20])
#    ax1.set_yticks(range(-10, 40, 5))

    fig1.savefig('match1.png', dpi=90, bbox_inches='tight')
    plt.subplots_adjust(hspace=0.5, right=0.5)
    plt.show()

