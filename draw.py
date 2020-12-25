from day import get_high, get_low, get_open, get_close
import matplotlib.patches as patches

def draw_box(ax, x, y, width, height, color):
    # print 'x, y, width, height, color'
    #print x, y, width, height, color
    ax.add_patch(
        patches.Rectangle(
                (x-width/2, y),   # (x,y)
                width,          # width
                height,          # height
                facecolor=color,
        )
    )

def plot_row(ax, x, row, shift=1, factor=10):
    # print 'plot_row:', row[0:4]
    # center to 0, because it could rise and down
    o = get_open(row) - shift
    c = get_close(row) - shift
    h = get_high(row) - shift
    l = get_low(row) - shift

    o *= factor
    c *= factor
    h *= factor
    l *= factor
    # print 'o, c, h, l', o, c, h, l

    color = 'red' if c >= o else 'green'

    # body
    y = o if o <= c else c
    width = 0.8
    height = abs(c-o)
    draw_box(ax, x, y, width, height, color)

    # shadow
    y = l
    width = 0.10
    height = abs(h-l)
    draw_box(ax, x, y, width, height, color)


def plot_target(ax, x, target, shift=1, factor=10):
    print('========= plot target ============')
    for i in range(len(target)):
        row = target[i,:]
        plot_row(ax, x+i, row, shift, factor)
