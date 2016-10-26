#!/usr/bin/env python2

from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText
import sys
import json


def create_figure(res):
    title = "Platform: {0}, Num-Threads: {1}".format(res['processor'] + ' - Cortex-A15',
                                                     res['threads'])
    suffix = "nthreads_{0}".format(res['threads'])
    fig = plt.figure(1)
    fig.suptitle(title, fontsize=14)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_autoscaley_on(False)
    ax.set_ylim([min(res['timings']) / 1.01, max(res['timings']) * 1.01])
    ax.set_title("CNN Model: {0}".format(
        res['cnn_model']['name']))
    ax.set_xlabel("Iteration (discrete)")
    ax.set_ylabel("Time (secs)")
    # (0,0 is lower-left and 1,1 is upper-right)
    anchored_text = AnchoredText('Average={0}'.format(res['average']), loc=2)
    ax.add_artist(anchored_text)
    ax.plot(range(len(res['timings'])), res['timings'])
    ax.plot(range(len(res['timings'])),
            [sum(res['timings']) / len(res['timings']) for i in res['timings']],
            linestyle='--', linewidth=2.0, color='r')
    fig.savefig('benchmark_{0}_{1}.png'.format(res['cnn_model']['name'],
                                               suffix))
    plt.close(fig)


if __name__ == "__main__":
    try:
        resfile = sys.argv[1]
    except Exception as e:
        print 'No input file!'
        sys.exit(1)

    fp = open(resfile)
    res = json.load(fp)
    create_figure(res)
