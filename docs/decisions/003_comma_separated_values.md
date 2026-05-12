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

---

## Advantages of using CSV in Python project

Using CSV in Python is extremely common and advantageous, mainly due to its ease of manipulation and compatibility.

- **Native Library (csv)**: Python comes with a built-in module called **csv** that allows you to read and write files without needing to install anything extra.

- **Integration with Pandas**: For data analysis projects, the **Pandas** library allows loading huge **CSV** files with just one line of code `(pd.read_csv())`.

- **Lightweight and High-Performance**: **CSV** files are simple text files, taking up less space and being faster to read/write than complex formats like `.xlsx`.

- **Interoperability**: Facilitates data transfer between Python script and other tools (e.g., exporting reports to Excel or importing data from an SQL database).

---

## How to manipulate CSV in Python

> The information below is for informational purposes and for future reference. If the reader wishes to read it, please feel free.

1. Reading a CSV file (using the native module):

```python
import csv

with open('dados.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
```

---

2. Creating/Writing a **CSV** (using Pandas - Recommended for structured data):

```python
import pandas as pd

data = {'Nome': ['Ana', 'Bruno'], 'Idade': [25, 30]}
df = pd.DataFrame(data)
df.to_csv('novo_dados.csv', index=False)
```