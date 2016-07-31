#
# Copyright (c) 2016 Antonino Ingargiola and contributors.
#

from collections import OrderedDict, namedtuple
import pandas as pd
import scipy.optimize as so
import lmfit

__version__ = '0.1dev'


def tidy(result, var_name='item', **kwargs):
    """Tidy DataFrame containing fitted parameter data from `result`.

    A function to tidy any of the supported fit result
    (or a list of fit results). This function will identify input type
    and call the relative "specialized" tidying function. When the input
    is a list, the returned DataFrame contains data from all the fit
    results.
    Supported fit result objects are `lmfit.ModelResult`,
    `lmfit.MinimizeResult` and `scipy.optimize.OptimizeResult`.

    Arguments:
        result (fit result object or list): one of the supported fit result
            objects or a list of supported fit result objects. When a list,
            all the elements need to be of the same type.
        var_name (string): name of the column containing an integer index
            that is different for each element in the list of fit results.
        param_names (string or list of string): names of the fitted parameters
            for fit results which don't include parameter's names
            (such as scipy's OptimizeResult). It can either be a list of
            strings or a single string with space-separated names.
        **kwargs: additional arguments passed to the underlying specialized
            tidying function.

    Returns:
        A DataFrame with one row for each fitted parameter.
        Columns include parameter properties such as best-fit value,
        standard error, eventual bounds/constrains, etc.
        When a list of fit-result objects is passed, the column `var_name`
        (`'item'` by default) contains the index of the object
        in the list.

    See also:
        For more information on the returned DataFrame and on additional
        arguments refer to the specialized tidying functions:
        :func:`tidy_lmfit_result` and :func:`tidy_scipy_result`.
    """
    # Find out what result is and call the relevant function
    if isinstance(result, list):
        return _multi_dataframe(result, tidy, var_name=var_name, **kwargs)
    elif (isinstance(result, lmfit.model.ModelResult) or
          isinstance(result, lmfit.minimizer.MinimizerResult)):
        return tidy_lmfit_result(result)
    elif isinstance(result, so.OptimizeResult):
        if 'param_names' not in kwargs:
            msg = "The argument `param_names` is required for this input type."
            raise ValueError(msg)
        return tidy_scipy_result(result, **kwargs)
    else:
        msg = 'Sorry, `tidy` does not support this fit result object (%s)'
        raise NotImplementedError(msg % type(result))


def glance(result, var_name='item', **kwargs):
    """Tidy DataFrame containing fit summaries from`result`.

    A function to tidy any of the supported fit result
    (or a list of fit results). This function will identify input type
    and call the relative "specialized" tidying function. When the input
    is a list, the returned DataFrame contains data from all the fit
    results.
    Supported fit result objects are `lmfit.ModelResult`,
    `lmfit.MinimizeResult` and `scipy.optimize.OptimizeResult`.

    Arguments:
        result (fit result object or list): one of the supported fit result
            objects or a list of supported fit result objects. When a list,
            all the elements need to be of the same type.
        var_name (string): name of the column containing an integer index
            that is different for each element in the list of fit results.
        **kwargs: additional arguments passed to the underlying specialized
            tidying function.

    Returns:
        A DataFrame with one row for each passed fit result.
        Columns include fit summaries such as reduced chi-square,
        number of evaluation, successful convergence, AIC, BIC, etc.
        When a list of fit-result objects is passed, the column `var_name`
        (`'item'` by default) contains the index of the object
        in the list.

    See also:
        For more information on the returned DataFrame and on additional
        arguments refer to the specialized tidying functions:
        :func:`glance_lmfit_result` and :func:`glance_scipy_result`.
    """
    if isinstance(result, list):
        return _multi_dataframe(result, glance, var_name=var_name, **kwargs)
    elif (isinstance(result, lmfit.model.ModelResult) or
          isinstance(result, lmfit.minimizer.MinimizerResult)):
        return glance_lmfit_result(result)
    elif isinstance(result, so.OptimizeResult):
        return glance_scipy_result(result, **kwargs)
    else:
        msg = 'Sorry, `glance` does not support this fit result object (%s)'
        raise NotImplementedError(msg % type(result))


def augment(result, var_name='item', **kwargs):
    """Tidy DataFrame containing fit data from `result`.

    A function to tidy any of the supported fit result
    (or a list of fit results). This function will identify input type
    and call the relative "specialized" tidying function. When the input
    is a list, the returned DataFrame contains data from all the fit
    results.

    Arguments:
        result (fit result object or list): one of the supported fit result
            objects or a list of supported fit result objects. When a list,
            all the elements need to be of the same type.
        var_name (string): name of the column containing an integer index
            that is different for each element in the list of fit results.
        **kwargs: additional arguments passed to the underlying specialized
            tidying function.

    Returns:
        A DataFrame with one row for each data point used in the fit.
        It contains the input data, the model evaluated at the data points
        with best fitted parameters, error ranges, etc.
        When a list of fit-result objects is passed, the column `var_name`
        (`'item'` by default) contains the index of the object
        in the list.
    """
    if isinstance(result, list):
        return _multi_dataframe(result, augment, var_name=var_name, **kwargs)
    elif isinstance(result, lmfit.model.ModelResult):
        return _augment_lmfit_modelresult(result)
    else:
        msg = 'Sorry, `augment` does not support this fit result object (%s)'
        raise NotImplementedError(msg % type(result))


def _multi_dataframe(results, func, var_name='item', **kwargs):
    """Call `func` for each element in `results` and concatenate results.
    """
    d = []
    for i, res in enumerate(results):
        d.append(func(res, **kwargs))
        d[-1][var_name] = i
    return pd.concat(d, ignore_index=True)


def tidy_lmfit_result(result):
    """Tidy parameters from lmfit's  `ModelResult` or `MinimizerResult`.

    Normally this function is not called directly but invoked by the
    general purpose function :func:`tidy`.

    Arguments:
        result (`ModelResult` or `MinimizerResult`): the fit result object.

    Returns:
        A DataFrame in tidy format with one row for each parameter.

    Note:
        The (possible) columns of the returned DataFrame are:

        - `name` (string): name of the parameter.
        - `value` (number): value of the parameter after the optimization.
        - `init_value` (number): initial value of the parameter before the
          optimization.
        - `min`, `max` (numbers): bounds of the parameter
        - `vary` (bool): whether the parameter has been varied during the
          optimization.
        - `expr` (string): constraint expression for the parameter.
        - `stderr` (float): standard error for the parameter.
    """
    params_attrs = ['name', 'value', 'min', 'max', 'vary', 'expr', 'stderr']
    columns = params_attrs + ['init_value']
    d = pd.DataFrame(index=range(result.nvarys), columns=columns)
    for i, (name, param) in enumerate(sorted(result.params.items())):
        for p in params_attrs:
            d.loc[i, p] = getattr(param, p)
        # Derived parameters may not have init value
        if name in result.init_values:
            d.loc[i, 'init_value'] = result.init_values[name]
    return d


def tidy_scipy_result(result, param_names, **kwargs):
    """Tidy parameters data from scipy's `OptimizeResult`.

    Normally this function is not called directly but invoked by the
    general purpose function :func:`tidy`.
    Since `OptimizeResult` has a raw array of fitted parameters
    but no names, the parameters' names need to be passed in `param_names`.

    Arguments:
        result (`OptimizeResult`): the fit result object.
        param_names (string or list of string): names of the fitted parameters.
            It can either be a list of strings or a single string with
            space-separated names.

    Returns:
        A DataFrame in tidy format with one row for each parameter.

    Note:
        The columns of the returned DataFrame are:

        - `name` (string): name of the parameter.
        - `value` (number): value of the parameter after the optimization.
        - `grad` (float): gradient for each parameter
        - `active_mask` (int)
    """
    Params = namedtuple('Params', param_names)
    params = Params(*result.x)
    df = dict_to_tidy(params._asdict(), **kwargs)
    for var in ('grad', 'active_mask'):
        df[var] = result[var]
    return df


def glance_scipy_result(result):
    """Tidy summary statistics from scipy's `OptimizeResult`.

    Normally this function is not called directly but invoked by the
    general purpose function :func:`glance`.

    Arguments:
        result (`OptimizeResult`): the fit result object.

    Returns:
        A DataFrame in tidy format with one row and several summary statistics
        as columns.

    Note:
        The columns of the returned DataFrame are:

        - `success` (bool): model name (only for `ModelResult`)
        - `cost` (float): method used for the optimization (e.g. `leastsq`).
        - `nfev` (int): number of objective function evaluations
        - `njev` (int): number of jacobian function evaluations
        - `status` (int): status returned by the fit routine
        - `message` (string): message returned by the fit routine
    """
    attr_names_all = ['success', 'cost', 'nfev', 'njev', 'status', 'message']
    attr_names = [a for a in attr_names_all if hasattr(result, a)]
    d = pd.DataFrame(index=range(1), columns=attr_names)
    for attr_name in attr_names:
        d.loc[0, attr_name] = getattr(result, attr_name)
    return d


def glance_lmfit_result(result):
    """Tidy summary statistics from lmfit's `ModelResult` or `MinimizerResult`.

    Normally this function is not called directly but invoked by the
    general purpose function :func:`glance`.

    Arguments:
        result (`ModelResult` or `MinimizerResult`): the fit result object.

    Returns:
        A DataFrame in tidy format with one row and several summary statistics
        as columns.

    Note:
        The columns of the returned DataFrame are:

        - `model` (string): model name (only for `ModelResult`)
        - `method` (string): method used for the optimization (e.g. `leastsq`).
        - `num_params` (int): number of varied parameters
        - `ndata` (int):
        - `chisqr` (float): chi-square statistics.
        - `redchi` (float): reduced chi-square statistics.
        - `AIC` (float): Akaike Information Criterion statistics.
        - `BIC` (float): Bayes Information Criterion statistics.
        - `num_func_eval` (int): number of evaluations of the objective
          function during the fit.
        - `num_data_points` (int): number of data points (e.g. samples) used
          for the fit.

    """
    def _is_modelresult(res):
        return hasattr(res, 'model')
    result_attrs = ['name', 'method', 'nvarys', 'ndata', 'chisqr', 'redchi',
                    'aic', 'bic', 'nfev', 'success', 'message']
    attrs_map = OrderedDict((n, n) for n in result_attrs)
    attrs_map['name'] = 'model'
    attrs_map['aic'] = 'AIC'
    attrs_map['bic'] = 'BIC'
    attrs_map['nvarys'] = 'num_params'
    attrs_map['nfev'] = 'num_func_eval'
    attrs_map['ndata'] = 'num_data_points'
    # ModelResult has attribute `.model.name`, MinimizerResult does not
    if not _is_modelresult(result):
        attrs_map.pop('name')
    d = pd.DataFrame(index=range(1), columns=attrs_map.values())
    if _is_modelresult(result):
        d.loc[0, attrs_map.pop('name')] = result.model.name
    for attr_name, df_name in attrs_map.items():
        d.loc[0, df_name] = getattr(result, attr_name)
    #d.loc[0, 'num_components'] = len(result.components)
    if hasattr(result, 'kws') and result.kws is not None:
        for key, value in result.kws.items():
            d['_'.join((result.method, key))] = value
    return d


def _augment_lmfit_modelresult(result):
    """Tidy data values and fitted model from `lmfit.model.ModelResult`.
    """
    columns = ['x', 'data', 'best_fit', 'residual']
    d = pd.DataFrame(index=range(result.ndata), columns=columns)
    for col in columns[1:]:
        d.loc[:, col] = getattr(result, col)

    independent_vars = result.model.independent_vars
    if len(independent_vars) == 1:
        independent_var = independent_vars[0]
    else:
        msg = ('Only 1 independent variable is currently supported.\n'
               'Found independent variables: %s' % str(independent_vars))
        raise NotImplementedError(msg)

    x_array = result.userkws[independent_var]
    d.loc[:, 'x'] = x_array

    if len(result.components) > 1:
        comp_names = [c.name for c in result.components]
        for cname, comp in zip(comp_names, result.components):
            d.loc[:, cname] = comp.eval(x=d.x, **result.values)
    return d


def tidy_to_dict(df, key='name', value='value', keys_exclude=None,
                 cast_value=float):
    """Convert a tidy DataFrame into a dictionary.

    This function converts two columns from an input tidy (or long-form)
    DataFrame into a dictionary. A typical use-case is passing
    parameters stored in tidy DataFrame to a python function. The arguments
    `key` and `value` contain the name of the DataFrame columns containing
    the keys and the values of the dictionary.

    Arguments:
        df (pandas.DataFrame): the "tidy" DataFrame containing the data.
            Two columns of this DataFrame should contain the keys and the
            values to construct the dictionary.
        key (string or scalar): name of the DataFrame column containing
            the keys of the dictionary.
        value (string or scalar ): name of the DataFrame column containing
            the values of the dictionary.
        keys_exclude (iterable or None): list of keys excluded when building
            the returned dictionary.
        cast_value (callable or None): callable used to cast
            the value of each item in the dictionary. If None, no casting
            is performed and the resulting values are 1-element
            `pandas.Series`. Default is the python built-in `float`.
            Other typical values may be `int` or `str`.

    Returns:
        A dictionary with keys and values extracted from the input (tidy)
        DataFrame.

    See also: :func:`dict_to_tidy`.
    """
    keys_list = set(df[key])
    if keys_exclude is not None:
        keys_list = keys_list - set(keys_exclude)
    if cast_value is None:
        cast_value = lambda x: x
    return {var: cast_value(df.loc[df[key] == var, value])
            for var in keys_list}


def dict_to_tidy(dc, key='name', value='value', keys_exclude=None,
                 value_type=None):
    """Convert a dictionary into a tidy DataFrame.

    This function converts a dictionary into a "tidy" (or long-form)
    DataFrame with two columns: one containing the keys and the other
    containing the values from the dictionary. Names of the columns
    can be specified with the `key` and `value` argument.

    Arguments:
        dc (dict): the input dictionary used to build the DataFrame.
        key (string or scalar): name of the DataFrame column containing
            the keys of the dictionary.
        value (string or scalar): name of the DataFrame column containing
            the values of the dictionary.
        keys_exclude (iterable or None): list of keys excluded when building
            the returned DataFrame.

    Returns:
        A two-columns tidy DataFrame containing the data in the dictionary.


    See also: :func:`tidy_to_dict`.
    """
    keys = dc.keys()
    if keys_exclude is not None:
        keys -= keys_exclude
    keys = sorted(keys)
    df = pd.DataFrame(columns=(key, value), index=range(len(keys)))
    df[key] = keys
    df[value] = [dc[k] for k in keys]
    return df


def _test_dict_to_tidy(dc, key='name', value='value', keys_exclude=None,
                       value_type=None):
    # Alternative implementation
    if keys_exclude is None:
        keys_exclude = []
    dc2 = {k: v for k, v in dc.items() if k not in keys_exclude}
    df = pd.DataFrame(columns=(key, value), index=range(len(dc2)))
    keys = sorted(dc2.keys())
    df[key] = keys
    df[value] = [dc2[k] for k in keys]
    # Test compliance
    assert all(df == dict_to_tidy(dc, key, value, keys_exclude, value_type))
    return df
