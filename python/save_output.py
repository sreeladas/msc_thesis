import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append("/home/sreela/Installs/anaconda2/lib")
from ROOT import gROOT, TCanvas, TFile, TH1F, TTree, TChain
from matplotlib.lines import Line2D
from matplotlib import cm
    
plt.rcParams["figure.figsize"] = (15, 10) # (w, h)
plt.rcParams["font.size"] = 22
plt.rcParams['lines.markersize'] = 12

bg = 'white'
plt.rcParams["figure.facecolor"] = bg
plt.rcParams["axes.facecolor"] = bg
plt.rcParams["savefig.facecolor"] = bg
plt.rcParams["errorbar.capsize"] = 12

zenith = [20, 30, 35, 40, 45, 50, 55, 60, 65]
myfmt = ['ko', 'rv', 'bD', 'g^', 'ks', 'r<', 'bp', 'g>', 'k*', 'r+']
zenfmt = ['kd', 'kd', 'kd', 'kd', 'kd', 'kd', 'kd', 'kd', 'kd', 'kd']
noise = [200, 250, 300, 350, 450]

energy = np.linspace(2, 5, 10)
zen_range = range(len(zenith))

def fetch_68_containment(fname, tcut):
    maxbin = 90
    nbins = 90000
    f = TFile(fname)
    tr = f.Get("diagnosticTree")
    histo = TH1F("histo", "", nbins, 0, maxbin)
    tr.Draw("DevDeg>>histo", tcut, "COLZ")
    std = histo.GetStdDev()/np.sqrt(histo.GetEntries())
    iter=0;
    while((iter<nbins) and ((histo.Integral(0, iter))<(histo.GetEntries()*.68))):
        iter=iter+1
    contain = (iter*maxbin*1.0)/nbins
    return (contain, std)

def plot_val(whichdisp, zenith, noise, myfmt, zenall):
    for i in range(len(zenith)):
        if(zenall == 0):
            plt.figure()
        for k in range(len(noise)):
            fname_disp = "sims_{}disp/z{:02}_n{}MHz.root".format(whichdisp, zenith[i], noise[k])
            if(os.path.isfile(fname_disp)):
                contain_disp, std_disp = fetch_68_containment(fname_disp, "")
                plt.errorbar(zenith[i], contain_disp, yerr=std_disp, fmt=myfmt[i])
        plt.xlabel("Noise (MHz)")
        plt.ylabel("68% Containment (deg)")
        plt.grid()
        plt.errorbar(0, 0, yerr=0, fmt=myfmt[i], label='Zenith {}'.format(zenith[i]))
        plt.xlim(150, 500)
        plt.ylim(0, 1.5)
        if(zenall == 0):
            plt.legend(loc=1)
            plt.savefig("sims_{}disp/zen{:02}_val.png".format(whichdisp, zenith[i]))
    if(zenall == 1):
        ax = plt.gca()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig("sims_{}disp/zenall_val.png".format(whichdisp))
    plt.show()
    
def plot_ratio(whichdisp, zenith, noise, myfmt, zenall):
    for i in range(len(zenith)):
        if(zenall == 0):
            plt.figure()
        for k in range(len(noise)):
            fname_disp = "sims_{}disp/z{:02}_n{}MHz.root".format(whichdisp, zenith[i], noise[k])
            fname_reg = "sims_reg/z{:02}_n{}MHz.root".format(zenith[i], noise[k])
            if(os.path.isfile(fname_disp) and os.path.isfile(fname_reg)):
                contain_disp, std_disp = fetch_68_containment(fname_disp, "")
                contain_reg, std_reg = fetch_68_containment(fname_reg, "")        
                plt.errorbar(noise[k], contain_disp/contain_reg, yerr=(std_disp/contain_disp+std_reg/contain_reg), fmt=myfmt[i])
        plt.xlabel("Noise (MHz)")
        plt.ylabel(r"68% Containment ratio (disp/regular)")
        plt.grid()
        plt.errorbar(0, 0, yerr=0, fmt=myfmt[i], label='Zenith {}'.format(zenith[i]))
        plt.xlim(150, 500)
        plt.ylim(0, 1.7)
        if(zenall == 0 ):
            plt.legend(loc=1)
            plt.savefig("sims_{}disp/zen{:02}_ratio.png".format(whichdisp, zenith[i]))
    if(zenall == 1):
        ax = plt.gca()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        plt.axhline(y=1, color='b')
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig("sims_{}disp/zenall_ratio_thesis.png".format(whichdisp))
    plt.show()
    
# plot_val("450size", zenith, noise, zenfmt, 0)
# plot_ratio("450size", zenith, noise, zenfmt, 0)
plot_val("450size", zenith, noise, myfmt, 1)
# plot_ratio("450size", zenith, noise, myfmt, 1)
