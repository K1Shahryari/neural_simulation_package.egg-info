from setuptools import setup, find_packages

setup(
    name='neural_simulation_package',
    version='0.1',
    author='K1 Shahryarimorad',
    author_email='k11shahryari@email.com',
    description='A package for simulating neural networks',
    packages=find_packages(),
    install_requires=[
        'numpy',  # Add other dependencies here if needed
        'matplotlib'
    ],
)