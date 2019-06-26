import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="share-array-widmi",
    version="0.0.1",
    author="Michael Widrich",
    author_email="widrich@ml.jku.at",
    description="Easily share numpy arrays between processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/widmi/multiprocess-shared-numpy-arrays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)