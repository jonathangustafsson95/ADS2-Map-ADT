import matplotlib
import matplotlib.pyplot as plt
import os
matplotlib.use('TkAgg')


def plot_results(results, title, filename=None):

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for data in results:
        for op in results[data]:
            n = []
            time = []
            for i in range(len(results[data][op])):
                n.append(results[data][op][i]['n'])
                time.append(results[data][op][i]['time'])

            if data == 'Randomly Ordered Keys':
                ax1.plot(n, time, label=op)
            else:
                ax2.plot(n, time, label=op)

    ax1.set_title('Randomly Ordered Keys')
    ax1.set_ylabel('time (s)')
    ax1.set_xlabel('input size (n)')
    ax1.legend()

    ax2.set_title('Sorted Keys')
    ax2.set_ylabel('time (s)')
    ax2.set_xlabel('input size (n)')
    ax2.legend()

    fig.suptitle(title+' Map')

    plt.show()

    if filename:
        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.mkdir(os.path.dirname(filename))
        fig.savefig(filename)
