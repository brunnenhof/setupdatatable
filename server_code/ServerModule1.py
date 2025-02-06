import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import csv
# Import JSON module
import json
# Define JSON string
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
js = '{"year": {"0": 1980.0, "1": 1980.03125, "2": 1980.0625, "3": 1980.09375, "4": 1980.125, "5": 1980.15625, "6": 1980.1875, "7": 1980.21875, "8": 1980.25, "9": 1980.28125, "10": 1980.3125, "11": 1980.34375, "12": 1980.375, "13": 1980.40625, "14": 1980.4375, "15": 1980.46875, "16": 1980.5, "17": 1980.53125, "18": 1980.5625, "19": 1980.59375, "20": 1980.625, "21": 1980.65625, "22": 1980.6875, "23": 1980.71875, "24": 1980.75, "25": 1980.78125, "26": 1980.8125, "27": 1980.84375, "28": 1980.875, "29": 1980.90625, "30": 1980.9375, "31": 1980.96875, "32": 1981.0}, "Cohort_0_to_20_H-us": {"0": 74.522724, "1": 74.509209325, "2": 74.49569464999999, "3": 74.482179975, "4": 74.4686653, "5": 74.455150625, "6": 74.44163595, "7": 74.428121275, "8": 74.4146066, "9": 74.401091925, "10": 74.38757724999999, "11": 74.374062575, "12": 74.3605479, "13": 74.347033225, "14": 74.33351855000001, "15": 74.320003875, "16": 74.3064892, "17": 74.292974525, "18": 74.27945985, "19": 74.265945175, "20": 74.2524305, "21": 74.238915825, "22": 74.22540115000001, "23": 74.211886475, "24": 74.1983718, "25": 74.18485712500001, "26": 74.17134245, "27": 74.157827775, "28": 74.1443131, "29": 74.13079842500001, "30": 74.11728375000001, "31": 74.103769075, "32": 74.0902544}, "Cohort_0_to_20_H-af": {"0": 200.988671, "1": 201.1943106125, "2": 201.399950225, "3": 201.60558983750002, "4": 201.81122945, "5": 202.0168690625, "6": 202.222508675, "7": 202.42814828750002, "8": 202.63378790000002, "9": 202.8394275125, "10": 203.045067125, "11": 203.2507067375, "12": 203.45634635000002, "13": 203.6619859625, "14": 203.867625575, "15": 204.0732651875, "16": 204.27890480000002, "17": 204.48454441250001, "18": 204.690184025, "19": 204.8958236375, "20": 205.10146325, "21": 205.30710286250002, "22": 205.512742475, "23": 205.7183820875, "24": 205.9240217, "25": 206.1296613125, "26": 206.335300925, "27": 206.5409405375, "28": 206.74658015, "29": 206.9522197625, "30": 207.15785937500002, "31": 207.3634989875, "32": 207.5691386}}'
sds = json.loads(js)
print(sds)
print(sds['year']['1'])

# Convert JSON String to Python
student_details = json.loads(jsonString)
# Print Dictionary
print(student_details)
# Print values using keys
print(student_details['name'])
print(student_details['course'])

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
  print ('in get_dict getting r')
  print (r)
  print (type(r))
  print ('in get_dict getting d as r[dict]')
  d = r['dict']
  print (d)
  sd = json.loads(d)
  print (type(sd))
  print (sd)
  print ('done')

  

    