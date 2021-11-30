# fastmtt
Taus decay via the weak interaction, necessitating the production of a neurino system. Leptonic tau decays occur 35% of the time, producing a single light lepton (an electron or muon) and a system of two neutrinos. Hadronic tau decays occur 65% of the time, producing a hadronic shower and a single neutrino. The neutrino systems in tau decays are invisible to detectors like CMS; accordingly, when a Higgs boson decays to two taus, the mass spectrum of the measured (*visible*) tau decay products typically undershoots the mass of the original ditau system. The fastmtt algorithm was developed to correct the mass spectrum of a visible ditau decay system to account for missing energy due to neutrino production. 
## Algorithm
This code implements the algorithm presented in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2019_032_v3.pdf. A dedicated C++ implementation of this algorithm is available here: https://github.com/SVfit/ClassicSVfit/tree/fastMTT_19_02_2019. 
## Usage
The repo is currently organized as follows:
 - ```test_fastmtt.py*``` contains a Numba-accelerated Pythonic implementation of fastmtt; to test this implementation, run the following command:
    ```python test_fastmtt.py <input sample> <n_evts>```
 - ```fastmtt_classic/``` contains the original C++ implementation of fastmtt; to build a shared library importable in Python, run ```python build_fastmtt_classic.py``` from this directory
 - ```samples/``` contains a set of test samples skimmed and formatted for easy input to fastmtt 
 - ```notebooks/``` contains a set of notebooks focused on validating the performance of this fastmtt implementation against the classic C++ version 
