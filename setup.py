from setuptools import setup, find_packages


setup(
    name="LLR",
    version="1.0",
    description="Local linear regression package",
    url="https://github.com/ashod1/LLR-package",
    author="Ashod Khederlarian",
    author_email="ask126@pitt.edu",
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        "sklearn",
        "numpy",
    ],
    packages=find_packages()
)
