import logging

import pandas as pd

from utils import fetch_and_convert_data, count_unique_values, validate_dataframe

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        # Specify the API URL
        api_url = "https://services1.arcgis.com/UWYHeuuJISiGmgXx/arcgis/rest/services/PublicArtInventory/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

        # Fetch and convert data
        logger.info("Fetching and converting data from API...")
        api_data = fetch_and_convert_data(api_url)

        # Convert to a data frame
        logger.info("Converting data to a DataFrame...")
        api_df = pd.json_normalize(api_data['features'])

        # Validate data using the Pandera schema
        logger.info("Validating DataFrame using Pandera schema...")
        is_valid = validate_dataframe(api_df)

        if is_valid:
            logger.info("DataFrame is valid.")
        else:
            logger.warning("DataFrame is invalid.")

        # Process data
        logger.info("Counting unique values in the DataFrame...")
        result = count_unique_values(api_df, "properties.zipcodes")

        # Print Number of Public Artworks by Zipcode
        print(result)

    except Exception as e:
        logger.exception(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
