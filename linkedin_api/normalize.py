import os
import csv
from collections import Counter
from operator import itemgetter
from prettytable import PrettyTable


CSV_FILE = os.path.join("/home/ragnarock/github/API_hunting","linkedin_api","my_connection.csv")
transforms = [(', Inc.', ''), (', Inc', ''), (', LLC', ''), (', LLP', ''),
(' LLC', ''), (' Inc.', ''), (' Inc', '')]

pt = PrettyTable(field_names=['Company', 'Freq'])
csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]
companies = [c['Company'].strip() for c in contacts if c['Company'].strip() != '']


for i, _ in enumerate(companies):
	for transform in transforms:
		companies[i] = companies[i].replace(*transform)
pt = PrettyTable(field_names=['Company', 'Freq'])
pt.align = 'l'
c = Counter(companies)
[pt.add_row([company, freq])
for (company, freq) in sorted(c.items(), key=itemgetter(1), reverse=True)
if freq > 1]
print pt






transforms = [
('Sr.', 'Senior'),
('Sr', 'Senior'),
('Jr.', 'Junior'),
('Jr', 'Junior'),
('CEO', 'Chief Executive Officer'),
('COO', 'Chief Operating Officer'),
('CTO', 'Chief Technology Officer'),
('CFO', 'Chief Finance Officer'),
('VP', 'Vice President'),
]

csvReader = csv.DictReader(open(CSV_FILE),delimiter=',',quotechar = '"')

contacts = [row for row in csvReader]


titles = []

for contacts in contacts:
	titles.extend([t.strip() for t in contact['Job Title'].split('/') 
		if contact['Job Title'].strip() != ''])
