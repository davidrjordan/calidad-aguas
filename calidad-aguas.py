import csv


with open('templates/calidad-aguas.template.csv', 'r') as template:
  template_reader = csv.DictReader(template)
  with open('data/calidad-aguas.csv', 'wb') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames = template_reader.fieldnames)
    writer.writeheader()
    writer.writerow({'Comunidad': 'Valencia', 'Provincia': 'Valencia'})
    csvfile.close()
  template.close()