Why Pybroom?
============

Which problem we are trying to solve?
------------------------------------

DataFrames in tidy format (or long-form) follow a simple rule:
one "observation" per row and one "variable" per column.
This simple structure makes it easy to process the data with clear and
`well-understood idioms <http://tomaugspurger.github.io/modern-5-tidy.html>`__
(filtering, aggregation, etc.) and allows
plot libraries to automatically generate complex plots in which many
variables are compared. Plotting libraries supporting tidy DataFrames
include `seaborn <https://web.stanford.edu/~mwaskom/software/seaborn/>`__,
recent versions of `matplotlib <http://matplotlib.org/>`__,
`bokeh <http://bokeh.pydata.org/>`__ and
`altair <https://github.com/ellisonbg/altair>`__.

But, while data is oftentimes represented in tidy DataFrames, fit results
are usually stored in a variety of custom objects and are harder
to manipulate, compare and plot.

Pybroom to the rescue!
----------------------

Pybroom allows to convert several types of fit results to tidy
DataFrames, and is particularly useful for handling collections
of such fit results.
Pybroom development was inspired by the R library
`broom <https://github.com/dgrtwo/broom>`__.
You can watch `this video <https://www.youtube.com/watch?v=eM3Ha0kTAz4>`__
for details of the philosophy behind broom (and by extension pybroom).

Like the R library broom, pybroom provides 3 functions: `glance`, `tidy` and
`augment`. The `glance` function returns fit statistics, one for each
fit result (e.g. fit method, number of iterations, chi-square etc.).
The `tidy` function returns data for each fitted parameter
(e.g. fitted value, gradient, bounds, etc.).
The `augment` function returns data with the same size as the fitted
data points (evaluated best-fit model, residuals, etc.).
Additionally, pybroom has two functions `tidy_to_dict` and `dict_to_tidy`
for conversion between dictionaries and 2-columns tidy DataFrames.

Collections of fit results can be in `list`, `dict`,
or any nested `dict`/`list` combination.
When a collection of fit result is used as input, pybroom functions
return a DataFrame with additional "categorical" column(s) containing
the dict keys or the list index.

Currently, supported fit result object are:

- `scipy.optimize.OptimizeResult` returned by several functions in
  `scipy.optimize`;
- `lmfit.model.ModelResult` (returned by `lmfit.Model.fit()`);
- `lmfit.minimizer.MinimizerResult` (returned by `lmfit.minimizer()`).

Note that the 3 functions (glance, tidy and augment) are implemented only for
the fit-result objects that are relevant. For example, `augment` cannot
process lmfit's `MinimizerResult` or scipy's `OptimizeResult` because
there is little or no data relevant to each data point.

Support for result objects from other libraries such as
`sklearn` can be added based on user request
(`PR welcome! <https://github.com/tritemio/pybroom>`__).
