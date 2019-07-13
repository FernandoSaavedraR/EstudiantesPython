from setuptools import setup

setup(
    name='saes',
    version='0.1',
    py_modules=['saes'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        saes=saes:cli
    ''',
)