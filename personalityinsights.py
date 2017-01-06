import json
import sys

from getopt import getopt
from getopt import GetoptError
from watson_developer_cloud import PersonalityInsightsV2
from watson_developer_cloud import WatsonException

__author__ = 'Ruslan Iakhin'

def usage(argv):
     print("usage: %s -u <url>" % argv[0])
     sys.exit(2)

def main(argv):
    personurl = ''
    response  = ''
    username  = '<ibm service username>'
    password  = '<ibm service password>'
    
    if len(argv) <= 1:
        usage(argv)
    
    try:
        opts, args = getopt(argv[1:],'u:')
    except GetoptError as error:
        print(str(error))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-u':
            personurl = arg
        else:
            usage(argv)
 
    personalityinsights = PersonalityInsightsV2(
        username = username,
        password = password
    )
    file = open('profile.json','r')
    text = file.read()
    file.close()

    try:
        response = personalityinsights.profile(
            text = text,
            content_type = 'application/json',
        )
    except WatsonException as error:
        print(str(error))

    print(json.dumps(response, indent = 4))

if __name__ == '__main__':
    main(sys.argv)
