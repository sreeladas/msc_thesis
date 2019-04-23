import numpy as np
import matplotlib.pyplot as plt
import ROOT
plt.rcParams["figure.figsize"] = (20, 12) # (w, h)
plt.rcParams["font.size"] = 22

color = 'black'
plt.rcParams['text.color'] = color
plt.rcParams['axes.labelcolor'] = color
plt.rcParams['xtick.color'] = color
plt.rcParams['ytick.color'] = color
plt.rcParams['lines.markersize'] = 20

bg = 'white'
plt.rcParams["figure.facecolor"] = bg
plt.rcParams["axes.facecolor"] = bg
plt.rcParams["savefig.facecolor"] = bg

zenith = [20, 30, 35, 40, 45, 50, 55, 60, 65]
markerstyle = ['o', 'v', 'D', '^', 's', '<', 'p', '>', '*']
energy = np.power(10, np.linspace(2, 5, 10))
c=TCanvas()
c.Draw()
i=4
# for i in range(9):

f = ROOT.TFile("zen20/zendisp.root")
tr = f.Get("diagnosticTree")
tr.SetBranchAddress("fEnergyGev")
histo=TH1F("histo", "", 100, 0, 10)
tree.Draw("DevDeg>>histo", "fEnergyGeV>100&&fEnergyGeV<126", "COLZ")
