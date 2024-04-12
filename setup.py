from setuptools import setup, Command

class HelloWorldCommand(Command):
    description = "prints 'Hello embedded world'"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Hello embedded world")

setup(
    name='HelloWorld',
    version='0.1',
    description='A simple script that prints "Hello embedded world"',
    author='mikolaj-t',
    author_email='mikolaj.t@outlook.com',
    packages=['pygpio'],
    cmdclass={
        'hello': HelloWorldCommand,
    },
)