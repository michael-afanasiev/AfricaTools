

from setuptools import setup

setup(
    name="aa_tools",
    version="0.0.1",
    py_packages=["AfricaTools"],
    install_requires=[
        "Click"
    ],
    entry_points="""
    [console_scripts]
    aa_tools=AfricaTools.cli:cli
    """
)