#!/usr/bin/env python3

import subprocess
import time
import csv

COUNT=1800

with open('ntp_stat_2.csv','w',newline='') as csvfile:
        log_writer=csv.writer(csvfile)
        for i in range(COUNT):
                output = subprocess.check_output(['sntp','72.108.48.26'])
                offset = output.decode().split(' ')[-6]
                timestamp = output.decode().split(' ')[-8]
                print([offset,timestamp])
                log_writer.writerow([offset,timestamp])
                time.sleep(1)
