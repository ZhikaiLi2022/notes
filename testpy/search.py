# /home/life/双星偏心率的求解/汇总2021_9_30/code六件套/allEBselct2021_09_20.py
# /home/life/变星在硬盘位置.py
from astropy.io import fits
from lightkurve import TessLightCurveFile
import lightkurve as lk
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from scipy.optimize import curve_fit
import os
import scipy.stats
import scipy.special
import matplotlib
import matplotlib.mlab as mlab
from matplotlib import cm
import pandas as pd
import seaborn as sns
#----------------------------
#  在硬盘上匹配光变曲线数据  |
#----------------------------
def cross_ssd_data(ID): #ID的格式为["TIC 224292441"]
    path1 = [
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector1/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector2/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector3/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector4/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector5/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector6/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector7/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector8/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector9/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector10/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector11/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector12/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector13/',
    ]
    file_dir1 = [[i+j for j in os.listdir(i)] for i in path1]
    path2 = [
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector14/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector15/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector16/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector17/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector18/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector19/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector20/',
    '/media/life/Seagate Expansion Drive/TESS数据下载/Sector21/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector22/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector23/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector24/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector25/',
    '/media/life/Seagate Expansion Drive/TESS数据下载2/Sector26/',
    ]
    file_dir2 = [[i+j for j in os.listdir(i)] for i in path2]
    file_dir = file_dir1+file_dir2
    IDdir = []
    for i in range(len(ID)):
        IDdir.append([])
    for i in range(len(ID)):
            for k in range(len(file_dir)):
                for l in range(len(file_dir[k])):
                    a = ID[i][4:]
                    if a == file_dir[k][l][-len(a)-15:-15] and file_dir[k][l][-len(a)-16:-len(a)-15] == '0':
                        IDdir[i].append(file_dir[k][l])
                        continue
            print("IDdir--"+str(i))
    return IDdir
ID = ["TIC 224292441"]
IDdir = cross_ssd_data(ID)
print(IDdir)
TESSMAG =[]
TEFF = []
LOGG = []
err_ID1 = []
for i in range(len(IDdir)):
    hdu = fits.open(IDdir[i][0])
    TESSMAG.append(hdu[0].header[34])
    TEFF.append(hdu[0].header[35])
    LOGG.append(hdu[0].header[36])
print("TESSMAG:",TESSMAG)
print("TEFF:",TEFF)
print("LOGG")
for ii in range(len(IDdir)):
    dirall = []
    for j in IDdir[ii]:
        try:
            dirall.append(lk.TessLightCurveFile(j))
        except:
            err_ID1.append(j)
            print(j)
    if dirall == []:
        continue
    if len(dirall) > 5:
        dirall = dirall[:5]
    target = "random"
    lc0 = lk.LightCurveCollection(dirall)
    lc = lc0.stitch().remove_nans()
    pg = lc.to_periodogram(method="LS",normalization="psd")
    print("Ra:",lc.ra)
    print("Dec:",lc.dec)
    lc.scatter()
    pg.plot('log')
    plt.show()
