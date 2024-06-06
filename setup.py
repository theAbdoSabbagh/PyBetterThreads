import os

from setuptools import setup

base_path = os.path.abspath(os.path.dirname(__file__))

requirements = []

readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name="PyBetterThreads",
    author="theAbdoSabbagh",
    url="https://github.com/theAbdoSabbagh/PyBetterThreads",
    project_urls={
        "Documentation": "https://github.com/theAbdoSabbagh/PyBetterThreads/blob/main/README.md",
        "Issue tracker": "https://github.com/theAbdoSabbagh/PyBetterThreads/issues",
    },
    version="0.0.3",
    packages=["PyBetterThreads"],
    license="MIT",
    description="Threads, but with more features!",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
