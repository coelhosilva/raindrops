import setuptools
import os

NAME = "raindrops"
VERSION = "0.0.1"
DESCRIPTION = "raindrops is a Python package for developing and building serverless applications in " \
              "Google Cloud Platform's Cloud Functions."
AUTHOR = "Lucas Coelho e Silva"
package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, "README.md")

with open(readme_filename, "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coelhosilva/raindrops.git",
    download_url="https://github.com/coelhosilva/raindrops/archive/refs/tags/v0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    keywordsList=['cloud computing', 'cloud functions', 'build tools'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Development Status :: 3 - Alpha"
    ],
    entry_points={
        'console_scripts': [
            'raindrops = raindrops.cli:main',
        ],
    },
    python_requires='>=3.6',
    include_package_data=True,
)
