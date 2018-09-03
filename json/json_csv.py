import json
import csv
import sys, getopt


def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('csv_json.py -i <path to inputfile> -o <path to outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('json_csv.py -i <path to inputfile> -o <path to outputfile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
       
    read_json(input_file, output_file)


def reduce_item(key, value):
    global reduced_item
    
    #Reduction Condition 1
    if type(value) is list:
        i=0
        for sub_item in value:
            reduce_item(key+'_'+to_string(i), sub_item)
            i=i+1

    #Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(key+'_'+to_string(sub_key), value[sub_key])
    


def to_string(s):
    try:
        return str(s)
    except:
        #Change the encoding type if needed
        return s.encode('utf-8')
        
#Read CSV File
def read_json(json_file, csv_file_path ):
    with open(json_file) as f:
        data = json.load(f)
    print(data)
    data_to_be_processed = data
    for item in data_to_be_processed:
        reduced_item = {}
        reduce_item(item)

        header += reduced_item.keys()

        processed_data.append(reduced_item)

    header = list(set(header))
    header.sort()

    with open(csv_file_path, 'w+') as f:
            writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in processed_data:
                writer.writerow(row)
    print ("Just completed writing csv file with %d columns" % len(header))
   


# employee_parsed = json.loads(employee_data)


# emp_data = employee_parsed['employee_details']

# # open a file for writing

# employ_data = open('/tmp/EmployData.csv', 'w')

# # create the csv writer object

# csvwriter = csv.writer(employ_data)

# count = 0

# for emp in emp_data:

#       if count == 0:

#              header = emp.keys()

#              csvwriter.writerow(header)

#              count += 1

#       csvwriter.writerow(emp.values())

# employ_data.close()

if __name__ == "__main__":
   main(sys.argv[1:])