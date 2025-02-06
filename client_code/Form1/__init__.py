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

  def file_loader_1_change(self, files, **event_args):
    # This method is called when a new file is loaded into this FileLoader
    for f in files:
        anvil.server.call('read_csv', f)

  def upload_numpy_change(self, files, **event_args):
    for f in files:
        anvil.server.call('load_numpy', f)
