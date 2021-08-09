import os
from turbo_seti.find_event.plot_event_pipeline import plot_event_pipeline
from blimpy import *
import glob
import os

DATADIR = os.getcwd() + '/'

PATH_CSVF1 = glob.glob(DATADIR + '*.0*.csv')
PATH_CSVF2 = glob.glob(DATADIR + '*.1*.csv')
print("Grabbing hits from csv files:", PATH_CSV1, PATH_CSVF2)

#List of h5 files
filelist1 = glob.glob(DATADIR + '*.0*guppi*.h5')
filelist2 = glob.glob(DATADIR + '*.1*guppi*.h5')

# Write file locations to a .lst
with open(DATADIR + 'filelist1.lst', 'w') as f:
    for item in filelist1:
        f.write("%s\n" % item)

with open(DATADIR + 'filelist2.lst', 'w') as f:
    for item in filelist2:
        f.write("%s\n" % item)

#Run plot_event_pipeline

for i in PATH_CSVF1:
    plot_event_pipeline(i,
                        DATADIR + 'filelist1.lst',
                        user_validation=True)

for i in PATH_CSVF2:
    plot_event_pipeline(i,
                        DATADIR + 'filelist2.lst',
                        user_validation=True)
