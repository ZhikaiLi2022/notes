# Data analysis of targets in TESS
-------------------------------------------------------------------------李志凯 德州学院  
## <h2 id="0"> content </h2>
#### 1.[Observation data](#1)
* observation method
* type of data
* using the data 
#### 2. [Data analysis of eccentric eclipsing binaries in TESS](#2)
* Eclipsing binaries
* Eccentricity of eclipsing binaries
#### 3. [Other intersting things in TESS](#3)
* 'heartbeat' stars
* quadruple system with two close eclipsing binaries
---
### <h2 id="1"> 1.Observation data [^](#0) </h2>
---
![pixelfile](/picture/pixelfile.gif)
[Download data](https://archive.stsci.edu/tess/bulk_downloads/bulk_downloads_ffi-tp-lc-dv.html)
<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/eebsky.png" width = "100%" alt=""/>
    <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">
      Figure 1. TESS observation targets of 26 sectors in the whole sky area. The black dots represent the large eccentricity binary samples we found.
  	</div>
</center>

Code
```
/home/life/notes/testpy/search.py
```
### <h2 id="2"> 2.Data analysis of eccentric eclipsing binaries in TESS [^](#0)</h2>

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/notes/picture/eb.jpg" width = "100%" alt=""/>
    <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">
      Figure 2. When the smaller star partially blocks the larger star,a primary eclipse occurs,and a secondary eclips occurs when the smaller star is occulted.
  	</div>
</center>

&emsp;The eclipsing binary candidates are first selected by **visually checking** whether more than three eclipses are present in the LightCurve.
<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/notes/picture/TIC 261656371a.png" width = "90%" alt=""/>
    <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">
      Figure 3. LC analysis and eclipses determination for EEB TIC 261656371 as an example.(a)Light curve.(b)The highest peak of the periodogram is determined as the inital period.(c,d)The original LC is folded and smoothed to obtain the differential folded LC and folded LC.The two eclipses are denoted by red dashed lines.(e,f)Two eclipses(black dotes)are fitted by the Gaussian function(red solid curve) to determine phases(black dashed lines) of the primary and secondary minimum.
  	</div>
</center>

code 
```
/home/life/双星偏心率的求解/汇总2021_9_30/code六件套/allEBselct2021_09_20.py
```
---

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/notes/picture/4TIC_353939279.png" width = "49%" alt=""/>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/notes/picture/8TIC_356015357.png" width = "49%" alt=""/>
</center>

![pipeline](/home/life/notes/picture/pipeline.jpg)

### <h2 id="3"> 3.Other intersting things in TESS [^](#0) </h2>

![heart](/home/life/notes/picture/eccentric_ellipsoidal.gif)
![hearts](/home/life/notes/picture/heart1.png)
![ho1](/home/life/notes/picture/ho1.png)
---

TIC 278956474:Two close binaries in one young quadruple system,identified by TESS

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/notes/picture/qlc.png" width = "49%" alt=""/>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="/home/life/notes/picture/q.png" width = "49%" alt=""/>
</center>

![hearts](/home/life/notes/picture/c1.png)


