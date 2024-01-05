# utils.py
import pandera as pa
import requests

# Define the schema for the DataFrame
SCHEMA = pa.DataFrameSchema({
    'type': pa.Column(pa.String, nullable=False),
    'properties.zipcodes': pa.Column(pa.String, nullable=False, regex=r'^\d{5}$'),
})


def validate_dataframe(df):
    """
    Validates a DataFrame against the defined Pandera schema.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.

    Returns:
    - bool: True if the DataFrame is valid, False otherwise.
    """
    try:
        # Validate the DataFrame against the schema
        SCHEMA.validate(df)
        return True
    except pa.errors.SchemaError:
        return False


def fetch_and_convert_data(api_url):
    """
    Fetches data from the specified API URL and converts it to a Python dictionary.

    Parameters:
    - api_url (str): The URL of the API endpoint to fetch data from.

    Returns:
    - dict: A Python dictionary representing the JSON data retrieved from the API.

    Raises:
    - requests.exceptions.RequestException: If an error occurs while making the HTTP request.
    """
    try:
        # Make an HTTP GET request to the API URL
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses

        # Convert the JSON data to a Python dictionary
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the HTTP request
        raise e


def count_unique_values(df, col):
    """
    Takes a DataFrame and a column, and returns a DataFrame with unique values
    of the specified column along with their counts.

    Parameters:
    - df: pandas DataFrame
    - col: str, the column for which unique values and counts are calculated

    Returns:
    - pandas DataFrame with the column name and 'Counts'
    """
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in the DataFrame.")

    result_df = df.groupby(col).size().reset_index(name='Counts')

    return result_df
