import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blazir",
    version="0.0.1",
    author="Robert Stein",
    author_email="rdstein@caltech.edu",
    description="Blazar IR project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="astronomy image IR blazar",
    url="https://github.com/robertdstein/blazir",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.10',
    install_requires=[
        "jupyter",
        "matplotlib",
        "pandas",
    ]
)