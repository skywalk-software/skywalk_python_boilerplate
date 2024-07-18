from setuptools import setup, find_packages

setup(
    name="skywalk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "python-dotenv==0.19.2",
    ],
    author="Skywalk Software Team",
    author_email="jackie@skywalk.com",
    description="A boilerplate for Python projects at Skywalk",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/skywalk/skywalk_python_boilerplate",
)
