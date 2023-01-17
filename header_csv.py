# Import DictWriter class from CSV module
from csv import DictWriter

def csv_create_and_fill(anime_name, rating):
    # list of column names
    field_names = ['anime_name', 'rating']
    
    # Dictionary that we want to add as a new row
    dict = {'anime_name': anime_name, 'rating': rating}
    
    # Open CSV file in append mode
    # Create a file object for this file
    with open('CSV_Database.csv', 'a') as f_object:
    
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(dict)
    
        # Close the file object
        f_object.close()