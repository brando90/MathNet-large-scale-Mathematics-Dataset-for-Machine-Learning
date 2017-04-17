from setuptools import setup

setup(
    name='main_pro_lib', #project name
    version='0.1.0',
    description='my research library for EIT',
    #url
    author='Brando Miranda',
    author_email='brando90@mit.edu',
    license='MIT',
    packages=['qaflow'],
    #install_requires=['numpy','keras','namespaces','pdb','scikit-learn','scipy','virtualenv']
    #install_requires=['numpy','keras','namespaces','pdb']
    install_requires=['numpy','pdb','maps','sympy','require']
)
