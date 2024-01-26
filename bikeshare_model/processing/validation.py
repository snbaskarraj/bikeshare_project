import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from typing import List, Optional, Tuple, Union

from datetime import datetime
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from bikeshare_model.config.core import config
from bikeshare_model.processing.data_manager import pre_pipeline_preparation

def validate_inputs(*, input_df: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    pre_processed = pre_pipeline_preparation(data_frame=input_df)
    validated_data = pre_processed[config.model_config.features].copy()
    errors = None

    try:
        # Handle invalid date format for dteday gracefully
        validated_data['dteday'] = validated_data['dteday'].apply(handle_date_input)
        
        # replace numpy nans so that pydantic can validate
        MultipleDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors

def handle_date_input(date_str: Union[str, datetime]) -> Optional[Union[str, datetime]]:
    try:
        if isinstance(date_str, str):
            return datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        return None

class DataInputSchema(BaseModel):
    dteday: Optional[Union[str, datetime]]
    season: Optional[str]
    hr: Optional[str]
    holiday: Optional[str]
    weekday: Optional[str]
    workingday: Optional[str]
    weathersit: Optional[str]
    temp: Optional[float]
    atemp: Optional[float]
    hum: Optional[float]
    windspeed: Optional[float]
    yr: Optional[int]
    mnth: Optional[str]

class MultipleDataInputs(BaseModel):
    inputs: List[DataInputSchema]
