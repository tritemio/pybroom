# pybroom

pybroom is the python "cousin" of the R library [broom](https://github.com/dgrtwo/broom).

Pybroom converts fitting results objects (obtained with lmfit, scipy.optimize,
sklearn, et.) into [Pandas](http://pandas.pydata.org/)
[DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)
in tidy format
[(Wickham 2014)](http://dx.doi.org/10.18637/jss.v059.i10).
The tidy format creates an uniform interface to fit results and allows to
cleanly combine results from different fits (e.g. comparison of different
models, comparison of different datasets, etc.). Tidy DataFrames can be
much more easily plotted with
[seaborn](https://web.stanford.edu/~mwaskom/software/seaborn/) (and, increasingly,
[matplotlib](http://matplotlib.org/)).

Like broom, pybroom provides only 3 functions: `tidy`, `augment` and `glance`.
For more information refer to the [broom](https://github.com/dgrtwo/broom)
homepage and this [video presentation](https://www.youtube.com/watch?v=eM3Ha0kTAz4).
