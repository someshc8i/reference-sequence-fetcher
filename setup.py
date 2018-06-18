import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
install_requires = []


setuptools.setup(
    name="reference-sequence-fetcher",
    version="0.0.1",
    author="Somesh Chaturvedi",
    author_email="somesh.08.96@gmail.com",
    description="A client library for Reference Sequence Retrieval API ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/someshchaturvedi/reference-sequence-fetcher",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        reference_sequence_fetcher=reference_sequence_fetcher.main:main
    ''',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
