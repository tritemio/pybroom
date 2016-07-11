# pybroom

pybroom is the python "cousin" of the R library [broom](https://github.com/dgrtwo/broom).

Pybroom converts fitting results objects into [Pandas](http://pandas.pydata.org/)
[DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)
in tidy format
[(Wickham 2014)](http://dx.doi.org/10.18637/jss.v059.i10).
Currently the only supported fit result object is `lmfit.model.ModelResult`, but
support for other fitting objects such as the ones used in  `scipy.optimize` and 
`sklearn` can be added (PR welcome!).

The tidy format creates an uniform interface to fit results and allows to
cleanly combine results from different fits (e.g. comparison of different
models, comparison of different datasets, etc.). Moreover, tidy DataFrames
can be easily and systematically plotted with
[seaborn](https://web.stanford.edu/~mwaskom/software/seaborn/) (and, increasingly,
[matplotlib](http://matplotlib.org/)).

Like broom, pybroom provides only 3 functions: `tidy`, `augment` and `glance`.
For usage example see the included notebooks (read them executed
[here](https://gist.github.com/tritemio/be72c6e8bef36031af14a610b1303c26) and 
[here](https://gist.github.com/tritemio/aca5fb2f3de4dbfa46e8ee04efe067cd)).

I was inspired to start pybroom after watching this presentation by
David Robinson (broom's author):

- [broom: Converting statistical models to tidy data frames](https://www.youtube.com/watch?v=eM3Ha0kTAz4).
