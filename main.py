import csv
import json


csv_filepath = "data.csv"

def get_from_csv(csv_filepath):
    
    data_list: List[Dict[str, str]] = []

    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_list.append(row)

def get_user_data():
  print ("Please enter the following information")
  guest_name = input("Guest Name: ")
  street = input("Street: ")
  number = input("Number: ")
  department = input("Department: ")
  location = input("Location: ")
  in_date = input("Check-in Date: ")
  out_date = input("Check-out Date: ")

  info = {
    "guest_name" : guest_name,
    "street" : street,
    "number" : number,
    "department" : department,
    "location" : location,
    "in_date" : in_date,
    "out_date" : out_date
  }

  return info

def mount_letter(info : dict) -> str:
  letter :str = "Hello {}, you have been registered in our hotel. Your address is {}, {}, {}, {}. You will be staying with us from {} to {}.".format(info['guest_name'], info['street'], info['number'], info['department'], info['location'], info['in_date'], info['out_date'])
  return letter

def main():

  print(mount_letter(get_user_data()))

  #test_get_user_data()



if __name__ == "__main__":
  main()