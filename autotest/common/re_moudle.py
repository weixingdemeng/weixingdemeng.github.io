import re


def re_findone(pattern, string, num=0):
    try:
        return re.findall(pattern=pattern, string=string)[num]
    except Exception as e:
        raise e


def re_findall(pattern, string):
    try:
        return re.findall(pattern, string)
    except Exception as e:
        raise e


def re_findmany(pattern, string, start=0, end=-1):
    try:
        return re.findall(pattern, string)[start:end]
    except Exception as e:
        raise e


def re_search(pattern, string):
    try:
        result = re.search(pattern, string).groups()
        return result
    except Exception as e:
        raise e

def re_match(pattern, string):
    try:
        result = re.match(pattern, string).groups()
        return result
    except Exception as e:
        raise e