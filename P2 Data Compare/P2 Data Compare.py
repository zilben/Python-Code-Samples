
#Import used packages
import pandas as pd
import numpy as np
import re

def compare_data(df1,df2,join1,join2,join_how,path):
    
    # Ensure dfs have same number of columns
    if len(list(df1.columns.values)) != len(list(df2.columns.values)):
        return 'Dataframes do not have the same number of columns. Operation stopped.'
        
    # Ensure consistent data types
    df1 = df1.astype(str)
    df2 = df2.astype(str)

    # Handle NaN values
    df1 = df1.fillna('')
    df2 = df2.fillna('')

    # Create joining column with concatenated values
    join1_on = join1 
    join2_on = join2
    join_1 = df1[join1_on].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    join_2 = df2[join2_on].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)    
    df1.insert(loc=0, column='join1', value=join_1)
    df2.insert(loc=0, column='join2', value=join_2)
    
    # Merges df1 and df2 on the first column of each DataFrame using the specified join method (join_how).
    # The suffix '_2_' is added to columns from df2 to avoid column name conflicts.
    # Replaces all NaN values and the string 'nan' with empty strings in the resulting DataFrame.
    comb_df = df1.merge(df2, how=join_how, left_on=df1.columns[0], right_on=df2.columns[0], suffixes=(None, '_2_')) \
            .replace(np.nan, '', regex=True).replace('nan', '')
    
    # Creates a list of column positions (indices) for the combined DataFrame.
    position = list(range(0, len(comb_df.columns)))
    
    # Creates a dictionary mapping each column position to its corresponding column name.
    col_dict = pd.Series(comb_df.columns, index=position).to_dict()
    
    # Creates a dictionary mapping the first half of the column positions to the second half.
    # This is used to compare corresponding columns from df1 and df2 in the combined DataFrame.
    comp_dict = pd.Series(position[int(len(col_dict) / 2):], index=position[:int(len(col_dict) / 2)]).to_dict()
    
    # Initializes an empty DataFrame to store mismatch information.
    m_df = pd.DataFrame() 
    
    # Iterates over the range from 0 to half the length of col_dict.
    # This loop processes each pair of columns from df1 and df2.
    for i in range(0, int(len(col_dict) / 2)):
        # Counts the number of mismatches between the ith column from df1 and the corresponding column from df2.
        m_count = comb_df.iloc[:, i].ne(comb_df.iloc[:, comp_dict[i]]).sum()
        
        # Creates a boolean Series indicating which rows have mismatches between the ith column from df1 and df2.
        index = comb_df.iloc[:, i].ne(comb_df.iloc[:, comp_dict[i]])
        
        # Gets the rows where mismatches occurred in the first column of the combined DataFrame.
        m_rows = comb_df.loc[index, col_dict[0]]
        
        # Creates a DataFrame with the mismatch information for the current column pair.
        # 'Field' indicates the name of the field (column) being compared.
        # 'Mismatches' indicates the count of mismatches.
        # 'Rows' is a string of indices where mismatches occurred, separated by commas.
        row = pd.DataFrame({
            'Field': col_dict[i], 
            'Mismatches': m_count, 
            'Rows': str(','.join(list(m_rows)))
        }, index=[0])
        
        # Concatenates the current row of mismatch information to m_df.
        # ignore_index=True ensures that the index is ignored and a new one is created.
        m_df = pd.concat([m_df, row], ignore_index=True)
    
    # Iterates over the range from 0 to half the length of col_dict.
    # This loop processes each pair of columns from df1 and df2 to handle specific mismatches.
    files = 0
    for i in range(0, int(len(col_dict) / 2)):
        # Extracts the list of row indices (as strings) where mismatches occurred for the current column.
        items_list = (m_df.loc[m_df['Field'] == col_dict[i], 'Rows']).values[0].split(",")
        
        # Defines the column names for the pair of columns being compared.
        col_a = col_dict[i] 
        col_b = col_dict[comp_dict[i]]
        
        # Creates a DataFrame containing only the rows with mismatches for the current column pair.
        # It includes the first column (assumed to be an identifier) and the current pair of columns being compared.
        col_comp_df = comb_df.loc[comb_df[df1.columns[0]].isin(items_list), [df1.columns[0], col_a, col_b]]
        
        # Adds a new column 'Changed' to indicate whether the values have changed between the two columns.
        col_comp_df['Changed'] = None
        
        ##
        # Renames the columns of the DataFrame for clarity.
        col_comp_df.columns = ['_ID', col_a, col_b, 'Changed']
        
        # Updates the 'Changed' column to True where there are differences between the compared columns.
        col_comp_df['Changed'] = col_comp_df[col_a].ne(col_comp_df[col_b])
        
        # If there are any changes (i.e., the sum of 'Changed' is greater than 0), save the DataFrame to a CSV file.
        delta_count = col_comp_df['Changed'].sum() 
        if delta_count > 0:	
            files += 1
            # Creates a file name indicating the columns being compared, replacing problematic characters.
            filename = re.sub('([/\\?])+',' ', f'{i}_{col_a} and {col_b} Changed.csv')
            
            # Saves the rows where changes occurred to a CSV file in the specified path.
            col_comp_df.loc[(col_comp_df['Changed'] == True)].to_csv(path+'//'+filename, index=False)
            print(f'File {filename} with {delta_count} mismatches saved.')
    
    if files == 0:
        return 'Comparison complete. No mismatches.'
    
    return f'Comparison complete. Files with mismatches saved in {path}.'

#Set input file path
SourcePathName = r'C:\Users\zilbe\OneDrive\Desktop\Python-Code-Samples\Python-Code-Samples\P2 Data Compare'

#read data
FileName = 'DC current E-Rate F471.csv'
file_1 = pd.read_csv(SourcePathName+'//'+FileName, dtype=object)
len(file_1)

FileName = 'DC original E-Rate F471.csv'
file_2 = pd.read_csv(SourcePathName+'//'+FileName, dtype=object)
len(file_2) 

############################
print( len(list(file_1.columns.values)) == len(list(file_2.columns.values)) )
    
############################

join1 = ['Application Number','Billed Entity Number']
join2 = ['Application Number','Billed Entity Number']
join_how = 'inner'
compare_data(file_1,file_2,join1,join2,join_how,SourcePathName)

