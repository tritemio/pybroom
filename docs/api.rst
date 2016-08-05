PyBroom API Documentation
=========================

.. automodule :: pybroom

Main Functions
--------------

The 3 high-level functions :func:`glance`, :func:`tidy` and :func:`augment`
allows tidying one or more fit results.
These are pybroom's most generic functions, accepting all the
the supported fit result objects, as well as a list/dict of such objects.
See also the examples at the beginning of this page and the example notebooks.

.. autofunction :: glance

.. autofunction :: tidy

.. autofunction :: augment


Dictionary conversions
----------------------

The two functions :func:`tidy_to_dict` and :func:`dict_to_tidy` provide
the ability to convert a tidy DataFrame to and from a python dictionary.

.. autofunction :: tidy_to_dict

.. autofunction :: dict_to_tidy


Specialized functions
---------------------

These are the specialized (i.e. low-level) functions, each converting one
specific object to a tidy DataFrame.

.. autofunction :: glance_scipy_result

.. autofunction :: tidy_scipy_result

.. autofunction :: glance_lmfit_result

.. autofunction :: tidy_lmfit_result

.. autofunction :: _augment_lmfit_modelresult
