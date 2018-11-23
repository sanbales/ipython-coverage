from io import open
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md'), encoding='utf-8').read()


version = '0.0.0'

install_requires = [
    'coverage>4,<5',
    'ipython>=1.0',
]


setup(
    name='ipython-sql',
    version=version,
    description="Coverage access via IPython",
    long_description=README,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Topic :: Database :: Front-Ends',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    keywords='testing coverage ipython',
    author='Santiago Balestrini-Robinson',
    author_email='sanbales@gmail.com',
    url='https://pypi.python.org/pypi/ipython-coverage',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
