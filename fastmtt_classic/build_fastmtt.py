import os
import ROOT

for basename in ['MeasuredTauLepton', 'svFitAuxFunctions', 'FastMTT']:
    if os.path.isfile("{0:s}_cc.so".format(basename)):
        ROOT.gInterpreter.ProcessLine(".L {0:s}_cc.so"
                                      .format(basename))
    else:
        ROOT.gInterpreter.ProcessLine(".L {0:s}.cc++"
                                      .format(basename))

