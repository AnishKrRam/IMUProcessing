import numpy as np
import matplotlib.pyplot as plt

ZERO_ERRORS = np.array([0.295, 0.546, 0.271, -0.541, -2.356, -2.227])
DT = 50e-3

def CalculateVelPos3D(Acc, Vel, Pos, DT):
    for i in range(len(Vel)):
        if i == 0:
            pass
        else:
            Vel[i,:] = Vel[i-1,:] + (Acc[i-1,:] * DT)

    for i in range(len(Pos)):
        if i == 0:
            pass
        else:
            Pos[i,:] = Pos[i-1,:] + (Vel[i-1,:] * DT)

Data = np.loadtxt("IMUData/MPU_Data_V4_dt50.csv",
                  delimiter=",", 
                  dtype=float,
                  usecols=range(3))

Acc = Data - ZERO_ERRORS[0:3] - np.array([0,0,9.81])
Vel = np.zeros_like(Acc)
Pos = np.zeros_like(Acc)

CalculateVelPos3D(Acc, Vel, Pos, DT)

AccPlot = plt.subplot2grid((3,1), (0,0))
VelPlot = plt.subplot2grid((3,1), (1,0))
PosPlot = plt.subplot2grid((3,1), (2,0))

[x, y, z] = AccPlot.plot(Acc)
AccPlot.legend([x,y,z], ["x","y","z"], loc=1)
VelPlot.plot(Vel)
PosPlot.plot(Pos)

plt.show()