from setuptools import setup
#import versioneer


def get_version():
    # http://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
    from ast import parse
    with open('pybroom.py') as f:
        version = parse(next(filter(
            lambda line: line.startswith('__version__'), f))).body[0].value.s
    return version


long_description = """
pybroom
=======

Pybroom converts fitting results objects into
`Pandas <http://pandas.pydata.org/`__
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`__
in tidy format
`(Wickham 2014) `<http://dx.doi.org/10.18637/jss.v059.i10>`__.

The tidy format creates an uniform interface to fit results and allows to
cleanly combine results from different fits (e.g. comparison of different
models, comparison of different datasets, etc.). Moreover, tidy DataFrames
can be easily and systematically plotted with
`seaborn <https://web.stanford.edu/~mwaskom/software/seaborn/>`__
(and, increasingly,
`matplotlib <http://matplotlib.org/>`__).
"""

setup(
    name='pybroom',
    version=get_version(),
    #version=versioneer.get_version(),
    #cmdclass=versioneer.get_cmdclass(),
    author='Antonino Ingargiola',
    author_email='tritemio@gmail.com',
    url='https://github.com/tritemio/pybroom',
    download_url='https://github.com/tritemio/pybroom',
    install_requires=['pandas', 'lmfit', 'setuptools'],
    license='MIT',
    description=("Make tidy DataFrames from messy fit/model results."),
    long_description=long_description,
    platforms=('Windows', 'Linux', 'Mac OS X'),
    classifiers=['Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Scientific/Engineering',
                 'License :: OSI Approved :: MIT License'],
    py_modules=['pybroom'],
    keywords=('dataframe tidy-data long-form model fitting'))
