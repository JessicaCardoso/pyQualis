from setuptools import setup, find_packages
from os import path

# The directory containing this file
this_directory = path.abspath(path.dirname(__file__))

# The text of the README file
with open(path.join(this_directory, "README.md"), encoding="utf-8") as fid:
    README = fid.read()

with open(path.join(this_directory, "LICENSE")) as f:
    license = f.read()

setup(
    name="pyQualis",
    version="v0.0.0-alpha",
    description="Consultas das notas de qualis-periódicos via python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JessicaSousa/pyQualis",
    author="Ivan Pereira, Jessica Sousa",
    author_email="navi1921@gmail.com, jessicasousa.pc@gmail.com",
    license="MIT",
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Other Audience",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests", "pandas", "lxml", "beautifulsoup4"],
    package_data={"pyQualis": ["data/*"]},
    zip_safe=False,
)