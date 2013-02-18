
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
    assert blake2.blake2("hello\x00world", key="hello\x00world") == 'e06e51bbdc12363243a55ddc23aaeb310faceec72e21d93c85d7e77360aa48cb6baf2963661bf857b1686c89f5dd209f0abee10aa2e38d0318043718976bcb60'
    assert blake2.blake2(None) == None


@tests.test
def blake2s():
    """Test blake2s results"""
    assert blake2.blake2s("blake2", key="blake2") == '9b2c152a9567b530af1dc6549e1f8b67a278b710a1512c92dca5236d27309f87'
    assert blake2.blake2s("hello world", key="hello world") == '846d7f4e70f94df2b07e2f5d59d271d5b4627ab64cc0fc376f411448528bee49'
    assert blake2.blake2s("hello world", hashSize=16, key="hello world") == '4e989fc7739d052dd93ec88962137c08'
    assert blake2.blake2s("hello world", hashSize=4, key="hello world") == 'fef7f902'
    assert blake2.blake2s("hello\x00world", key="hello\x00world") == '36429945e82aec7853fd2bd1c7349a65e4457db81c059b287f7a859e3b26e3f4'
    assert blake2.blake2(None) == None



if __name__ == '__main__':
    tests.run()
