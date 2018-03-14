from setuptools import setup

setup(
    name='tools',
    version='0.1',
    packages=['tools'],
    entry_points = {
        'console_scripts': [
            'debug_flash=tools.debug_flash:main',
            'debug_run=tools.debug_run:main'
        ]
    }
)
