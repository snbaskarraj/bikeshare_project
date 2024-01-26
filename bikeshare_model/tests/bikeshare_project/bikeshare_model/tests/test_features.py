# bikeshare_model/tests/test_features.py
# bikeshare_model/tests/test_features.py
import pandas as pd
from ..features import WeekdayImputer, WeathersitImputer, Mapper, OutlierHandler, WeekdayOneHotEncoder

def test_weekday_imputer():
    # Setup
    data = {'dteday': ['2020-01-01', '2020-01-02'], 'weekday': [None, 'Mon']}
    df = pd.DataFrame(data)
    
    # Execute
    imputer = WeekdayImputer(variable='weekday', date_var='dteday')
    transformed_df = imputer.transform(df)
    
    # Assert
    assert transformed_df['weekday'].isnull().sum() == 0
    assert transformed_df.loc[0, 'weekday'] == 'Wed'  # 2020-01-01 is a Wednesday

def test_weathersit_imputer():
    # Setup
    data = {'weathersit': ['Clear', None, 'Rain']}
    df = pd.DataFrame(data)
    
    # Execute
    imputer = WeathersitImputer(variable='weathersit')
    transformed_df = imputer.transform(df)
    
    # Assert
    assert transformed_df['weathersit'].isnull().sum() == 0
    assert transformed_df['weathersit'].mode()[0] == transformed_df.loc[1, 'weathersit']  # Replace None with mode

def test_mapper():
    # Setup
    data = {'season': ['spring', 'summer', 'fall', 'winter']}
    df = pd.DataFrame(data)
    mappings = {'spring': 1, 'summer': 2, 'fall': 3, 'winter': 4}
    
    # Execute
    mapper = Mapper(variable='season', mappings=mappings)
    transformed_df = mapper.transform(df)
    
    # Assert
    assert all(transformed_df['season'] == [1, 2, 3, 4])

def test_outlier_handler():
    # Setup
    data = {'temp': [10, 20, 30, 1000, -100]}
    df = pd.DataFrame(data)
    
    # Execute
    handler = OutlierHandler(variable='temp')
    transformed_df = handler.transform(df)
    
    # Assert
    assert transformed_df['temp'].max() <= handler.upper_bound
    assert transformed_df['temp'].min() >= handler.lower_bound

def test_weekday_onehot_encoder():
    # Setup
    data = {'weekday': ['Mon', 'Tue', 'Wed']}
    df = pd.DataFrame(data)
    
    # Execute
    encoder = WeekdayOneHotEncoder(variable='weekday')
    transformed_df = encoder.transform(df)
    
    # Assert
    assert transformed_df.shape[1] > df.shape[1]  # Check if new columns are added
    assert all(col.startswith('weekday_') for col in transformed_df.columns)  # Check if new columns have the correct prefix

# Add more tests as needed for your specific project requirements and features.

