import numpy as np
from day import norm_days, norm_day, get_high, get_low, get_open, get_close
from operator import itemgetter
import os

def remove_header_footer(infilename, outfilename):
    with open(infilename, 'r') as infile:
        lines = infile.readlines()
        outlines = lines[2:-1]
        with open(outfilename, 'w') as outfile:
            for line in outlines:
                outfile.write(line)


# 2011/10/19,5.27,5.39,5.24,5.28,7454650,40288124.00 
def read_tdx(filename):
    tempfilename = '/tmp/read-data.tmp'
    remove_header_footer(filename, tempfilename)

    csv = np.genfromtxt(tempfilename, delimiter=",")
    # print '=read_tdx: ', filename, ', csv.dtype:', csv.dtype, ', csv.shape:', csv.shape, ', type(csv): ', type(csv)
    # remove the first column as it is not a number.
    data = csv[:,1:]

    dates = []
    with open(tempfilename, 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            dates.append(line.split(',')[0])

    print(('===read_tdx: ', filename, ', data.dtype:', data.dtype, ', data.shape:', data.shape,
           ', type(data): ', type(data), ', len(dates): ', len(dates)))
    return data, dates


# csv can be produced by yfinance and to_csv, with format:
#     Date,Open,High,Low,Close,Adj Close,Volume
def read_csv(filename, skip_header=1):
    csv = np.genfromtxt(filename, skip_header=skip_header, delimiter=",")
    print('===read_csv: ', filename, ', type(csv): ', type(csv), ', csv.dtype:', csv.dtype, ', csv.shape:', csv.shape)
    # remove the first column as it is not a number.
    data = csv[:,1:]

    dates = []
    with open(filename, 'r') as infile:
        lines = infile.readlines()
        for line in lines[skip_header:]:
            dates.append(line.split(',')[0])

    print('===read_csv: ', filename,
            ', type(data): ', type(data), ', data.dtype:', data.dtype, ', data.shape:', data.shape,
            ', type(dates):', type(dates), ', type(dates[0]):', type(dates[0]), ', len(dates): ', len(dates))
    return data, dates


def match_one(target, cand, body_only=False):
    score = 0.0
    for i in range(len(target)):
        t = target[i,:]
        c = cand[i,:]
        score += abs(get_open(t) - get_open(c))
        score += abs(get_close(t) - get_close(c))
        if not body_only:
            score += abs(get_high(t) - get_high(c))
            score += abs(get_low(t) - get_low(c))
    return score


def match_all(target, data):
    """match target with all the data.

    target is normalized first.

    for each candidate in data, we also normalized it first.
    """
    print(len(target))
    print(len(data))
    normed_target = norm_days(target)

    scores = []
    for i in range(len(data) - len(target) + 1):
        cand = data[i:i+len(target),:]
        normed_cand = norm_days(cand)
        score = match_one(normed_target, normed_cand)
        scores.append(score)
        # print 'match score:', score
        if i % 10000 == 0:
            print('matched records:', i)

    return scores


def read_dir(dirname, numfiles, read_func):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in os.listdir(dirname) if isfile(os.path.join(dirname, f))]
    print('onlyfiles:', onlyfiles)
    print('numfiles:', numfiles)
    print('onlyfiles[0:numfiles]', onlyfiles[0:numfiles])
    
    if numfiles < 0:
        numfiles = len(onlyfiles)
    all_data = None
    all_dates = None
    for filename in onlyfiles[0:numfiles]:
        print('filename:', filename)
        data, dates = read_func(os.path.join(dirname,filename))
        print(type(data))
        # break
        if all_data is None:
            all_data = data
            all_dates = dates
        else:
            all_data = np.concatenate((all_data, data), axis=0)
            all_dates = np.concatenate((all_dates, dates), axis=0)
    print('all_data.shape:', all_data.shape)
    return all_data, all_dates
            
    

