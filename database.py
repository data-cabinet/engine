import yaml
import json
import os

class Database:
  def __init__(self, name, description):
    self.tables = []
    self.relationships = []
    self.declarations = []
    self.name = name
    self.description = description

  def add_table(self, name):
    self.tables.append(f"{name}.json")
    self.declarations.append(f"{name}.yaml")
    with open(f"{name}.json", "w") as f:
      json.dump([], f)
    with open(f"{name}.yaml", "w") as f:
      yaml.dump({}, f)

  def delete_table(self, name):
    self.tables.remove(f"{name}.json")
    self.declarations.remove(f"{name}.yaml")
    os.remove(f"{name}.json")
    os.remove(f"{name}.yaml")

  def add_relationship(self, table1, table2):
    self.relationships.append(f"{table1}:{table2}")

  def delete_relationship(self, table1, table2):
    self.relationships.remove(f"{table1}:{table2}")
