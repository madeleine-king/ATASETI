# ATASETI

This repo contains my work as a SETI REU Intern in 2021. 
ATASETI is a data processing pipeline to handle files, identify target signals, and cull interference from the Allen Telescope Array observational data. 

fullTurbo is a shell script that automates the process of searching for narrowband doppler drifting signals, filtering them and plotting candidates. It adapts tools from the turboSETI package from the Breakthrough Listen project for use on ATA data.

findeventATA uses the turboSETI utility find_event_pipeline to filter candidates due to RFI using simultaneous pointings. 

ploteventATA uses the turboSETI utilty plot_event_pipeline to plot candidates. 
