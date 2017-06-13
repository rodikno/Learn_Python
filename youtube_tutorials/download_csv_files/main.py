from urllib import request

report_url = 'http://www.stats.govt.nz/~/media/Statistics/Browse%20for%20stats/AnnualEnterpriseSurvey/HOTP15/aes-2015-csv.csv'

def download_csv_file(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_file = r'report.csv'
    fx = open(dest_file, 'w')

    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_csv_file(report_url)