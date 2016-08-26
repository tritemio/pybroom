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

**Pybroom** is a small python 3+ library for converting collections of
fit results (curve fitting or other optimizations)
to `Pandas <http://pandas.pydata.org/>`__
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`__
in tidy format (or long-form)
`(Wickham 2014) <http://dx.doi.org/10.18637/jss.v059.i10>`__.
Once fit results are in tidy DataFrames, it is possible to leverage
`common patterns <http://tomaugspurger.github.io/modern-5-tidy.html>`__
for tidy data analysis. Furthermore powerful visual
explorations using multi-facet plots becomes easy thanks to libraries
like `seaborn <https://pypi.python.org/pypi/seaborn/>`__ natively
supporting tidy DataFrames.

See the `pybroom homepage <http://pybroom.readthedocs.io/>`__ for more info.
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
    keywords=('dataframe tidy-data long-form model fitting tidyverse'))
