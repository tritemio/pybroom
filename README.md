# pybroom

pybroom is the python "cousin" of the R library [broom](https://github.com/dgrtwo/broom).

Pybroom converts fitting results objects into [Pandas](http://pandas.pydata.org/)
[DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)
in tidy format
[(Wickham 2014)](http://dx.doi.org/10.18637/jss.v059.i10).
The tidy format is a uniform interface which allows to
cleanly combine results from different fits (e.g. comparison of different
models, comparison of different datasets, etc.). Moreover, tidy DataFrames
can be easily and systematically plotted with
[seaborn](https://web.stanford.edu/~mwaskom/software/seaborn/) (and, increasingly,
[matplotlib](http://matplotlib.org/)).

Like broom, pybroom provides 3 functions: `tidy`, `augment` and `glance`.
For usage example see the [documentation](http://pybroom.readthedocs.io/) 
which includes example notebooks (you can find the notebooks in 
[docs/notebooks](docs/notebooks)). 
Moreover, pybroom provides two functions `tidy_to_dict` and `dict_to_tidy`
for conversion between dictionaries and 2-columns tidy DataFrame. These
functions are useful to call python functions with parameters stored
in tidy DataFrames or to create tidy DataFrames from plain dictionaries.

Currently, supported fit result object are:
- `lmfit.model.ModelResult` (returned by `lmfit.Model.fit()`)
- `lmfit.minimizer.MinimizerResult` (returned by `lmfit.minimizer()`)

Support for `scipy.optimize` or objects used in other libraries such as
`sklearn` can be added based on user request (PR welcome!).

I was inspired to start pybroom after watching this presentation by
David Robinson (broom's author):

- [broom: Converting statistical models to tidy data frames](https://www.youtube.com/watch?v=eM3Ha0kTAz4).
