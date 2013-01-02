
import blake2
from attest import Tests

tests = Tests()


@tests.test
def blake2b():
    """Test blake2s results"""
    assert blake2.blake2("blake2", key="blake2") == 'b202b477a797e984e6a2b976ca4cb7d3944004b3ef6cde80341c7853a2dd7e2f9e08cda6d7372812cf75e8c7741fb656cec3a119772e2e715cebc76433fafd4d'
    assert blake2.blake2("hello world", key="hello world") == '45589476ec87eec2e35a20817e822ec894a3c35116dfb8a35b2b966a7193deafbb65684f102a8dee449d75065251e7d8fe71c05b4d2452329caf6c5bb48d66f9'
    assert blake2.blake2("hello world", hashSize=32, key="hello world") == '177a8d7754e0aaa6645179c6c9933c3c57a4880e91223f56ded5d3e3cd7144dd'
    assert blake2.blake2("hello world", hashSize=16, key="hello world") == '8fe7d57f5c53d8afd00f552269502b81'
    assert blake2.blake2("hello world", hashSize=4, key="hello world") == 'bbd7cc6e'


if __name__ == '__main__':
    tests.run()
