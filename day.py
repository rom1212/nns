OI=0
HI=1
LI=2
CI=3

# day data can also be seen as a row in a dataset.

def get_open(row):
    return row[OI]


def get_close(row):
    return row[CI]


def get_high(row):
    return row[HI]


def get_low(row):
    return row[LI]


def set_open(row, value):
    row[OI] = value


def set_close(row, value):
    row[CI] = value


def set_high(row, value):
    row[HI] = value


def set_low(row, value):
    row[LI] = value


def norm_day(row, factor=None):
    # print 'open:', get_open(row)
    # print 'close:', get_close(row)
    # print 'high:', get_high(row)
    # print 'low:', get_low(row)

    o = get_open(row)
    c = get_close(row)
    h = get_high(row)
    l = get_low(row)

    if factor is None:
        factor = l

    o /= factor
    c /= factor
    h /= factor
    l /= factor

    norm = row.copy()
    set_open(norm, o)
    set_close(norm, c)
    set_high(norm, h)
    set_low(norm, l)

    # print 'row:', row
    # print 'norm:', norm
    return norm

# days data could also be seen as pattern, or a target/sample during matching
def norm_days(days, factor=None):
    if factor is None:
        factor = get_low(days[0,:])

    norm = days.copy()
    for i in range(len(norm)):
        new_row = norm_day(days[i,:], factor)
        norm[i] = new_row
    # print "days:", days
    # print "norm:", norm
    return norm

