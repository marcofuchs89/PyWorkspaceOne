import os

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyws1uem',
    version='0.0.6',
    description=('PyWorkspaceOneUEM is a Python API library for VMware Workspace ONE UEM formerly known as AirWatch'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/marcofuchs89/PyWorkspaceOne',
    author='marcofuchs89',
    author_email='marco@fusche.net',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=['requests'],
    keywords='uem airwatch api',
)
