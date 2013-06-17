from setuptools import setup, find_packages

setup(
    name='Gabriel',
    version='0.1.0',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'gabriel = gabriel.__main__:main'
        ],
    },
    license='MIT',
    long_description=open('README.md').read(),
    requires=[
        'pyyaml',
        'mako',
        ],
)
