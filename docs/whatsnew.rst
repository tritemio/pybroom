Pybroom's Release Notes
=======================

Version 0.2
-----------

- Improved support for `scipy.optimize` fit result.
- In addition to list of fit results, `pybroom` now supports:

    - dict of fit results,
    - dict of lists of fit results
    - any other nested combination.

- When input contains a dict, pybroom adds "key" column of type
  `pandas.Categorical`.
  When input contains a list, pybroom adds a "key" column (i.e. list index)
  of type `int64`.
- Updated and expanded documentation and notebooks.

Version 0.1
-----------

- Support `lmfit` and `scipy.optimize` fit results.
- Support lists of fit results.
