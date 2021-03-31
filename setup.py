from setuptools import setup, find_packages

setup(
    name='presearch-node-updater',
    version='1.0.0',
    url='https://github.com/aussedatlo/presearch-node-updater',
    author='Louis Aussedat',
    author_email='aussedat.louis@gmail.com',
    description='Small cli script to update preseach-node',
    packages=find_packages(),
	scripts = [
		'presearch-node-updater',
    ],
    install_requires=[
        'requests >= 2.25.1',
    ],
)