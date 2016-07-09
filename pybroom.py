import pandas as pd
import lmfit


def augment():
    """Tidy DataFrame containing fit data from `result`.

    Returns:
        A DataFrame with one row for each data point used in the fit.
        It contains the input data, the model evaluated at the data points
        with best fitted parameters, error ranges, etc.
    """
    raise NotImplemented()


def glance(result):
    """Tidy DataFrame containing fit summaries from`result`.

    Returns:
        A DataFrame with only one row and several columns.
        Columns include fit summaries such as reduced chi-square,
        number of evaluation, successful convergence, AIC, BIC, etc.
    """
    raise NotImplemented()


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


def _tidy_lmfit_modelresult(result):
    """Return a tidy DataFrame containing from a `lmfit.model.ModelResult`.
    """
    params_attrs = ['name', 'value', 'min', 'max', 'vary', 'expr', 'stderr']
    columns = params_attrs + ['init_value']
    d = pd.DataFrame(index=range(result.nvarys), columns=columns)
    for i, (name, param) in enumerate(sorted(result.params.items())):
        for p in params_attrs:
            d.loc[i, p] = getattr(param, p)
        d.loc[i, 'init_value'] = result.init_values[name]
    return d
