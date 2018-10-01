import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import numpy as np
import scipy.stats

def nplot(dfstat, value):
    

    mu = dfstat[value]['mean'] 
    sigma = dfstat[value]['std']
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    ax = plt.subplot(111)
    ax.plot(x, scipy.stats.norm.pdf(x, mu, sigma))
    return ax

def twoplot(onestat, twostat, value, legends=['target', 'reference']):
    ax = plt.subplot(211)

    one_mu = onestat[value]["mean"]
    two_mu = twostat[value]["mean"]
    one_sigma = onestat[value]["std"]
    two_sigma = twostat[value]["std"]
    mu = (one_mu + two_mu)/2
    left_sigma = min(one_sigma, two_sigma)
    right_sigma = max(one_sigma, two_sigma)
    x =  np.linspace(mu - 4*left_sigma, mu + 4*right_sigma, 100)
    ax.plot(x, scipy.stats.norm.pdf(x, one_mu, one_sigma))
    #ax2 = plt.subplot(212, sharex=ax1)
    ax.plot(x, scipy.stats.norm.pdf(x, two_mu, two_sigma))
    ax.legend(legends)
    return ax

def histplot(numbers, bins=5, color='blue', axis = "", figsize=(30,8)):
    if axis == "":
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(121)
    else:
        ax = axis
    numBins = bins
    ax.hist(numbers,density=True,bins=numBins, color=color,alpha=0.8)
    return ax
