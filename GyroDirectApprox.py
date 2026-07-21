import numpy as np
import matplotlib.pyplot as plt

DT = 50e-3

def CalculateRot3D(Gyro, Rot, DT):
    for i in range(len(Gyro)):
        if i == 0:
            pass
        else:
            Rot[i,:] = Rot[i-1,:] + (Gyro[i-1,:] * DT)


Data1 = np.loadtxt("IMUData/MPU_Data_V1_dt50.csv", delimiter=",", dtype=float, usecols=[3, 4, 5])
Data2 = np.loadtxt("IMUData/MPU_Data_V2_dt50.csv", delimiter=",", dtype=float, usecols=[3, 4, 5])
Data3 = np.loadtxt("IMUData/MPU_Data_V3_dt100.csv", delimiter=",", dtype=float, usecols=[3, 4, 5])

Gyro = Data2
Gyro = Gyro - np.array([np.mean(Gyro[:,0]), np.mean(Gyro[:,1]), np.mean(Gyro[:,2])])
Rot = np.zeros_like(Data1)

CalculateRot3D(Gyro, Rot, DT)

GyroPlot = plt.subplot2grid((2,1), (0,0))
RotPlot = plt.subplot2grid((2,1), (1,0))

GyroPlot.plot(Gyro)
RotPlot.plot(Rot)

plt.show()