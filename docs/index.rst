.. pybroom documentation master file, created by
   sphinx-quickstart on Mon Jul 25 15:02:27 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pybroom's documentation!
===================================

Pybroom is a small pure-python library for converting fitting results
(curve fitting or other optimizations)
to `Pandas <http://pandas.pydata.org/>`__
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`__
in tidy format
`(Wickham 2014) <http://dx.doi.org/10.18637/jss.v059.i10>`__.
The tidy DataFrames are a uniform interface to
easily combine results from different fits (e.g. comparison of different
models, comparison of different datasets, bootstrap sampling etc.).
Moreover, tidy DataFrames can be easily and systematically plotted with
`seaborn <https://web.stanford.edu/~mwaskom/software/seaborn/>`__ and
recent versions of `matplotlib <http://matplotlib.org/>`__
(as well as with new libraries such as `altair <https://github.com/ellisonbg/altair>`__).
`pybroom` was inspired by the R library `broom <https://github.com/dgrtwo/broom>`__.

Like the R library broom, `pybroom` main API
consists of only 3 functions: `tidy`, `augment` and `glance`.
Additionally, pybroom provides two functions `tidy_to_dict` and `dict_to_tidy`
for conversion between dictionaries and 2-columns tidy DataFrame.

Currently, supported fit result object are:

- `lmfit.model.ModelResult` (returned by `lmfit.Model.fit()`)
- `lmfit.minimizer.MinimizerResult` (returned by `lmfit.minimizer()`)

Support for `scipy.optimize` or objects used in other libraries such as
`sklearn` can be added based on user request (PR welcome!).

Installation
------------

Install pybroom with `pip` from the source folder::

    pip install .

Dependencies are only pandas and lmfit (0.9.5+). However, matplotlib and
seaborn are strongly recommended.


.. toctree::
   :maxdepth: 1
   :caption: Example Notebooks

   notebooks/pybroom-example.ipynb
   notebooks/pybroom-example-multi-datasets.ipynb
   notebooks/pybroom-example-multi-datasets-minimize.ipynb

.. toctree::
    :maxdepth: 1
    :caption: Reference

    api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
