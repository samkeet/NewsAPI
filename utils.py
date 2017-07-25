import argparse
import json
import requests

args = {}


def load_args():
    '''Parse the arguments with argparse utility.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--articles', action='store_true')
    parser.add_argument('-s', '--source', nargs=1)
    # parser.add_argument('-ls', '--source_list')
    # parser.add_argument('api', help='API Key')
    parser.add_argument('-d', '--debug', action='store_true')
    global args
    args = parser.parse_args()


def enlist_sources():
    '''Enlist all news sources.
    '''
    source = 'https://newsapi.org/v1/sources?language=en'
    result_json = requests.get(source).text
    result_json = json.loads(result_json)
    i = 1
    print('NEWS SOURCES ===============>\n\n')
    for each_source in result_json['sources']:
        print(i, each_source['id'])
        i += 1


def log(*arguments):
    '''Logger is set for debugging only if
    '-d' or '--debug' is given from commandline
    '''
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    if args.debug:
        print('{}[dbg]{} '.format(WARNING, ENDC), *arguments)
