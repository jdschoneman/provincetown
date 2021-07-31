# -*- coding: utf-8 -*-
"""
Generate plots for relationships between breakthrough infection fraction,
percentage of population vaccinated, and vaccine effectiveness. 
"""

import numpy as np
import matplotlib.pyplot as plt


colormap = plt.cm.viridis

#%% First figure - B vs. V for various E
E = [0.0, 0.5, 0.6, 0.7, 0.8, 0.9]  # Selections of vaccine effectiveness
V = np.linspace(0., 1.)       # Proportion of population vaccinated 

plt.figure(figsize = (12, 6))
for ve in E:
    R = V*(1 - ve)/(1 - V*ve) # Ratio infected who were vaccinated
    
    # Scale the effectiveness value to lie within [0, 1] for colormap 
    # purposes
    ve_cmap = (ve - min(E))/(max(E) - min(E))
    
    # Plot, adjusting axes labels to percentages and doing the same for the
    # vaccine effectiveness label
    plt.plot(V*100, R*100, color = colormap(ve_cmap), linewidth = 2.,
             label = 'Vax Effectivenss [E] = %.0f%%' % (ve*100))
    
# Add a line with observed 74% fraction
plt.hlines(74, 0., 100., linestyle = '--', linewidth = 1.5, 
           label = 'Provincetown Observation')

# Add line with average MA vaccination rate
yl = [-5, 105]
plt.vlines(69, *yl, linestyle = '-.',color = 'r', linewidth = 1.5, 
           label = 'MA Vaccination Rate')
plt.ylim(yl)
    
# Add annotations
plt.legend(fontsize = 14, framealpha = 1.)
plt.xlabel('Percentage of Population Vaccinated [V]', fontsize = 16,
           fontweight = 'bold')
plt.ylabel('Percentage of Breakthrough Infections [B]', fontsize = 16,
           fontweight = 'bold')
plt.xlim([0., 100.])

plt.title('Observed Percentage of Breakthrough Infections [B] vs. Percentage of Population\nVaccinated [V]' +
           ' for Several Vaccine Effectiveness Value [E]; B = (V - VE)/(1 - VE)',
           fontsize = 16, fontweight = 'bold')

# Save figure
plt.tight_layout()
plt.savefig('images/B_vs_V_forE.png', transparent = True, 
            bbox_inches = 'tight')

#%% Second figure - feasible effectivenss values vs. fraction vaccinated for the 
# observed fraction of 74%
# E = (B - V)/(B*V - V)

# Axis limits
yl = [-5, 105]
xl = [70, 100]



plt.figure(figsize = (12, 6))

# Line plot
V = np.linspace(0.01, 0.999999)
B = 0.74
E = (B - V)/(B*V - V)
plt.plot(V*100, E*100, 'k', linewidth = 2.)

# Marker plot; Set a few poulation percentage levels to pick off the E level
V_points = np.array([0.75, 0.8, 0.85, 0.9, 0.95])
E_points = (B - V_points)/(B*V_points - V_points)
for V_pt, E_pt in zip(V_points, E_points):

    plt.plot(V_pt*100, E_pt*100, 'o', color = colormap(E_pt), markersize = 10,
             markeredgecolor = 'k',
             label = '%.0f%% Vaccinated; Effectiveness = %.0f%%' % 
             (V_pt*100, E_pt*100))

plt.legend(framealpha = 1.0, fontsize = 14)
plt.ylabel('Implied Vaccine Effectiveness [E]', fontsize = 16,
           fontweight = 'bold')

plt.xlabel('Percentage of Population Vaccinated [V]', fontsize = 16,
           fontweight = 'bold')

plt.title('Implied Vaccine Effectiveness [E] vs. Percentage of Population Vaccinated [V]\n' +
          'for Observed %.0f%% Breakthrough Infection Rate [B]; E = (B - V)/(B*V - V)',
           fontsize = 16, fontweight = 'bold')

plt.ylim(yl)
plt.xlim(xl)
plt.grid()

