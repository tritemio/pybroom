.. pybroom documentation master file, created by
   sphinx-quickstart on Mon Jul 25 15:02:27 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pybroom's documentation!
===================================

:Latest Version: |version|

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


Installation
------------

You can install pybroom from PyPI using the following command::

    pip install pybroom

or from `conda-forge <https://conda-forge.github.io/>`__ using::

    conda install -c conda-forge pybroom

Dependencies are python 3.4+, pandas and lmfit (0.9.5+, which in turn requires scipy).
However, matplotlib and seaborn are strongly recommended (and necessary
to run the example notebooks).

.. toctree::
    :maxdepth: 1
    :caption: Documentation

    intro
    whatsnew
    api

.. toctree::
   :maxdepth: 1
   :caption: Notebook Tutorials

   notebooks/pybroom-example.ipynb
   notebooks/pybroom-example-multi-datasets.ipynb
   notebooks/pybroom-example-multi-datasets-minimize.ipynb
   notebooks/pybroom-example-multi-datasets-scipy-robust-fit.ipynb


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
