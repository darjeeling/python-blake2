from distutils.core import setup, Extension
 
module1 = Extension('blake2', sources = ['src/blake2module.c',"src/blake2b-ref.c"],
                extra_compile_args = ["-std=c99", "-Wall", "-pedantic"] )
 
setup (name = 'blake2',
        version = '0.1',
        description = 'This is a demo package',
        ext_modules = [module1])
