import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name=Time_for_an_Adventure
    version="0.0.1",
    author="Ethan Kubistek",
    author_email=ekubistek@gmail.com,
    url=https://github.com/EthanKubistek/Time_for_an_Adventure,
    description=New text based game with a structured skeletom,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

