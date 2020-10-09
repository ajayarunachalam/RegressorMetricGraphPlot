from distutils.core import setup
import setuptools

__version__ = '0.0.1'

def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setuptools.setup(
    name='regressormetricgraphplot',
    version=__version__,
    description='A simple package for comparing different Regression Models and Plotting with their most common evaluation metrics.',
    long_description = readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/ajayarunachalam/RegressorMetricGraphPlot',
    download_url='https://github.com/ajayarunachalam/RegressorMetricGraphPlot/tarball/master',
    install_requires=[
          'matplotlib', 'numpy', 'sklearn', 'pandas', 'scipy',

      ],
    license='MIT',
    include_package_data=True,
    author='Ajay Arunachalam',
    author_email='ajay.arunachalam08@gmail.com',
    )