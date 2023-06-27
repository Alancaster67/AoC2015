#%%
import re
import json
with open('input.json', 'r') as file:
  accounting_data = json.load(file)

def drilldown_dict(obj, ignore_red: bool = False):
  total = 0
  match obj:

    case int():
      total += obj

    case str():
      pass

    case list():
      for elm in obj:
        total +=drilldown_dict(elm, ignore_red)

    case dict():
      if ignore_red:
        if "red" not in obj.values():
          for value in obj.values():
            total += drilldown_dict(value, ignore_red)
      else:
        for value in obj.values():
            total += drilldown_dict(value, ignore_red)
  
  return total

part_1 = drilldown_dict(accounting_data, ignore_red=False)
part_2  = drilldown_dict(accounting_data, ignore_red=True)
# %%
