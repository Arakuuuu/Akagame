from setuptools import setup, find_packages

setup(
    name='Akagame',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    entry_points={
        'console_scripts': [
            'akagame=main:main',  # Adjust this line based on your main function
        ]
    },
)
