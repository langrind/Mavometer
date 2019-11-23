import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mavometer",
    version="0.1.0",
    author="Nik Langrind",
    author_email="langrind@gmail.com",
    description="Application to monitor bandwidth and message composition of a MAVLink stream",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/langrind/mavometer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pymavlink',
          'uqtie>=0.1.1',
    ],
    python_requires='>=3.6',
    scripts=['bin/mavometer'],
)
