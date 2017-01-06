import json
import sys
import os.path

from getopt import getopt
from getopt import GetoptError
from watson_developer_cloud import AlchemyLanguageV1
from watson_developer_cloud import WatsonException 

__author__ = 'Ruslan Iakhin'

def usage(argv):
     print("usage: %s -u <url>" % argv[0])
     sys.exit(2)

def main(argv):
    response = ''
    url      = ''
    alchemy  = AlchemyLanguageV1(api_key='<your key>')

    if len(argv) <= 1:
        usage(argv)
    
    try:
        opts, args = getopt(argv[1:],"u:")
    except GetoptError as error:
        print(str(error))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-u':
            url = arg
        else:
            usage(argv)
    try: 
        response = alchemy.combined(
            url = url,
            extract = 'doc-emotion,doc-sentiment'
        )
    except WatsonException as error:
        print(str(error))
        sys.exit(2)
            
    if 'language' in response:
        print("Language: %s" % response['language'])

    if 'docSentiment' in response:
        print("Sentiment: %s" % response['docSentiment']['type'])   

    if 'docEmotions' in response:
        for item in response['docEmotions']:
            print("%s: %s" % (item, response['docEmotions'][item]))
    
if __name__ == '__main__':
    main(sys.argv)

