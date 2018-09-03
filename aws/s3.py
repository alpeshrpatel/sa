import pandas as pd
import boto3
import io
import sys, getopt
import csv
import json

def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'csv_json.py -i <path to inputfile> -o <path to outputfile> -f <dump/pretty>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
    read_csv(input_file, output_file, format)


def read_csv(bucketName, fileName):
    s3_file_key = fileName
    bucket = bucketName

    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=s3_file_key)

    initial_df = pd.read_csv(io.BytesIO(obj['Body'].read()))


if __name__ == "__main__":
   readCSV(sys.argv[1:])