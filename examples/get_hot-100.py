import billboard
import csv
from datetime import date, timedelta

with open('examples\\hot-100.csv', 'w', encoding='UTF8', newline='') as f:
    # csv header
    fieldnames = ['date', 'rank', 'title', 'artist',
                  'peakPos', 'lastPos', 'weeks', 'isNew']

    writer = csv.DictWriter(f, fieldnames=fieldnames,
                            delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()

    def daterange(start_date, end_date):
     for n in range(0, int((end_date - start_date).days) + 1, 7):
         yield start_date + timedelta(n)

    #1958-08-04 is the fist Monday publication
    #1961-12-25 is the final Monday publication
    #1962-01-06 is the fist Saturday publication
    #date_list = list(daterange(date(1958, 8, 4), date(1961, 12, 25))) + list(daterange(date(1962, 1, 6), date.today()))
    #1976-07-03 was published one day late on 1976-07-04
    #uncomment next to check that the correct chart is returned
    #date_list = list(daterange(date(1976, 6, 26), date(1976, 7, 17)))
    date_list = list(daterange(date(2009, 8, 29), date.today()))
    for dt in date_list:
        # csv data
        chart = billboard.ChartData('hot-100', dt.strftime("%Y-%m-%d"))
        for x in chart:
            row = {'date': chart.date, 'rank': x.rank, 'title': x.title, 'artist': x.artist,
                    'peakPos': x.peakPos, 'lastPos': x.lastPos, 'weeks': x.weeks, 'isNew': x.isNew}
            writer.writerow(row)
        print(dt.strftime("%Y-%m-%d") + " " + chart.date)
