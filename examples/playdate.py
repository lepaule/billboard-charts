import billboard
import csv
from datetime import datetime, timedelta

with open('examples\charts.csv', 'w', encoding='UTF8', newline='') as f:
    # csv header
    fieldnames = ['date', 'title', 'artist', 'peakPos', 'lastPos', 'weeks', 'rank', 'isNew']
    
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    
    with open('examples\\billboardCharts.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for rw in datareader:
            print(rw[0])
            # csv data
            chart = billboard.ChartData('hot-100',rw[0])
            for x in chart:
                print(x.title, x.artist)
            print(chart.entries.count)
            
