import billboard
import csv
import datetime

with open('examples\hot-100_year-end.csv', 'w', encoding='UTF8', newline='') as f:
    # csv header
    fieldnames = ['date', 'rank', 'title', 'artist']
    
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    
    d = datetime.datetime.now()
    for y in range(2006, d.year):
        # csv data
        chart = billboard.ChartData('hot-100-songs',year=str(y))
        for x in chart:
            if x.rank < 6:
                row={'date': chart.year, 'rank':x.rank, 'title': x.title, 'artist':x.artist}
                writer.writerow(row)
        print(y)