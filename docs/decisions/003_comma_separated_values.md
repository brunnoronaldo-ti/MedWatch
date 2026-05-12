# decision 3:  Comma Separated Values (CSV)

## Overview

**CSV**, which stands for **Comma-Separated Values**, is a simple text file format used to store tabular data, such as spreadsheets or databases. It allows you to save structured data (numbers and text) in a readable format, where each line of the file represents a row in the table and each column is separated by a delimiter, usually a comma **(,)** or semicolon **(;)**.

## how work?

1. **Simple Structure**: The file is just plain text **(.csv)**. The first line usually contains the column headers, and subsequent lines contain the data.
2. **Delimiters**: Although the name suggests commas, many files use **;** or **\t (tab)** to separate values, especially in regions where the comma is used as a decimal separator.
3. **Quotation marks**: If data contains a delimiter character (e.g., a comma within an address), that data is enclosed in quotation marks (e.g., "Street A, 100") to indicate that it is not a column separator.

### exemple of **.csv**

```csv
id,name,age
1,Ana,28
2,Bruno,35
3,Carlos,22
```

