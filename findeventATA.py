from blimpy import *
from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
import glob
import os

DATADIR = os.getcwd() + '/'

# Retrieve the dat files

dat1 = glob.glob('1.0*.dat')[0]
dat11 = glob.glob('1.1*.dat')[0]
dat2 = glob.glob('2.0*.dat')[0]
dat21 = glob.glob('2.1*.dat')[0]
dat3 = glob.glob('3.0*.dat')[0]
dat31 = glob.glob('3.1*.dat')[0]

# Each subarray taking a turn as ON with the other two OFF
# subarray1 first ON, then 2, then 3

dat_lists1 = [[DATADIR + dat2, DATADIR + dat1, DATADIR + dat3], 
             [DATADIR + dat1, DATADIR + dat2, DATADIR + dat3],
             [DATADIR + dat1, DATADIR + dat3, DATADIR + dat2]]

dat_lists2 = [[DATADIR + dat21, DATADIR + dat11, DATADIR + dat31], 
             [DATADIR + dat11, DATADIR + dat21, DATADIR + dat31],
             [DATADIR + dat11, DATADIR + dat31, DATADIR + dat21]]

#start with 1st subarray as ON 
subarray = 1.0
for dat_list in dat_lists1:
    # This writes the dat files into a .lst, as required by the find_event_pipeline
    listName = DATADIR + 'dat_files{}.lst'.format(subarray)
    with open(listName, 'w') as f:
        for item in dat_list:
            f.write("%s\n" % item)
            
    PATH_CSVF = dir + 'ONOFF_{}_.csv'.format(subarray)
    print(listName)
    find_event_pipeline(listName, 
                    check_zero_drift=False,
                    SNR_cut = 25,
                    filter_threshold = 3,
                    number_in_cadence = len(dat_list),
                    on_off_first = 'OFF',
                    sortby_tstart=False,
                    user_validation=False,
                    saving=True,
                    csv_name=PATH_CSVF)
    ##Each time through loop, next subarray will be ON
    subarray = subarray + 1.0
    
    
subarrayList = [1.1, 2.1, 3.1,0]
subarray = subarrayList[0]
counter = 0
for dat_list in dat_lists2:
    # This writes the dat files into a .lst, as required by the find_event_pipeline
    listName = DATADIR + 'dat_files{}.lst'.format(subarray)
    with open(listName, 'w') as f:
        for item in dat_list:
            f.write("%s\n" % item)
            
    PATH_CSVF = dir + 'ONOFF_{}_.csv'.format(subarray)
    
    print(listName)
    find_event_pipeline(listName, 
                    check_zero_drift=False,
                    SNR_cut = 25,
                    filter_threshold = 3,
                    number_in_cadence = len(dat_list),
                    on_off_first = 'OFF',
                    sortby_tstart=False,
                    user_validation=False,
                    saving=True,
                    csv_name=PATH_CSVF)
    ##Each time through loop, next subarray will be ON
    counter = counter + 1
    subarray = subarrayList[counter]
