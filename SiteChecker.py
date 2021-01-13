import requests
import os.path
import argparse

def check_site(site):
    try:
        requests.get(site, timeout=10)
        print(f'Checking site: {site}\t Status: Up')
    except:
        print(f'Checking site: {site}\t Status: Down')

def check_sites(file):
    lines = file.readlines()
    for line in lines:
        check_site(line)

def open_file(name):
    try:
        file = open(name, 'r')
        check_sites(file)
        file.close()
    except:
        print('File not found')

parser = argparse.ArgumentParser(description='Check websites\' status')
parser.add_argument('sites', help='The website(s) to be checked', nargs='*')
parser.add_argument('-f', help='A .txt file with websites to check', nargs='?')
args = parser.parse_args()

if args.sites != []:
    for site in args.sites:
        check_site(site)

if args.f:
    open_file(args.f)
