import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="ana_photo_flow",
    version="0.1.0-dev1",
    url="https://github.com/ariegenature/ana-photo-flow",
    license='MIT',
    author="Yann Voté",
    author_email="ygversil@lilo.org",
    description="Simple photos publishing workflow in use at association des naturalistes de l'Ariège (also CEN Ariège and CPIE Ariège).",
    long_description=read("README.rst"),
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'celery',
        'circus',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'check-manifest',
            'bumpversion',
            'flake8',
            'pytest',
            'readme_renderer',
            'tox',
            'twine',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: French',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
    ],
)
