import numpy as np

def CalculateVelPos3D(Acc, Vel, Pos, DT=50e-3):
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

def CalculateRot3D(Gyro, Rot, DT=50e-3):
    for i in range(len(Gyro)):
        if i == 0:
            pass
        else:
            Rot[i,:] = Rot[i-1,:] + (Gyro[i-1,:] * DT)

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

