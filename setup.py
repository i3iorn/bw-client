import setuptools

setuptools.setup(
    name="BW Client",
    version="0.1.0",
    author="Björn",
    author_email="bjorn@schrammel.dev",
    description="A Python package for BW Client.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        "bitwarden_sdk",
        "dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7"
)