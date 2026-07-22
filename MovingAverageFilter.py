import numpy as np
import matplotlib.pyplot as plt
from library import CalculateRot3D, CalculateVelPos3D
ZERO_ERRORS = np.array([0.295, 0.546, 0.271, -0.541, -2.356, -2.227])
ZERO_ERRORS_V5 = np.array([-0.434, 0.567, 0.285, -0.508, -2.269,-2.172])
DT = 50e-3

# Data_V4 acceleerometer calculated z position drifts due to non comtensated rotations about y axis
# Therefore, movement data needs to be corrected as per current angle of sensor
# Postioning system coordinates therefore depend on initial orientation, unless magnetometer is included
# Measuring position, without input fron motor encoder/GPS/other sensor measuring lower derivatives
# is a form of dead reckoning, even with filters


windowsize = 7

def MAFilter(Data, Data_MA, window=5):
    readings = np.zeros(shape=(window, Data.shape[1]))
    readings[0:window, :] = Data[0:window, :]
    Data_MA[0,:] = Data[0,:]

    for i in range(1, Data.shape[0]):

        if i < window:
            Data_MA[i, :] = np.mean(readings[0:i, :], axis=0)
        else:
            readings = np.roll(readings, -1, axis=0)
            readings[window-1, :] = Data[i, :]
            Data_MA[i, :] = np.average(readings, axis=0)

# Data1 = np.loadtxt("IMUData/MPU_Data_V1_dt50.csv", delimiter=",", dtype=float, usecols=range(6))
# Data2 = np.loadtxt("IMUData/MPU_Data_V2_dt50.csv", delimiter=",", dtype=float, usecols=range(6))
# Data3 = np.loadtxt("IMUData/MPU_Data_V3_dt100.csv", delimiter=",", dtype=float, usecols=range(6))
# Data4 = np.loadtxt("IMUData/MPU_Data_V4_dt50.csv", delimiter=",", dtype=float, usecols=range(6))
Data6 = np.loadtxt("IMUData/MPU_Data_V6_dt50.csv", delimiter=",", dtype=float, usecols=range(6))

Acc = Data6[:, 0:3] - ZERO_ERRORS_V5[0:3] - np.array([0,0,9.81])
AccMA = np.zeros_like(Acc)
Vel = np.zeros_like(Acc)
VelMA = np.zeros_like(Acc)
Pos = np.zeros_like(Acc)
PosMA = np.zeros_like(Acc)

MAFilter(Acc, AccMA, window=windowsize)
CalculateVelPos3D(Acc, Vel, Pos, DT)
CalculateVelPos3D(AccMA, VelMA, PosMA, DT)

Gyro = Data6[:, 3:6]
Gyro = Gyro - ZERO_ERRORS[3:6]
GyroMA = np.zeros_like(Gyro)
Rot = np.zeros_like(Gyro)
RotMA = np.zeros_like(Gyro)

MAFilter(Gyro, GyroMA, window=windowsize)
CalculateRot3D(Gyro, Rot, DT)
CalculateRot3D(GyroMA, RotMA, DT)

GyroPlot = plt.subplot2grid((5,2), (0,0))
RotPlot = plt.subplot2grid((5,2), (1,0))
GyroMAPlot = plt.subplot2grid((5,2), (0,1))
RotMAPlot = plt.subplot2grid((5,2), (1,1))

AccPlot = plt.subplot2grid((5,2), (2,0))
VelPlot = plt.subplot2grid((5,2), (3,0))
PosPlot = plt.subplot2grid((5,2), (4,0))
AccMAPlot = plt.subplot2grid((5,2), (2,1))
VelMAPlot = plt.subplot2grid((5,2), (3,1))
PosMAPlot = plt.subplot2grid((5,2), (4,1))

GyroPlot.plot(Gyro)
GyroPlot.set_title("Unfiltered")
RotPlot.plot(Rot)
GyroMAPlot.plot(GyroMA)
GyroMAPlot.set_title(f"Filtered \n window={windowsize}")
RotMAPlot.plot(RotMA)

[x, y, z] = AccPlot.plot(Acc)
AccPlot.legend([x,y,z], ["x","y","z"], loc=1)
VelPlot.plot(Vel)
PosPlot.plot(Pos)
AccMAPlot.plot(AccMA)
VelMAPlot.plot(VelMA)
PosMAPlot.plot(PosMA)

plt.suptitle("Data V6 Moving Average Filter")
plt.show()