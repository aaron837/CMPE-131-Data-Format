# Include standard modules
import sys
import pandas as pd

choice = sys.argv[2]

tsv = pd.read_csv(str(sys.argv[1]), delimiter='\t', encoding_errors='ignore')

if choice == '-c':
    print("Converting to CSV")
    tsv.to_csv('D_tab.csv', index=None)
elif choice == '-j':
    print("Converting to JSON")
    tsv.to_json('D_tab.json', orient='records', lines=True)
elif choice == '-x':
    print("Converting to XML")
    tsv.to_xml('D_tab.xml', parser='lxml')
else:
    print("Try again Bucko")
