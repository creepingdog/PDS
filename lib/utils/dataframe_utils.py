
import pandas as pd
import numpy as np
import lib.utils.logger as LOG
logger = LOG.get_logger(__name__)


def value_counts_by_columns(df, cols):
    if not isinstance(df, pd.DataFrame):
        logger.error('The first argument to this function should be of type pd.DataFrame')
        return None
    #
    if isinstance(cols, str):
        cols = (cols,)
    elif isinstance(cols, pd.Series) or \
            isinstance(cols, list) or \
            isinstance(cols, tuple):
        cols = tuple(cols)
    else:
        logger.error('The second argument to this function should be of type [string|pd.Series|list|tuple]')
        return None
    #

    if not cols:
        logger.error('Pleaes provide at lease one column name to "cols"')
        return None
    #
    ret = df.apply(pd.value_counts).T.stack()
    ret = ret.astype(np.int64)
    ret = pd.DataFrame(ret, columns=['Count',])
    return ret
#