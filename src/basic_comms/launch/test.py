import numpy as np 
import matplotlib.pyplot as plt 

A = 1
f = 2
phi = 0
sr = 100 

time = np.arange(0, 10, 1/sr)
y= A* np.sin(2*np.pi*f*time + phi)

# Plot the waveform 
plt.figure(figsize=(10,4))
plt.plot(time, y) 
plt.xlabel('Time (s)') 
plt.ylabel('Amplitude') 
plt.show() 