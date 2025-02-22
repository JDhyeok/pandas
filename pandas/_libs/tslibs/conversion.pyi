from datetime import (
    datetime,
    tzinfo,
)

import numpy as np

from pandas._typing import npt

DT64NS_DTYPE: np.dtype
TD64NS_DTYPE: np.dtype

class OutOfBoundsTimedelta(ValueError): ...

def precision_from_unit(
    unit: str,
) -> tuple[int, int]: ...  # (int64_t, _)
def ensure_datetime64ns(
    arr: np.ndarray,  # np.ndarray[datetime64[ANY]]
    copy: bool = ...,
) -> np.ndarray: ...  # np.ndarray[datetime64ns]
def ensure_timedelta64ns(
    arr: np.ndarray,  # np.ndarray[timedelta64[ANY]]
    copy: bool = ...,
) -> np.ndarray: ...  # np.ndarray[timedelta64ns]
def localize_pydatetime(dt: datetime, tz: tzinfo | None) -> datetime: ...
