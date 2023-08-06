from astropy.table import Table, vstack
import glob

all_query_tables=glob.glob('query_result_*.fits')
all_query_tables.sort()
#table_list=[]
stack = None
for i, query_table in enumerate(all_query_tables):
    print(i, len(all_query_tables), query_table)
    table = Table.read(query_table, format='fits')
    if stack:
        stack = vstack([stack, table])
    else:
        stack = table
    stack.write('stacked_table.fits', format='fits', overwrite=True)

catalog = Table.read('stacked_table.fits')

for column in catalog.keys():
# Check if the column dtype starts with 'U' (Unicode string)
    if catalog[column_name].dtype.kind in ['U', 'S']:
        # Convert the column to 'float64'
        catalog[column] = catalog[column].astype('float64')

    catalog.write('stacked_table.fits',format='fits',overwrite=True)