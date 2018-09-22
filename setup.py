"""``k8satt`` lives on
https://github.com/hhollenstain/k8satt
"""
from setuptools import setup, find_packages
import k8satt

INSTALL_REQUIREMENTS = [
    'boto3==1.7.84',
]

TEST_REQUIREMENTS = {
    'test':[
        'boto3==1.7.84',
        'pytest',
        'pylint',
        'moto==1.3.3',
        'sure',
        ]
    }

setup(
    name='k8satt',
    version=k8satt.VERSION,
    description='kubernetes all the things',
    url='https://github.com/hhollenstain/k8satt',
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIREMENTS,
    extras_require=TEST_REQUIREMENTS,
    entry_points={
        'console_scripts':  [
            'k8satt = k8satt.k8satt:main'
        ],
    },
    )
