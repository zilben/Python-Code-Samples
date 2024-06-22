
# Data Comparison Script

## Overview

This script contains a function `compare_data(df1, df2, join1, join2, join_how, path)` that compares two pandas DataFrames cell by cell and outputs a CSV file for each column that has differences (deltas). This is particularly useful for identifying discrepancies between two datasets.

## Functionality

### Function: `compare_data`

- **Purpose**: Compares two DataFrames cell by cell and returns a CSV file for each column that has deltas, listing the deltas.
- **Requirements**:
  - The datasets must have the same number of columns.
  - The columns must be in the same order.
  - The column names do not need to match.

### Parameters

- `df1`: The first DataFrame to compare.
- `df2`: The second DataFrame to compare.
- `join1`: List of columns to join on in the first DataFrame.
- `join2`: List of columns to join on in the second DataFrame.
- `join_how`: The method of joining (options: 'left', 'right', 'inner', 'outer').
- `path`: The file path where the resulting CSV files should be saved.

### Sample Data

The sample data used for this script comes from the USAC Open Data portal, specifically the dataset [E-Rate Request for Discount on Services Basic Information](https://opendata.usac.org/E-Rate/E-Rate-Request-for-Discount-on-Services-Basic-Info/9s6i-myen/about_data), filtering for DC entities.

## How to Use

1. **Install Requirements**: Ensure you have pandas and numpy installed. You can install these using pip:

    ```sh
    pip install pandas numpy
    ```

2. **Prepare Your DataFrames**: Load your data into two pandas DataFrames. Make sure the columns are in the same order.

3. **Call the Function**: Use the `compare_data` function with the appropriate parameters. Example:

    ```python
    import pandas as pd
    from P2_Data_Compare import compare_data

    # Load your data into DataFrames
    df1 = pd.read_csv('path/to/first/dataset.csv')
    df2 = pd.read_csv('path/to/second/dataset.csv')

    # Define joining columns
    join1 = ['column_name1']
    join2 = ['column_name1']

    # Define joining method
    join_how = 'inner'

    # Define the path to save CSV files
    path = 'path/to/save/csv_files'

    # Call the compare_data function
    compare_data(df1, df2, join1, join2, join_how, path)
    ```

4. **Check Results**: The CSV files with deltas will be saved in the specified path. Each CSV file will contain the discrepancies found for a specific column.

## Example

Here is an example of how to use the script with sample data from the USAC Open Data portal:

```python
import pandas as pd
from P2_Data_Compare import compare_data

# Sample DataFrames (replace with your actual data)
df1 = pd.read_csv('sample_data_1.csv')
df2 = pd.read_csv('sample_data_2.csv')

# Define joining columns
join1 = ['Entity Number']
join2 = ['Entity Number']

# Define joining method
join_how = 'inner'

# Define the path to save CSV files
path = 'output/deltas'

# Call the compare_data function
compare_data(df1, df2, join1, join2, join_how, path)
```

## Acknowledgements

- [USAC Open Data Portal](https://opendata.usac.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
