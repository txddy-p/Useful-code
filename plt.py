import matplotlib.pyplot as plt
import numpy as np

with open('Res_100Hz_15k.txt') as f:
    lines = f.readlines()
    
print(lines[:10])

cur = np.array([])
times = np.array([])
voltages_resistor = np.array([])

iline = 0

for line in lines:
    if iline != 0:
        time = float(line.split('\t')[0])
        voltage_resistor = float(line.split('\t')[1])

        times = np.append(times, time)
        voltages_resistor = np.append(voltages_resistor, voltage_resistor)
    iline = iline +1

# for i in voltages_resistor:
#     cur=np.append(i/15000,voltage_resistor)

plt.plot(times, voltages_resistor, label='', color='b')

ax = plt.gca()
labely = ax.set_xlabel("time [s]", fontsize = 18)
labely = ax.set_ylabel("volatge [V]", fontsize = 18)


plt.show()
