# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:41:05 2021

@author: JRD_U
"""



#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st 
import os
import glob
import scipy
from scipy.stats import linregress


path = "G:\\My Drive\\JRD_Research\\PROJECTS\\018_SiNx_functionalization\\data\\p096_IVs"
save_path = "G:\\My Drive\\JRD_Research\\PROJECTS\\019_SOLVENT_SYSTEM\\fig_working\\SI1_IV_PLOTS"

sigma = []
labels = []
concentrations = []
conductivities = []
all_pHs = []
dates = []
file_tags = []

""" IV #1 """
Sol_conc1 = "1.0M KCl"
Sol_cond1 = 12.35
Sol_pH1 = 7.14
Date1 = "07-01-2021"
label1 = "pre-func"
tag1 = "_pre_func"
concentrations.append(Sol_conc1)
conductivities.append(Sol_cond1)
all_pHs.append(Sol_pH1)
dates.append(Date1)
sigma.append(Sol_cond1)
labels.append(label1)
file_tags.append(tag1)

""" IV #2 """
Sol_conc2 = "1.0M KCl"
Sol_cond2 = 12.01
Sol_pH2 = 7.74
Date2 = "07-02-2021"
label2 = "post-g vs. pH #1"
tag2 = "_07-02-2021_post_exp"
concentrations.append(Sol_conc2)
conductivities.append(Sol_cond2)
all_pHs.append(Sol_pH2)
dates.append(Date2)
sigma.append(Sol_cond2)
labels.append(label2)
file_tags.append(tag2)

""" IV #3 """
Sol_conc3 = "1.0M KCl"
Sol_cond3 = 12.26
Sol_pH3 = 6.72
Date3 = "07-06-2021"
label3 = "day 5"
tag3 = "p096_07-06-2021_day4"
concentrations.append(Sol_conc3)
conductivities.append(Sol_cond3)
all_pHs.append(Sol_pH3)
dates.append(Date3)
sigma.append(Sol_cond3)
labels.append(label3)
file_tags.append(tag3)

""" IV #4 """
Sol_conc4 = "1.0M KCl"
Sol_cond4 = 12.26
Sol_pH4 = 6.72
Date4 = "07-12-2021"
label4 = "day 11"
tag4 = "p096_day10"
concentrations.append(Sol_conc4)
conductivities.append(Sol_cond4)
all_pHs.append(Sol_pH4)
dates.append(Date4)
sigma.append(Sol_cond4)
labels.append(label4)
file_tags.append(tag4)

""" IV #5 """
Sol_conc5 = "0.1M KCl"
Sol_cond5 = 1.35
Sol_pH5 = 6.76
Date5 = "07-13-2021"
label5 = "pre-GvpH2_0.1M"
tag5 = "_p096_day11_"
concentrations.append(Sol_conc5)
conductivities.append(Sol_cond5)
all_pHs.append(Sol_pH5)
dates.append(Date5)
sigma.append(Sol_cond5)
labels.append(label5)
file_tags.append(tag5)

""" IV #6 """
Sol_conc6 = "1.0M KCl"
Sol_cond6 = 12.32
Sol_pH6 = 7.22
Date6 = "07-26-2021"
label6 = "day 25"
tag6 = "_p096_7262021_"
concentrations.append(Sol_conc6)
conductivities.append(Sol_cond6)
all_pHs.append(Sol_pH6)
dates.append(Date6)
sigma.append(Sol_cond6)
labels.append(label6)
file_tags.append(tag6)

# """ IV #7 """
# Sol_conc7 = "1.0M KCl"
# Sol_cond7 = 11.19
# Sol_pH7 = 6.98
# Date7 = "10-25-2022"
# label7 = "day 6"
# tag7 = "p192_10252022"
# concentrations.append(Sol_conc7)
# conductivities.append(Sol_cond7)
# all_pHs.append(Sol_pH7)
# dates.append(Date7)
# sigma.append(Sol_cond7)
# labels.append(label7)
# file_tags.append(tag7)

# """ IV #8 """
# Sol_conc8 = "1.0M KCl"
# Sol_cond8 = 11.21
# Sol_pH8 = 6.97
# Date8 = "10-26-2022"
# label8 = "day 7"
# tag8 = "p192_10262022"
# concentrations.append(Sol_conc8)
# conductivities.append(Sol_cond8)
# all_pHs.append(Sol_pH8)
# dates.append(Date8)
# sigma.append(Sol_cond8)
# labels.append(label8)
# file_tags.append(tag8)

# """ IV #9 """
# Sol_conc9 = "1.0M KCl"
# Sol_cond9 = 11.31
# Sol_pH9 = 7.04
# Date9 = "10-28-2022"
# label9 = "day 9\nPre-G v pH"
# tag9 = "p192_10282022_1"
# concentrations.append(Sol_conc9)
# conductivities.append(Sol_cond9)
# all_pHs.append(Sol_pH9)
# dates.append(Date9)
# sigma.append(Sol_cond9)
# labels.append(label9)
# file_tags.append(tag9)

# """ IV #10 """
# Sol_conc10 = "1.0M KCl"
# Sol_cond10 = 11.31
# Sol_pH10 = 7.04
# Date10 = "10-28-2022"
# label10 = "day 9\nPost-G v pH"
# tag10 = "p192_10282022_2"
# concentrations.append(Sol_conc10)
# conductivities.append(Sol_cond10)
# all_pHs.append(Sol_pH10)
# dates.append(Date10)
# sigma.append(Sol_cond10)
# labels.append(label10)
# file_tags.append(tag10)

# """ IV #11 """
# Sol_conc11 = "1.0M KCl"
# Sol_cond11 = 11.19
# Sol_pH11 = 7.01
# Date11 = "10-31-2022"
# label11 = "day 12"
# tag11 = "p192_10312022"
# concentrations.append(Sol_conc11)
# conductivities.append(Sol_cond11)
# all_pHs.append(Sol_pH11)
# dates.append(Date11)
# sigma.append(Sol_cond11)
# labels.append(label11)
# file_tags.append(tag11)

# """ IV #12 """
# Sol_conc12 = "1.0M KCl"
# Sol_cond12 = 11.32
# Sol_pH12 = 6.97
# Date12 = "11-01-2022"
# label12 = "day 13"
# tag12 = "p192_11012022"
# concentrations.append(Sol_conc12)
# conductivities.append(Sol_cond12)
# all_pHs.append(Sol_pH12)
# dates.append(Date12)
# sigma.append(Sol_cond12)
# labels.append(label12)
# file_tags.append(tag12)

# """ IV #13 """
# Sol_conc13 = "1.0M KCl"
# Sol_cond13 = 11.18
# Sol_pH13 = 7.04
# Date13 = "11-08-2022"
# label13 = "day 20"
# tag13 = "p192_11082022"
# concentrations.append(Sol_conc13)
# conductivities.append(Sol_cond13)
# all_pHs.append(Sol_pH13)
# dates.append(Date13)
# sigma.append(Sol_cond13)
# labels.append(label13)
# file_tags.append(tag13)

# """ IV #14 """
# Sol_conc14 = "1.0M KCl"
# Sol_cond14 = 11.14
# Sol_pH14 = 7.06
# Date14 = "11-09-2022"
# label14 = "day 21"
# tag14 = "p192_11092022"
# concentrations.append(Sol_conc14)
# conductivities.append(Sol_cond14)
# all_pHs.append(Sol_pH14)
# dates.append(Date14)
# sigma.append(Sol_cond14)
# labels.append(label14)
# file_tags.append(tag14)

# """ IV #15 """
# Sol_conc15 = "1.0M KCl"
# Sol_cond15 = 11.29
# Sol_pH15 = 7.08
# Date15 = "11-10-2022"
# label15 = "day 22"
# tag15 = "p192_11102022"
# concentrations.append(Sol_conc15)
# conductivities.append(Sol_cond15)
# all_pHs.append(Sol_pH15)
# dates.append(Date15)
# sigma.append(Sol_cond15)
# labels.append(label15)
# file_tags.append(tag15)

# """ IV #16 """
# Sol_conc16 = "1.0M KCl"
# Sol_cond16 = 11.35
# Sol_pH16 = 6.97
# Date16 = "11-11-2022"
# label16 = "day 23\npre-trans"
# tag16 = "p192_11112022_1"
# concentrations.append(Sol_conc16)
# conductivities.append(Sol_cond16)
# all_pHs.append(Sol_pH16)
# dates.append(Date16)
# sigma.append(Sol_cond16)
# labels.append(label16)
# file_tags.append(tag16)

# """ IV #17 """
# Sol_conc17 = "1.0M KCl"
# Sol_cond17 = 11.35
# Sol_pH17 = 6.97
# Date17 = "11-11-2022"
# label17 = "day 23\npost-trans"
# tag17 = "p192_11112022_2"
# concentrations.append(Sol_conc17)
# conductivities.append(Sol_cond17)
# all_pHs.append(Sol_pH17)
# dates.append(Date17)
# sigma.append(Sol_cond17)
# labels.append(label17)
# file_tags.append(tag17)

# """ IV #18 """
# Sol_conc18 = "1.0M KCl"
# Sol_cond18 = 11.26
# Sol_pH18 = 6.98
# Date18 = "11-15-2022"
# label18 = "day 27"
# tag18 = "p192_11152022"
# concentrations.append(Sol_conc18)
# conductivities.append(Sol_cond18)
# all_pHs.append(Sol_pH18)
# dates.append(Date18)
# sigma.append(Sol_cond18)
# labels.append(label18)
# file_tags.append(tag18)

""" Other User Defined Values """

mem_thickness = 15

save_file_name = "p096_02-02-2023_analysis"

plot_name = "p096"

plots_file_folder = [f"{save_file_name}_IV_plots_files_v01"]

IV_steps = 21
voltage_step = 20
max_pos = 200
min_negative = (-200)

# plot_colors = ["k", "b", "g", "r", "m", "y"]   

""" nanopore_sizing is based on the following reference:
Nature Protocols (2020), 15, 122-143.

Equation:
d = (G / 2 * sigma) * (1 + sqrt(1 + (16 * sigma * t / Pi * G)))

It was stated this sizing does not take surface charge or
EO into account. Because of this, it is most accurate at 
neutral pH and high salt concentrations.
"""
#aquisition_rate = 10000

all_avg_data = []
all_avg_current_data = []
all_avg_voltage_data = []

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        

try:
    os.mkdir(os.path.join(save_path, plots_file_folder[0]))
except OSError as error:
    print(error)

file_list = os.listdir(path)
file_names = []
for f in file_list:
    file_names.append(f)

all_data = []
for h in range(len(file_tags)):
#for h in range(0):
    abc = (glob.glob( f"{path}\\*{file_tags[h]}*.txt"))
    all_avg_current_data = []
    all_avg_voltage_data = []
    all_data.append(all_avg_current_data)
    for k in range(len(abc)):
        current_file = abc[k]               # check here to make sure you are not using a I/V curve that was ended early
        with open(f"{current_file}", "r") as f:
            lines = f.readlines()
            raw_voltage = [float(line.split()[0]) for line in lines]
            raw_current = [float(line.split()[1]) for line in lines]
            aquisition_rate = int(len(raw_current)/IV_steps)
            for i in range(21):
                current_window = (raw_current[aquisition_rate*i:((aquisition_rate*(i+1))-1)])
                averaged_current = int(st.mean(current_window))
                stdev = np.std(current_window)
                voltage_window = (raw_voltage[aquisition_rate*i:((aquisition_rate*(i+1))-1)])
                averaged_voltage = int(st.mean(voltage_window))
                all_avg_current_data.append(averaged_current)
                all_avg_voltage_data.append(averaged_voltage)

y = []          # make y-data for plots
for o in range(len(file_tags)):
    ydata = list(np.arange(min_negative,(max_pos + voltage_step), voltage_step))
    y.append(ydata)

x = []          # separate each I/V, avg current values at each voltage
xdata = []
G_all = []
G_pos = []
G_neg = []
G_avg = []
IV_stdev = []
G_stdev = []
G_stdev_list = []

for u in range(len(all_data)):
    list1 = all_data[u]
    x = list(chunks(list1, IV_steps))
    
    c = []
    c1 = []
    total = []
    G_calc = []
    G_calc2 = []
    G_stdev = []
    IV_stdev_calc = []
    
    
    for d in range(IV_steps):
        c.append([item[d] for item in x])
        c1 = int(sum(c[d])/len(c[d]))
        total.append(c1)
        IV_stdev_calc.append(np.std(c[d]))
    for t in range(IV_steps):
        G_calc.append(total[t]/ydata[t])
        G_calc2.append(total[t]/ydata[t])
    del G_calc2[10]
    del G_calc[10]
    G_stdev = np.std(G_calc2)
    G_stdev_list.append(G_stdev)
    G_all.append(G_calc)
    G_pos.append(G_calc[19])
    G_neg.append(G_calc[0])
    G_avg.append((G_calc[19]+G_calc[0])/2)
    IV_stdev.append(IV_stdev_calc)
    xdata.append(total)
    

diameters = []
t = mem_thickness

for i in range(len(G_avg)):
    g = round(G_avg[i],5)
    #g = g*1000 # make nanoamps?
    s = sigma[i]
    Pi = np.pi
    d = (g / (2 * s)) * (1 + np.sqrt(1 + (16 * s * t / (Pi * g))))
    d = round(d,1)
    diameters.append(d)
    
#d = (G / 2 * sigma) * (1 + sqrt(1 + (16 * sigma * t / Pi * G)))

#  Diameter calc #2
all_slopes = []

for u in range(len(all_data)):
    list1 = all_data[u]
    x = list(chunks(list1, IV_steps))
    slope = []
    for i in range(len(x)):
        
        fit_data = scipy.stats.linregress(ydata, x[i], alternative='two-sided') # x and y are labeled wrong oops
        # scipy.stats.linregress information = https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
        
        slope.append(fit_data[0])
        
    all_slopes.append(slope)

all_diameters_2 = []
all_avg_diameters_2 = []
all_stdev_diameters_2 = []
t = mem_thickness

for l in range(len(all_slopes)):
    traces = all_slopes[l]
    diameters_2 = []
    for i in range(len(traces)):
        g = round(traces[i],5)
        #g = g*1000 # make nanoamps?
        s = sigma[l]        # is this l right? 10-20-2022
        Pi = np.pi
        d = (g / (2 * s)) * (1 + np.sqrt(1 + (16 * s * t / (Pi * g))))
        d = round(d,5)
        diameters_2.append(d)
    all_diameters_2.append(diameters_2)
    avg_diameters_2 = round((sum(diameters_2)/len(diameters_2)),1)
    all_avg_diameters_2.append(avg_diameters_2)
    stdev_diameters_2 = round(np.std(diameters_2),2)
    all_stdev_diameters_2.append(stdev_diameters_2)


#########################EDIT TITLE BELOW ###############################

new_line = '\n'
plus_minus = '\u00B1'


pH_lable = [f"{dates[0]}{new_line}{labels[0]}{new_line}{all_avg_diameters_2[0]}{plus_minus}{all_stdev_diameters_2[0]} nm (dia){new_line}{Sol_conc1}{new_line}pH = {Sol_pH1}{new_line}", 
            f"{dates[1]}{new_line}{labels[1]}{new_line}{all_avg_diameters_2[1]}{plus_minus}{all_stdev_diameters_2[1]} nm (dia){new_line}{Sol_conc2}{new_line}pH = {Sol_pH2}{new_line}", 
            f"{dates[2]}{new_line}{labels[2]}{new_line}{all_avg_diameters_2[2]}{plus_minus}{all_stdev_diameters_2[2]} nm (dia){new_line}{Sol_conc3}{new_line}pH = {Sol_pH3}{new_line}",
            f"{dates[3]}{new_line}{labels[3]}{new_line}{all_avg_diameters_2[3]}{plus_minus}{all_stdev_diameters_2[3]} nm (dia){new_line}{Sol_conc4}{new_line}pH = {Sol_pH4}{new_line}",
            f"{dates[4]}{new_line}{labels[4]}{new_line}{all_avg_diameters_2[4]}{plus_minus}{all_stdev_diameters_2[4]} nm (dia){new_line}{Sol_conc5}{new_line}pH = {Sol_pH5}{new_line}",
            f"{dates[5]}{new_line}{labels[5]}{new_line}{all_avg_diameters_2[5]}{plus_minus}{all_stdev_diameters_2[5]} nm (dia){new_line}{Sol_conc6}{new_line}pH = {Sol_pH6}{new_line}"]#,
            # f"{new_line}{labels[6]}{new_line}{all_avg_diameters_2[6]}{plus_minus}{all_stdev_diameters_2[6]} nm (dia){new_line}{Sol_conc7}{new_line}pH = {Sol_pH7}{new_line}"]#,
            # f"{new_line}{labels[7]}{new_line}{all_avg_diameters_2[7]}{plus_minus}{all_stdev_diameters_2[7]} nm (dia){new_line}{Sol_conc8}{new_line}pH = {Sol_pH8}{new_line}",
            # f"{new_line}{labels[8]}{new_line}{all_avg_diameters_2[8]}{plus_minus}{all_stdev_diameters_2[8]} nm (dia){new_line}{Sol_conc9}{new_line}pH = {Sol_pH9}{new_line}", 
            # f"{new_line}{labels[9]}{new_line}{all_avg_diameters_2[9]}{plus_minus}{all_stdev_diameters_2[9]} nm (dia){new_line}{Sol_conc10}{new_line}pH = {Sol_pH10}{new_line}", 
            # f"{new_line}{labels[10]}{new_line}{all_avg_diameters_2[10]}{plus_minus}{all_stdev_diameters_2[10]} nm (dia){new_line}{Sol_conc11}{new_line}pH = {Sol_pH11}{new_line}",
            # f"{new_line}{labels[11]}{new_line}{all_avg_diameters_2[11]}{plus_minus}{all_stdev_diameters_2[11]} nm (dia){new_line}{Sol_conc12}{new_line}pH = {Sol_pH12}{new_line}",
            # f"{new_line}{labels[12]}{new_line}{all_avg_diameters_2[12]}{plus_minus}{all_stdev_diameters_2[12]} nm (dia){new_line}{Sol_conc13}{new_line}pH = {Sol_pH13}{new_line}",
            # f"{new_line}{labels[13]}{new_line}{all_avg_diameters_2[13]}{plus_minus}{all_stdev_diameters_2[13]} nm (dia){new_line}{Sol_conc14}{new_line}pH = {Sol_pH14}{new_line}",
            # f"{new_line}{labels[14]}{new_line}{all_avg_diameters_2[14]}{plus_minus}{all_stdev_diameters_2[14]} nm (dia){new_line}{Sol_conc15}{new_line}pH = {Sol_pH15}{new_line}",
            # f"{new_line}{labels[15]}{new_line}{all_avg_diameters_2[15]}{plus_minus}{all_stdev_diameters_2[15]} nm (dia){new_line}{Sol_conc16}{new_line}pH = {Sol_pH16}{new_line}",
            # f"{new_line}{labels[16]}{new_line}{all_avg_diameters_2[16]}{plus_minus}{all_stdev_diameters_2[16]} nm (dia){new_line}{Sol_conc17}{new_line}pH = {Sol_pH17}{new_line}",
            # f"{new_line}{labels[17]}{new_line}{all_avg_diameters_2[17]}{plus_minus}{all_stdev_diameters_2[17]} nm (dia){new_line}{Sol_conc18}{new_line}pH = {Sol_pH18}{new_line}"]#,
            
# pH_lable = [f"{Date1}", f"\n{Date2}", f"{Date3}", f"\n{Date4}",f"{Date5}", f"\n{Date6}", f"{Date7}", f"\n{Date8}", f"{Date9}", f"\n{Date10}", f"{Date11}", f"\n{Date12}", f"{Date13}", f"\n{Date14}", 
            # f"{Date15}", f"\n{Date16}", f"{Date17}", f"\n{Date18}"] 


plot_colors = ["k", "dimgray", "lightgray", "rosybrown", "indianred", "brown", "maroon", "red", "tomato", "coral", "orange", "sienna", "chocolate", "peru", "darkorange", "tan", "darkgoldenrod", "gold", "khaki", "darkkhaki", "olive", "yellow", "yellowgreen", "darkolivegreen", "chartreuse", "darkseagreen", "palegreen", "limegreen", "green", "lime", "springgreen", "aquamarine", "turquoise", "lightseagreen", "darkslategray", "darkcyan", "cyan", "deepskyblue", "lightskyblue", "dodgerblue", "cornflowerblue", "midnightblue", "blue", "slateblue", "darkslateblue", "rebeccapurple", "indigo", "darkorchid", "mediumorchid", "thistle", "plum", "violet", "purple", "fuchsia", "orchid", "mediumvioletred", "deeppink", "hotpink", "palevioletred", "crimson", "lightcoral", "indianred", "firebrick", "darkred", "tomato", "coral", "sienna", "bisque", "tan", "orange", "darkgoldenrod", "gold", "darkkhaki", "olive", "olivedrab", "darkolivegreen", "lawngreen", "forestgreen", "lime", "springgreen", "mediumspringgreen", "aquamarine" ]

#%%
fig = plt.figure(figsize=(8,5))
plt.errorbar(pH_lable, G_avg, yerr = G_stdev_list, ls = "None", ecolor = "k", elinewidth = 1, capsize = 4, capthick = 1, zorder = 0)
plt.scatter(pH_lable, G_avg, s = 10, zorder = 1, color = "k")
plt.title(f'{plot_name}', size=12, weight='bold')
# plt.xlabel('pH')
plt.ylabel('Conductance (pA/mV)')    
#plt.xlim(2.5, 7)
#plt.ylim(bottom = 0, top = max(G_pos + G_neg)+2)
#plt.yticks(np.arange(0, max(G_pos + G_neg)+3, 10))
plt.xticks(fontsize=6)
ax = plt.gca()
ax.tick_params(axis = 'x', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 8)
ax.tick_params(axis = 'y', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 12)
# ax.set_yticklabels([])
# ax.set_xticklabels([])
plt.tight_layout()
plt.savefig(os.path.join(save_path, plots_file_folder[0], f"{save_file_name}_avgG_wError.png"), dpi = 1260)




fig = plt.figure(figsize=(8,5))
plt.scatter(pH_lable, all_avg_diameters_2, s = 10, zorder = 1, color = "k")
plt.errorbar(pH_lable, all_avg_diameters_2, yerr = all_stdev_diameters_2, ls = "None", ecolor = "k", elinewidth = 1, capsize = 4, capthick = 1, zorder = 0)
plt.title(f'{plot_name}', size=12, weight='bold')
# plt.xlabel('pH')
plt.ylabel('diameter (nm)')    
#plt.xlim(2.5, 7)
#plt.ylim(bottom = 0, top = max(G_pos + G_neg)+2)
#plt.yticks(np.arange(0, max(G_pos + G_neg)+3, 10))
# plt.xticks(fontsize=6)
ax = plt.gca()
ax.tick_params(axis = 'x', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 8)
ax.tick_params(axis = 'y', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 12)
# ax.set_yticklabels([])
# ax.set_xticklabels([])
plt.tight_layout()
plt.savefig(os.path.join(save_path, plots_file_folder[0], f"{save_file_name}_diameters.png"), dpi = 1680)


#%%
# plotting diameters
import matplotlib.ticker as ticker
# pub ready
fonts = 11
border = 1.25
ticks = 1.25

# plot current only
PLOT_DPI = 600 
fig = plt.figure(figsize=(3,1.5))
plt.scatter(pH_lable, all_avg_diameters_2, s = 10, zorder = 1, color = "k")
plt.errorbar(pH_lable, all_avg_diameters_2, yerr = all_stdev_diameters_2, ls = "None", ecolor = "k", elinewidth = 1, capsize = 4, capthick = 1, zorder = 0)

ax = plt.gca()
# ax.set_xlabel('Time (s)', fontsize=fonts)
ax.set_ylabel('Diameter (nm)', fontsize=fonts)
plt.xticks(fontsize=fonts)
plt.yticks(fontsize=fonts)
# ax.set_title(f'initial_window_size = {initial_window_size}\nwindow_size_limit = {window_size_limit}\nwindow_stdev_limit = {window_stdev_limit}\nbaseline_focusing_val = {baseline_focusing_val}')
# plt.ylim(15,23)
# plt.xlim(250,1800)
[x.set_linewidth(border) for x in ax.spines.values()]
ax.set_yticks(np.arange(9, 21, 4))
ax.xaxis.set_tick_params(width=ticks)
ax.set_xticklabels([])
ax.yaxis.set_tick_params(width=ticks)
# ax.xaxis.set_major_locator(ticker.NullLocator())
# plt.xticks(x, labels=" ")
plt.savefig(os.path.join(save_path, plots_file_folder[0], "p096_IV_diameters_v02"), dpi = PLOT_DPI, bbox_inches = 'tight')
# plt.close()



#%%





# # plot
# i = 0
# fig = plt.figure(figsize=(20,20))
# for i in range(len(xdata)):
#     plt.scatter(y[i], xdata[i], s=12, alpha=0.75, color = plot_colors[i])

# plt.title(f'{plot_name}', size=12, weight='bold')
# plt.xlabel('Voltage (mV)')
# plt.ylabel('Current (pA)')    
# plt.legend(pH_lable, bbox_to_anchor=(1, 0.95), loc = 0, prop={'size': 6})
# plt.tight_layout()
# #plt.show()
# plt.savefig(os.path.join(path, plots_file_folder[0], f"{save_file_name}.png"), dpi = 1600)




# plot
i = 0
fig = plt.figure(figsize=(6,6))
for i in range(len(xdata)):
    plt.errorbar(y[i], xdata[i], yerr = IV_stdev[i], ls = "None", ecolor = plot_colors[i], elinewidth = 0.5, capsize = 3, capthick = 0.5 , zorder = 0)
    plt.scatter(y[i], xdata[i], s=10, alpha=0.75, zorder = 1, color = plot_colors[i])
    
ax = plt.gca()
ax.tick_params(axis = 'x', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 12)
ax.tick_params(axis = 'y', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 12)
# ax.set_yticklabels([])
# ax.set_xticklabels([])
plt.title(f'{plot_name}', size=12, weight='bold')
plt.xlabel('Voltage (mV)')
plt.ylabel('Current (pA)')     
plt.legend(pH_lable, bbox_to_anchor=(1, 0.95), loc = 0, prop={'size': 8})
plt.tight_layout()
#plt.show()
plt.savefig(os.path.join(save_path, plots_file_folder[0], f"{save_file_name}_wError_v01.png"), dpi = 1680)



# plot
i = 0
fig = plt.figure(figsize=(6,6))
for i in range(len(xdata)):
    plt.errorbar(y[i], xdata[i], yerr = IV_stdev[i], ls = "None", ecolor = plot_colors[i], elinewidth = 0.5, capsize = 3, capthick = 0.5 , zorder = 0)
    plt.scatter(y[i], xdata[i], s=10, alpha=0.75, zorder = 1, color = plot_colors[i])
    
ax = plt.gca()
ax.tick_params(axis = 'x', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 12)
ax.tick_params(axis = 'y', which = 'both', direction = 'inout', length = 7, width = 1.5, labelsize = 12)
# ax.set_yticklabels([])
# ax.set_xticklabels([])
plt.title(f'{plot_name}', size=12, weight='bold')
plt.xlabel('Voltage (mV)')
plt.ylabel('Current (pA)')     
# plt.legend(pH_lable, bbox_to_anchor=(1, 0.95), loc = 0)
plt.tight_layout()
#plt.show()
plt.savefig(os.path.join(save_path, plots_file_folder[0], f"{save_file_name}_wError_no_leg_v01.png"), dpi = 1280)




#%%   
















fig = plt.figure(figsize=(6,6))
ax = plt.gca()
ax.scatter(file_tags, G_neg, label = "G_neg")
ax.scatter( file_tags, G_pos, label = "G_pos")
ax.set_title(f'{save_file_name}', size=12, weight='bold')
ax.set_xlabel('pH')
ax.set_ylabel('Conductance (pA/mV)')  
ax.set_ylim(bottom = 0)
ax.legend()
fig.tight_layout()
plt.savefig(os.path.join(path, plots_file_folder[0], f"{save_file_name}_BothG2.png"), dpi = 1280)



#%%















##################################OLD




for i in range(len(file_names)):
#for i in range(6):
    
    data_list = []
    raw_current = []
    Curr = []
    Round_CUR_stdev = []
    CUR_stdev = []
    VOLT = []
    Round_VOLT_stdev = []
    VOLT_stdev = []
    
    current_file = file_names[i]
    with open(f"{path}"f"\\{current_file}", "r") as f:
        lines = f.readlines()
        raw_voltage = [float(line.split()[0]) for line in lines]
        raw_current = [float(line.split()[1]) for line in lines] 
        
    #lines = a.readlines()
    #for j in range(len(lines)):
        #data_point = re.split(r'\t+', lines[j])
        #raw_current.append(data_point[1])
        #raw_current = float(raw_current)
        raw_current = raw_current
        for k in range(21):
            #averaged_data = st.mean(raw_current[10000*k:10000*(k+1)])
            averaged_current = (st.mean(raw_current[aquisition_rate*k:((aquisition_rate*(k+1))-1)]))
            current_window = (raw_current[aquisition_rate*k:((aquisition_rate*(k+1))-1)])
            current_data = [int(current_window) for current_window in current_window]
            Curr_st_dev = st.stdev(current_data)
            Curr.append(averaged_current)
            #Round_CUR_stdev = [round(num, 0) for num in raw_current[aquisition_rate*k:aquisition_rate*(k+1)]]
            #CUR_stdev(st.stdev((Round_CUR_stdev)))
            voltage_window = (raw_voltage[aquisition_rate*k:((aquisition_rate*(k+1))-1)])
            voltage_data = [int(voltage_window) for voltage_window in voltage_window]
            averaged_voltage = (st.mean(raw_voltage[aquisition_rate*k:((aquisition_rate*(k+1))-1)]))
            VOLT_st_dev = st.stdev(current_data)
            VOLT.append(averaged_voltage)  
            #Round_VOLT_stdev = [round(num, 0) for num in raw_voltage[aquisition_rate*k:aquisition_rate*(k+1)]]
            #VOLT_stdev(st.stdev((Round_VOLT_stdev)))
            all_avg_data.append([averaged_current, averaged_voltage])
            all_avg_current_data.append(averaged_current)
            all_avg_voltage_data.append(averaged_voltage)
    #fig = plt.figure(figsize=(20,5))
    plt.scatter(VOLT, Curr, label = f'{current_file}')
    ax = plt.gca()
    #ax.set_title(f" {analysis_title} ", size=12, weight='bold') #Title
    ax.set_xlim(-225,225)
    ax.legend()
    
    
#all_data.append([current_data, voltage_data])

#%%

ax = plt.axes(projection='3d')
zdata = range(len(file_names))
xdata = all_avg_voltage_data
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');



#%%

all_avg_current_data = all_avg_current_data*100
#plt.scatter(VOLT, Curr, )
fig = plt.figure(figsize=(20,20))
plt.scatter(all_avg_voltage_data, all_avg_current_data)  
#plt.scatter(VOLT, Curr, label = f'{current_file}')
ax = plt.gca()
#ax.set_title(f" {analysis_title} ", size=12, weight='bold') #Title
ax.set_xlim(-225,225)
ax.legend()

#%%
# 3rd axis
numbers = []
numbers = [int(word) for word in current_file.split() if word.isdigit()]
                  
                     
                     
                     
#%%
                     
#path_names = 
sorted(file_names)

   
#%%
   
    
#
save_file_name = f"{current_file}_IV_v01"     
try:
    os.mkdir(os.path.join(path, save_file_name))    # makes a folder to save everything in (master folder)
except OSError as error:
    print(error)     
save_current = open(save_file_name, "w")
save_current.write(current_data)
save_current.write(voltage_data)
save_current.close()
    #current = lines
    #data_list.append(lines)
    




#%%
b = open("C:\\Users\\MrCpt\\Desktop\\04-20-2021\\BS_p069_0455.txt") 














#%%
path_list = []
path_list = ["G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-98_25_0832.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-98_26_0833.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-68_21_0843.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-68_21_0845.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-68_23_0846.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-68_23_0848.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-68_25_0849.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-87_1_0535.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-87_1_0544.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-87_2_0546.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH6-87_3_0548.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_0455.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_0456.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_0458.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH2-74_1_0714.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH2-74_2_0716.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH2-74_3_0718.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH2-74_4_0719.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-01_21_0729.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-01_22_0730.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-01_23_0732.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-34_1_0658.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-34_2_0700.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-34_3_0701.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-34_3_0703.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-49_21_0740.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-49_22_0741.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH3-49_23_0743.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-08_1_0644.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-08_2_0646.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-08_3_0648.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-17_21_0753.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-17_21_0754.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-17_23_0756.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-17_24_0757.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-17_25_0759.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-17_26_0802.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-35_1_0633.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-35_2_0634.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-35_3_0636.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-88_1_0621.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-88_2_0622.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-88_3_0623.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-91_21_0813.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-91_22_0815.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH4-91_23_0816.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-27_1_0607.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-27_2_0609.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-27_3_0611.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-90_1_0556.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-90_2_0557.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-90_3_0559.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-98_21_0826.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-98_22_0827.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-98_23_0829.txt",
"G:/My Drive/JRD_Research/PROJECTS/006_G_vs_pH/data/04-20-2021/BS_p069_pH5-98_24_0830.txt"]
#%%
all_data = []
list_size = len(path_list)

for i in range(list_size):
    current_path = path_list[i]
    current_data = open(f"{current_path}", "r")
    for j in range(len(current_data)):
        all_data.append(current_data.readline(j))
    
    
    
    
    
    
    
#%%
a = print(current_data.readline(5))
#%%

b = open(f"{current_path}", "r")

#%%

pH_data = pd.read_csv("run5_pH_data_9-3-2020.csv")
y_pH = pH_data[["pH"]].to_numpy()
y_pH = list(reversed(y_pH))















