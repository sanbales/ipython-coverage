from io import open
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md'), encoding='utf-8').read()


version = '0.0.0'


setup(
    author='Santiago Balestrini-Robinson',
    author_email='sanbales@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
    ],
    description="Coverage access via IPython",
    include_package_data=True,
    install_requires=[
        'coverage>4,<5',
        'ipython>=1.0',
    ],
    keywords='testing coverage ipython',
    license='MIT',
    long_description=README,
    name='ipython-coverage',
    packages=find_packages('.'),
    test_suite="tests",
    url='https://pypi.python.org/pypi/ipython-coverage',
    version=version,
    zip_safe=False,
)
