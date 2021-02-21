import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bprimal",
    version="0.0.2",
    author="Bijesh Raj Kunwar",
    author_email="bijeshr.kunwar@gmail.com",
    description="A collection of random functions created to learn deploying a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bijeshofficial/bprimal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
