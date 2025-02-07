from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

#  def file_loader_1_change(self, files, **event_args):
    # This method is called when a new file is loaded into this FileLoader
#    for f in files:
#        anvil.server.call('read_csv', f)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    anvil.server.call('import_csv_data',file)

  def upload_numpy_change(self, files, **event_args):
    for f in files:
        anvil.server.call('load_text', f)

  def get_v_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('get_v')

  def get_dict_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('get_dict')
