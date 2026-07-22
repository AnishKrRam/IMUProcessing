import numpy as np
import matplotlib.pyplot as plt

def printDataStats(Data, mean=1, var=0, std=1):
    if mean:
        with np.printoptions(precision=3):
            print(f"      Means: {np.mean(Data, axis=0)}")
    if var:
        with np.printoptions(formatter={"float":lambda x: f"{x:.4e}"}):
            print(f"   Variance: {np.var(Data, axis=0)}")
    if std:
        with np.printoptions(precision=4, floatmode="fixed"):
            print(f"StandardDev: {np.std(Data, axis=0)}")

Data1 = np.loadtxt("IMUData/MPU_Data_V1_dt50.csv", delimiter=",", dtype=float)
Data2 = np.loadtxt("IMUData/MPU_Data_V2_dt50.csv", delimiter=",", dtype=float)
Data3 = np.loadtxt("IMUData/MPU_Data_V3_dt100.csv", delimiter=",", dtype=float)
Data5 = np.loadtxt("IMUData/MPU_Data_V5_dt50.csv", delimiter=",", dtype=float)

printDataStats(Data1, std=0)
printDataStats(Data2, std=0)
printDataStats(Data3, std=0)
printDataStats(Data5, std=0)

printDataStats(Data1, mean=0)
printDataStats(Data2, mean=0)
printDataStats(Data3, mean=0)
printDataStats(Data5, mean=0)



fig, ax = plt.subplots(3, 6)
fig.suptitle('Distributitons of Measurements')

for i in range(6):
    ax[0, i].hist(Data1[:,i], bins=20)
    ax[1, i].hist(Data2[:,i], bins=20)
    ax[2, i].hist(Data5[:,i], bins=20)

plt.show()