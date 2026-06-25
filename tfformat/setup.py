from setuptools import setup, find_packages

setup(
    name="tfformat",
    version="0.9.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'tfformat': ['magicDB.json'],
    },
    entry_points={
        'console_scripts': [
            'tfformat=tfformat.main:main',
        ],
    },
    author="Hermit Winters",
    description="True File Format Detector",
)
