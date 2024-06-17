# US County Population Estimates Cleanup and Consolidation

This JupyterLab Notebook is designed to consolidate yearly US county population estimate data from 1980 to 2023 into a single, normalized file. The script handles US Census data scattered across multiple files and formats, transforming and merging them into a unified format with three columns: FIPS, Year, and POP (population estimate).

## Purpose

The primary purpose of this notebook is to:

1. **Load Population Data**: Import population estimate data from various files and formats covering different periods.
2. **Normalize Data**: Standardize the data structure across different years and formats.
3. **Consolidate Data**: Merge the normalized data into a single DataFrame with consistent columns.
4. **Export Consolidated Data**: Save the final consolidated DataFrame to an Excel file for easy analysis and use.

## Data Sources

1. **2000-09, 2010-19, 2020-23**:
   - Files: `co_2000-09.csv`, `co_2010-19.csv`, `co_2020-23.csv` (renamed copies of original source files)
   - Structure: Each period's data is contained within a single CSV file.
   - Source URLs:
     - [2000-09](https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-2000-2010-counties.html) https://www2.census.gov/programs-surveys/popest/datasets/2000-2010/intercensal/county/co-est00int-tot.csv
     - [2010-19](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html) https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv
     - [2020-23](https://www.census.gov/data/datasets/time-series/demo/popest/2020s-counties-total.html) https://www2.census.gov/programs-surveys/popest/datasets/2020-2023/counties/totals/co-est2023-alldata.csv

2. **1980-89**:
   - File: `co-1980-89_tabs.xls` (renamed copy of original source file)
   - Structure: Each year's data is contained in a separate tab within a single Excel file.
   - Source URL: [1980-89](https://www.census.gov/data/datasets/time-series/demo/popest/1980s-county.html) https://www2.census.gov/programs-surveys/popest/datasets/1980-1990/counties/asrh/pe-02.xls

3. **1990-99**:
   - Files: `stch-icen19YY.txt` (one file per year)
   - Structure: Fixed column widths within plain text files.
   - Source URL: [1990-99](https://www.census.gov/data/datasets/time-series/demo/popest/intercensal-1990-2000-state-and-county-characteristics.html)

## Script Structure

### Description

The notebook is structured to guide the user through the following steps:

1. **Introduction and Setup**: Importing necessary libraries and setting up the environment.
2. **Data Loading**: Loading population estimates data from multiple source files for each period.
3. **Data Cleaning and Normalization**: Standardizing the format of each data file, including renaming columns, handling missing values, and converting data types.
4. **Data Consolidation**: Merging all the cleaned data into a single DataFrame with columns FIPS, Year, and POP.
5. **Exporting Data**: Saving the consolidated DataFrame to an Excel file.

### Code Summary

- **Imports required libraries**: The notebook begins by importing libraries such as `pandas` and `openpyxl`.
- **Loads data from multiple sources**: Data is loaded from various CSV, Excel, and text files.
- **Performs data cleaning and normalization**: Includes operations like renaming columns, handling missing values, and converting data types to ensure consistency.
- **Handles different file formats**:
  - CSV files: Loaded directly and processed uniformly using a custom function.
  - Excel file (1980-89): Each sheet is processed and concatenated into a single DataFrame.
  - Fixed-width text files (1990-99): Custom processing for fixed column widths.
- **Consolidates data into a single DataFrame**: Uses techniques like concatenation and `groupby` to merge data.
- **Exports the consolidated DataFrame**: Saves the final DataFrame to an Excel file for future use.

## How to Use

1. **Prerequisites**: Ensure you have Python and JupyterLab Notebook installed, along with the required libraries (`pandas`, `openpyxl`).
2. **Running the Notebook**: Open the notebook in JupyterLab and execute the cells in order to reproduce the analysis.
3. **Modifying the Analysis**: Feel free to modify the code and analysis to suit your own needs or to explore different aspects of the data.
