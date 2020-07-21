from setuptools import setup, find_packages

requires = [
    'flask',
    'urllib',
    'werkzeug',
]

setup(
    name='sat_labeling',
    version='0.0',
    description='Tool to label satillite images',
    author='USAFA Cadets',
    keywords='satillite labeling',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
)