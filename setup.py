from setuptools import setup, find_packages

setup(
    name="PhotoYearOrganizer",
    version="0.1.2",
    author='MasterCard007',
    author_email="your.email@example.com",
    description="A multi-threaded photo sorting tool based on metadata.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MasterCard007/PhotoYearOrganizer",
    packages=find_packages(),
    py_modules=["PhotoYearOrganizer.py"],
    install_requires=[
        "pillow",
        "icecream"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'photo_sort=PhotoYearOrganizer.py:sort_photos'
        ]
    },
)
