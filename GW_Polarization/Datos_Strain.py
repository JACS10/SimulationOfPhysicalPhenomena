import pylab as pl
import readligo as rl

strainH1, timeH1, chan_dict_H1 = rl.loaddata('H-H1_GWOSC_4KHZ_R1-1187529241-32.hdf5', 'H1')
strainL1, timeL1, chan_dict_L1 = rl.loaddata('L-L1_GWOSC_4KHZ_R1-1187529241-32.hdf5', 'L1')

pl.figure()
pl.plot(timeH1, strainH1)
pl.title('GW170823 H1')
pl.ylabel('Strain')
pl.xlabel('Time(s)')
pl.show()

pl.figure()
pl.plot(timeL1, strainL1)
pl.title('GW170823 L1')
pl.ylabel('Strain')
pl.xlabel('Time(s)')
pl.show()
