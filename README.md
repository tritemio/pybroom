# pybroom

> *pybroom, the python's broom to tidy up messy fit results!*

**Pybroom** is a small python 3 library for converting fitting results
(curve fitting or other optimizations)
to [Pandas](http://pandas.pydata.org/)
[DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)
in tidy format
[(Wickham 2014)](http://dx.doi.org/10.18637/jss.v059.i10).
The DataFrames in tidy format (or long-form) follow a simple rule:
one "observation" per row and one "variable" per column.
This simple structure makes it easy to process the data with clear and
well-understood idioms (for filtering, aggregation, etc.) and allows
plot libraries to automatically generate complex plots in which many
variables are compared. Plotting libraries supporting tidy DataFrames
include [seaborn](https://web.stanford.edu/~mwaskom/software/seaborn/),
recent versions of [matplotlib](http://matplotlib.org/),
[bokeh](http://bokeh.pydata.org/) and
[altair](https://github.com/ellisonbg/altair).
pybroom development was inspired by the R library
[broom](https://github.com/dgrtwo/broom).

Like the R library broom, *pybroom* provides 3 functions: `tidy`, `augment` and `glance`.

For details see the [documentation](http://pybroom.readthedocs.io/)
which includes example notebooks (you can find the source notebooks in
[docs/notebooks](docs/notebooks)).

Pybroom was started after watching this presentation by
David Robinson (broom's author):

- [broom: Converting statistical models to tidy data frames](https://www.youtube.com/watch?v=eM3Ha0kTAz4).
