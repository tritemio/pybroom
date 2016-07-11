import pandas as pd
import lmfit


def tidy(result):
    """Tidy DataFrame containing fitted parameter data from `result`.

    Returns:
        A DataFrame with one row for each fitted paramater.
        Columns include parameter properties such as best-fit value,
        standard error, eventual bounds/constrains, etc.
    """
    # Find out what result is and call the relevant function
    if isinstance(result, lmfit.model.ModelResult):
        return _tidy_lmfit_modelresult(result)
    else:
        raise NotImplemented('Sorry, the data is not recognized.')


def glance(result):
    """Tidy DataFrame containing fit summaries from`result`.

    Returns:
        A DataFrame with only one row and several columns.
        Columns include fit summaries such as reduced chi-square,
        number of evaluation, successful convergence, AIC, BIC, etc.
    """
    if isinstance(result, lmfit.model.ModelResult):
        return _glance_lmfit_modelresult(result)
    else:
        raise NotImplemented('Sorry, the data is not recognized.')


def augment(result):
    """Tidy DataFrame containing fit data from `result`.

    Returns:
        A DataFrame with one row for each data point used in the fit.
        It contains the input data, the model evaluated at the data points
        with best fitted parameters, error ranges, etc.
    """
    if isinstance(result, lmfit.model.ModelResult):
        return _augment_lmfit_modelresult(result)
    else:
        raise NotImplemented('Sorry, the data is not recognized.')


def _tidy_lmfit_modelresult(result):
    """Make a "tidy" view of `lmfit.model.ModelResult`.
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


def _glance_lmfit_modelresult(result):
    """Make a "glance" view of `lmfit.model.ModelResult`.
    """
    result_attrs = ['method', 'nvarys', 'ndata', 'chisqr', 'redchi',
                    'aic', 'bic', 'nfev', 'success', 'message']
    attrs_map = {n: n for n in result_attrs}
    attrs_map['aic'] = 'AIC'
    attrs_map['bic'] = 'BIC'
    attrs_map['nvarys'] = 'num_params'
    attrs_map['nfev'] = 'num_func_eval'
    attrs_map['ndata'] = 'num_data_points'

    columns = ['name'] + [attrs_map[n] for n in result_attrs]
    d = pd.DataFrame(index=range(1), columns=columns)
    for name in result_attrs:
        d.loc[0, attrs_map[name]] = getattr(result, name)

    d.loc[0, 'name'] = result.model.name
    #d.loc[0, 'num_components'] = len(result.components)
    return d


def _augment_lmfit_modelresult(result):
    """Make a "glance" view of `lmfit.model.ModelResult`.
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
        raise NotImplemented(msg)

    x_array = result.userkws[independent_var]
    d.loc[:, 'x'] = x_array

    if len(result.components) > 1:
        comp_names = [c.name for c in result.components]
        for cname, comp in zip(comp_names, result.components):
            d.loc[:, cname] = comp.eval(x=d.x, **result.values)
    return d
