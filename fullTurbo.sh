#! /bin/bash

#Script to copy files from storage for one observation, run turboSETI, run find_event_pipeline and plot_event_pipeline

#Format for entering observation name: guppi_{Julian date}_Unknown_0001 EX: guppi_59377_28093_149227_Unknown_0001

read -p "Centre Frequency:" FREQ

if [ ! -d "$FREQ" ]
then
        mkdir $FREQ
fi

#Make a folder for the observation within frequency folder
cd /mnt/buf0/mking/$FREQ
read -p "Folder name:" FOLDER

if [ ! -d "$FOLDER" ]
then
        mkdir $FOLDER
fi

cd /mnt/datax-netStorage-40G/

#For each subarray copy the .fil file
for i in 1.0 1.1 2.0 2.1 3.0 3.1; do
        FILE="${FOLDER}-ics.rawspec.0000.fil"
        echo $FILE
        cp dmpauto-seti-node$i/$FOLDER/${FILE} /mnt/buf0/mking/$FREQ/$FOLDER/${i}${FILE} &
done
wait

echo "I finished copying all the files!"

#Copy the python scripts into the observation folder
cd /mnt/buf0/mking
cp findeventATA.py $FREQ/$FOLDER
cp ploteventATA.py $FREQ/$FOLDER

#Run turboSETI
cd /mnt/buf0/mking/$FREQ/$FOLDER

for i in *.fil
do
        echo "Running turboSETI on the .fil file......"
        turboSETI "$i"  -M 10 -g y -p 12 -n 1440 -o /mnt/buf0/mking/$FREQ/$FOLDER
        if [[ $? -ne 0 ]]; then
                echo "turboSETI threw error, quitting the run....."
                exit 1
        else
                echo "successful turbo run, deleting .fil"
                rm $i
        fi
done


echo "I ran turboSETI on all the .fil files"
echo "Eliminating non-zero candidates and filtering"

python findeventATA.py

echo "Plotting candidates"

python ploteventATA.py

#Back to main folder, track the run in both frequency-specific file and in today's runs file
cd /mnt/buf0/mking

echo $FOLDER >> trackRuns${FREQ}.csv

currentDate=$(date)

echo ${FREQ},${FOLDER},${currentDate}>>trackToday.csv
