import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="decimal_sdk-python-sdk",  # Replace with your own username
    version="0.0.1",
    author="DecimalTeam",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/decimalteam/decimal-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)