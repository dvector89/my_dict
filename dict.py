# -*- coding: utf-8 -*-
import requests
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def request_youdao(word):
    """
    :param word:
    :return: a dict of info about word
    """
    uname = 'blabla'
    key = 'blabla'
    url = "http://fanyi.youdao.com/openapi.do?keyfrom=%s" \
          "&key=%s&type=data&doctype=json&version=1.1&q=" % (uname, key)
    url = url + word
    return requests.get(url).json()


def display_json_youdao(json):
    print ' '*14 + bcolors.OKBLUE + json['query'] + bcolors.ENDC
    print 'phonetic-us: [%s%s%s]' % (bcolors.WARNING,
                                     json['basic']['us-phonetic'],
                                     bcolors.ENDC)
    print '   phonetic: [%s]' % json['basic']['phonetic']
    print 'phonetic-uk: [%s]' % json['basic']['uk-phonetic']
    print '*** explain ***'
    print bcolors.OKGREEN + '\n'.join(json['basic']['explains']) + bcolors.ENDC


if __name__ == "__main__":
    usage = "python %s word" % sys.argv[0]
    if len(sys.argv) != 2:
        print "error.", usage
        exit()

    word = sys.argv[1]
    try:
        json = request_youdao(word)
        display_json_youdao(json)
    except:
        print "something wrong"
