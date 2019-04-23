import numpy as np
import matplotlib.pyplot as plt
import os
os.system("echo $PYTHONPATH")
import sys
sys.path.append("/usr/local/lib")
from ROOT import gStyle, gROOT, TCanvas, TFile, TH2F, TTree, TLegend

plt.rcParams["figure.figsize"] = (15, 10) # (w, h)
plt.rcParams["font.size"] = 22
plt.rcParams['lines.markersize'] = 12

bg = 'white'
plt.rcParams["figure.facecolor"] = bg
plt.rcParams["axes.facecolor"] = bg
plt.rcParams["savefig.facecolor"] = bg
plt.rcParams["errorbar.capsize"] = 12

def check_overtraining(fname, tree, var, xmax, ymin, ymax):
    f = TFile(fname)
    c = TCanvas("c", "{}_{}".format(var, tree), 1200, 800)
    tr = f.Get("TMVA_450/{}Tree".format(tree))
    histo = TH2F("histo", "", 100, 0, xmax, 100, ymin, ymax)
    c.SetLogz()
    gStyle.SetStatX(.90);
    gStyle.SetStatY(.92);
    tr.Draw("BDTG-{}:{}>>histo".format(var, var), "", "COLZ")
    histo.GetXaxis().SetTitle("{}_{{true}}".format(var, var));
    histo.GetYaxis().SetTitle("{}_{{regression}} - {}_{{true}}".format(var, var));
    c.Print("../images/{}_{}.png".format(var, tree))

check_overtraining("sims_450disp/TMVA_450_trueDisp.root", "Train", "trueDisp", 2.2, -1.7, 1.9)
check_overtraining("sims_450disp/TMVA_450_trueDisp.root", "Test", "trueDisp", 2.2, -1.7, 1.9)

check_overtraining("sims_450disp/TMVA_450_DispError.root", "Train", "DispError", 2.2, -1.7, 0.6)
check_overtraining("sims_450disp/TMVA_450_DispError.root", "Test", "DispError", 2.2, -1.7, 0.6)

check_overtraining("sims_450disp/TMVA_450_MAError.root", "Train", "MAError", 90, -90, 25)
check_overtraining("sims_450disp/TMVA_450_MAError.root", "Test", "MAError", 90, -90, 25)
