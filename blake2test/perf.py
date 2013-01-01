
import datetime
import blake2
import hashlib


def testmd5():
    start = datetime.datetime.now()
    for x in xrange(10000):
        hashlib.md5("Nobody inspects the spammish repetition").hexdigest()
    end = datetime.datetime.now()
    print end - start

def testsha1():
    start = datetime.datetime.now()
    for x in xrange(10000):
        hashlib.sha1("Nobody inspects the spammish repetition").hexdigest()
    end = datetime.datetime.now()
    print end - start


def testsha224():
    start = datetime.datetime.now()
    for x in xrange(10000):
        hashlib.sha224("Nobody inspects the spammish repetition").hexdigest()
    end = datetime.datetime.now()
    print end - start

def testsha256():
    start = datetime.datetime.now()
    for x in xrange(10000):
        hashlib.sha256("Nobody inspects the spammish repetition").hexdigest()
    end = datetime.datetime.now()
    print end - start

def testsha384():
    start = datetime.datetime.now()
    for x in xrange(10000):
        hashlib.sha384("Nobody inspects the spammish repetition").hexdigest()
    end = datetime.datetime.now()
    print end - start

def testsha512():
    start = datetime.datetime.now()
    for x in xrange(10000):
        hashlib.sha512("Nobody inspects the spammish repetition").hexdigest()
    end = datetime.datetime.now()
    print end - start

def testblake2():
    start = datetime.datetime.now()
    for x in xrange(10000):
        blake2.blake2("Nobody inspects the spammish repetition")
    end = datetime.datetime.now()
    print end - start

if __name__ == '__main__':
    testmd5()
    testsha1()
    testsha224()
    testsha256()
    testsha384()
    testsha512()
    testblake2()
