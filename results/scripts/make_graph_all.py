#!/usr/bin/env python2

from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText
import sys
import json
import os
from os import path
import operator


def create_figure(res):
    # title = "Platform: {0}".format(res[0]['processor'] + ' - (Cortex A15)')
    title = "Platform: Jetson TK1"
    fig = plt.figure(1)
    fig.suptitle(title, fontsize=14)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)

    ax.set_autoscaley_on(True)
    ax.set_ylim(0.3, 1)

    ax.set_title("CNN Model: {0}".format(
        res[0]['cnn_model']['name']))

    ax.set_xlabel("Iteration (discrete)")
    ax.set_ylabel("Time (secs)")

    # anchored_text = AnchoredText('Average={0}'.format(res['average']), loc=2)
    # ax.add_artist(anchored_text)

    for idx, val in enumerate(res):
        if val['processor'] == 'gpu':
            label = 'gpu: cnmem = %i' % val['cnmem']
        else:
            label = 'cpu: #threads = %i' % int(val['threads'])
        ax.plot(range(len(val['timings'])), val['timings'],
                label=label)
        ax.plot(range(len(val['timings'])),
                [sum(val['timings']) / len(val['timings']) for i in val['timings']],
                linestyle='--', linewidth=2.0, color='r')

    legend = ax.legend(loc='upper left', shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    fig.savefig('benchmark_{0}.png'.format(res[0]['cnn_model']['name']))
    plt.close(fig)


if __name__ == "__main__":
    try:
        res_path = sys.argv[1]
    except Exception as e:
        print 'No input dir!'
        sys.exit(1)

    res = [json.load(open(path.join(path.abspath(res_path), f))) for f in os.listdir(res_path) if f.endswith('.json')]
    # Sort by number of threads
    res.sort(key=operator.itemgetter('threads'))

    print len(res)
    # fp = open(resfile)
    # res = json.load(fp)
    create_figure(res)
