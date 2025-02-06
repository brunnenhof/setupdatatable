import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import csv

@anvil.server.callable
def read_csv(csv_object):
    # Get the data as bytes.
    csv_bytes = csv_object.get_bytes()
    # Convert bytes to a string.
    csv_string = str(csv_bytes, "utf-8")
    # Create a list of lines split on \n
    line_list = csv_string.split('\n')
    for line in line_list:
        # Create a list of fields from line.
        print("line=", line)
        field_list = line.split(",")
        for field in field_list:
            print("field=", field)