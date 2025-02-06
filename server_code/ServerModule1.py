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

@anvil.server.callable
def load_text(txt_object):
    # Get the data as txtbytes.
    txt_bytes = txt_object.get_bytes() 
    print(type(txt_bytes))
    csv_string = str(txt_bytes)
    print(type(csv_string))
    app_tables.test.add_row(id=1, dict=csv_string)

@anvil.server.callable
def get_v():
  # This finds all rows where object_col is a
  # dict and contains a key 'the_answer' with
  # the value '42' - no matter what other keys
  # are in the dict.
  r = app_tables.test.search(dict={'year': 1985})
  print (r)
  print (type(r))

@anvil.server.callable
def get_dict():
  r = app_tables.test.get(id=1)
  print (r)
  print (type(r))

    