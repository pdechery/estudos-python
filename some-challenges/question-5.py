import locale
import json

from datetime import datetime

'''
- Read in the document from a file
- Find and print:
    The Payee ID value
    Any invoices that contain the text “583”
- Change any date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
    Hint: The format of the date/time fields are integer timestamp. To create a datetime object from an integer timestamp, use the following: datetime_obj = datetime.datetime.fromtimestamp(integer_timestamp / 1e3)
- Write the json document back out to a new file
'''

if __name__ == '__main__':

  with open('./dataset.json', encoding="utf-8") as dataset:
    obj = json.load(dataset)
    for key, value in obj.items():
      if key == "payee":
        print(f'Payee id is: {value["id"]}')
      if key == "invoiceIds":
        for v in value:
          if "583" in v:
            print(f'This is an invoice containing "583": {v}')
      if "Time" in key:
        time = datetime.fromtimestamp(value / 1e3)
        obj[key] = time.strftime("%Y-%m-%dT%H:%M:%S")

    with open('./new-dataset.json', "w") as file:
      json.dump(obj, file, indent=2)

