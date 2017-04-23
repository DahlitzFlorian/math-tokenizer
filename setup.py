from setuptools import setup

setup(
    name='math-tokenizer',
    version='1.0.1',
    packages=['tokenizer',],
    license='MIT',
    description='Simple and lightweighted tokenizer for mathematical functions',
    long_description=open('README.rst').read(),
    author='Florian Dahlitz',
    author_email='f2dahlitz@freenet.de',
    url='https://github.com/DahlitzFlorian/math-tokenizer',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tokenizer math math-functions token analysis',
)