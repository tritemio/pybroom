from setuptools import setup
#import versioneer


def get_version():
    # http://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
    from ast import parse
    with open('pybroom.py') as f:
        version = parse(next(filter(
            lambda line: line.startswith('__version__'), f))).body[0].value.s
    return version


long_description = r"""
pybroom
=======

**Pybroom** is a small python 3 library for converting fitting results
(curve fitting or other optimizations)
to `Pandas <http://pandas.pydata.org/>`__
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`__
in tidy format
`(Wickham 2014) <http://dx.doi.org/10.18637/jss.v059.i10>`__.
The DataFrames in tidy format (or long-form) follow a simple rule:
one "observation" per row and one "variable" per column.
This simple structure makes it easy to process the data with clear and
well-understood idioms (for filtering, aggregation, etc.) and allows
plot libraries to automatically generate complex plots in which many
variables are compared. Plotting libraries supporting tidy DataFrames
include `seaborn <https://web.stanford.edu/~mwaskom/software/seaborn/>`__,
recent versions of `matplotlib <http://matplotlib.org/>`__,
`bokeh <http://bokeh.pydata.org/>`__ and
`altair <https://github.com/ellisonbg/altair>`__.
pybroom development was inspired by the R library
`broom <https://github.com/dgrtwo/broom>`__.
See `this video <https://www.youtube.com/watch?v=eM3Ha0kTAz4>`__
for details of the philosophy behind broom and pybroom.

See the `pybroom homepage<http://pybroom.readthedocs.io/>`__ for more info.
"""

setup(
    name='pybroom',
    version=get_version(),
    #version=versioneer.get_version(),
    #cmdclass=versioneer.get_cmdclass(),
    author='Antonino Ingargiola',
    author_email='tritemio@gmail.com',
    url='http://pybroom.readthedocs.io/',
    download_url='https://github.com/tritemio/pybroom',
    install_requires=['pandas', 'lmfit', 'setuptools'],
    license='MIT',
    description=("Make tidy DataFrames from messy fit/model results."),
    long_description=long_description,
    platforms=('Windows', 'Linux', 'Mac OS X'),
    classifiers=['Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Scientific/Engineering',
                 'License :: OSI Approved :: MIT License'],
    py_modules=['pybroom'],
    keywords=('dataframe tidy-data long-form model fitting'))
