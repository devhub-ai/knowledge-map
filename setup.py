from setuptools import setup, find_packages

setup(
    name='knowledge-map',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[  # Add any dependencies you need here  
    ],
    entry_points={
        'console_scripts': [
            'knowledgeMap = knowledgeMap:hello',
        ],    
    },
)