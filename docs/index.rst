.. pybroom documentation master file, created by
   sphinx-quickstart on Mon Jul 25 15:02:27 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pybroom's documentation!
===================================

:Latest Version: |version|

**Pybroom** is a small python 3 library for converting fitting results
(curve fitting or other optimizations)
to `Pandas <http://pandas.pydata.org/>`__
`DataFrame <http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe>`__
in tidy format
`(Wickham 2014) <http://dx.doi.org/10.18637/jss.v059.i10>`__.
DataFrames in tidy format (or long-form) follow a simple rule:
one "observation" per row and one "variable" per column.
This simple structure makes it easy to process the data with clear and
`well-understood idioms <http://tomaugspurger.github.io/modern-5-tidy.html>`__
(for filtering, aggregation, etc.) and allows
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

Like the R library broom, pybroom provides 3 functions: `glance`, `tidy` and
`augment`. The `glance` function returns fit statistics, one for each
fit result (e.g. fit method, number of iterations, chi-square etc.).
The `tidy` function returns data for each fitted parameter
(e.g. fitted value, gradient, bounds, etc.).
The `augment` function returns data with the same size as the fitted
data points (evaluated best-fit model, residuals, etc.).
Additionally, pybroom has two functions `tidy_to_dict` and `dict_to_tidy`
for conversion between dictionaries and 2-columns tidy DataFrames.

Currently, supported fit result object are:

- `scipy.optimize.OptimizeResult`
- `lmfit.model.ModelResult` (returned by `lmfit.Model.fit()`)
- `lmfit.minimizer.MinimizerResult` (returned by `lmfit.minimizer()`)

Note that the 3 functions (glance, tidy and augment) are implemented only for
the fit-result objects that are relevant. For example, `augment` cannot
process lmfit's `MinimizerResult` or scipy's `OptimizeResult` because
there is little or no data relevant to each data point.

Support for result objects from other libraries such as
`sklearn` can be added based on user request
(`PR welcome! <https://github.com/tritemio/pybroom>`__).

Installation
------------

Install pybroom with `pip` (python 3 only)::

    pip install pybroom

Dependencies are only pandas and lmfit (0.9.5+, which in turn requires scipy).
However, matplotlib and seaborn are strongly recommended (and necessary
to run the example notebooks).


.. toctree::
   :maxdepth: 1
   :caption: Example Notebooks

   notebooks/pybroom-example.ipynb
   notebooks/pybroom-example-multi-datasets.ipynb
   notebooks/pybroom-example-multi-datasets-minimize.ipynb
   notebooks/pybroom-example-multi-datasets-scipy-robust-fit.ipynb

.. toctree::
    :maxdepth: 1
    :caption: Reference

    api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
