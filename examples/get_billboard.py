import billboard
import csv
from datetime import datetime, timedelta

with open('examples\charts.csv', 'w', encoding='UTF8', newline='') as f:
    # csv header
    fieldnames = ['date', 'rank', 'title', 'artist', 'peakPos', 'lastPos', 'weeks', 'isNew']
    
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    
    with open('examples\\billboardCharts.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for rw in datareader:
            # csv data
            chart = billboard.ChartData('hot-100',rw[0])
            for x in chart:
                row={'date': chart.date, 'rank':x.rank, 'title': x.title, 'artist':x.artist, 'peakPos':x.peakPos, 'lastPos':x.lastPos, 'weeks':x.weeks, 'isNew':x.isNew}
                writer.writerow(row)
            print(rw[0])
