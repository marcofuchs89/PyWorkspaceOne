import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyws1uem',
    version='0.0.1',
    description=('PyWorkspaceOneUEM is a Python API library for '
                 '[VMware Workspace ONE UEM] (https://www.vmware.com/content/vmware/vmware-published-sites/us/products/workspace-one.html.html) formerly known as [AirWatch] (https://www.air-watch.com/) 9.1+'),
    url='https://github.com/marcofuchs89/PyWorkspaceOne',
    author='marcofuchs89',
    author_email='marco@fusche.net',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
