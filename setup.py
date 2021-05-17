import pathlib
import setuptools

long_description = pathlib.Path("README.md").read_text()

setuptools.setup(
    name="colorviews",
    version="0.1-alpha0",
    author="Julin S",
    author_email="",
    description="A simple module to handle colors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ju-sh/colorviews",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        'Changelog': 'https://github.com/ju-sh/colorviews/blob/master/CHANGELOG.md',
        'Issue Tracker': 'https://github.com/ju-sh/colorviews/issues',
    },
    install_requires=[],
    python_requires='>=3.6',
)
