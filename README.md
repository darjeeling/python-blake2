PYTHON BLAKE2 Module
============================
BLAKE2 is an improved version of BLAKE, one the finalists in the NIST SHA-3 competition. Like BLAKE or SHA-3, BLAKE2 offers the highest security, yet is fast as MD5 on 64-bit platforms and requires at least 33% less RAM than SHA-2 or SHA-3 on low-end systems. This implementation uses the BLAKE2b variant of the algorithm which is optimized for 64-bit systems. The algorithm was designed by Jean-Philippe Aumasson, Samuel Neves, Zooko Wilcox-O'Hearn, and Christian Winnerlein.


Installation
------------
blake2 package is uploaded to pypi. you can use 

- easy_install blake2
- pip install blake2

Installation with source
------------
1. git clone https://github.com/darjeeling/python-blake2.git
1. cd python-blake2
1. python setup.py install



Usage
----
**you shoud apply same key to get same hash.**
**initialzed key shoud be given.**
```python
import blake2
blake2.blake2( data [, hashSize = 64,   key = "",  rawOutput = False ] )
blake2.blake2b( data [, hashSize = 64,   key = "",  rawOutput = False ] )
blake2.blake2s( data [, hashSize = 32,   key = "",  rawOutput = False ] )
```


More Info
---------
https://blake2.net/
