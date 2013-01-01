
import blake2
from attest import Tests

tests = Tests()


@tests.test
def blake2b():
    """Test blake2s results"""
    assert blake2.blake2("blake2") == '22ccfc5a19a58358eb07a89e9b2c29356fff5ed0a50364ae1391649fc6152a2a700fc712f1ba031f3ee6e64736feacf49308755eabc9719352b54192b820f435'
    assert blake2.blake2("hello world") == '1b48ac3711e63c9dadcff921866bf4adabc4b0b204399d582b5d695e67c29a100bade80ec193ae220de7aeb200d7a4069b917d3d4b4e6a230b0dc0a5c8a03c3e'
    assert blake2.blake2("hello world",hashSize=32) == 'a9f88a40d4d7840b1669c0da696b5db1e545e9b6b606a13d500e0787f2cb375e'
    assert blake2.blake2("hello world",hashSize=16) == 'a5bd8867c9201df110adf0c20d164f7a'
    assert blake2.blake2("hello world",hashSize=4) == '72920435'


if __name__ == '__main__':
    tests.run()
