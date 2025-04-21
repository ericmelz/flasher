from setuptools import setup, find_packages

setup(
    name="flasher",
    version="0.1.0",
    packages=["src", "src.models", "src.data"],
    install_requires=[
        "streamlit>=1.44.1",
        "pydantic>=2.11.3",
    ],
) 