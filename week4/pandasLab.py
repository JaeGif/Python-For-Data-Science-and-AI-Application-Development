import pandas as pd

filename = "week4/TopSellingAlbums.csv"

## using iloc index locator
# takes args df.iloc([rowIndex, columnIndex])

x = {
    "Student": ["David", "Samuel", "Samuel", "Terry", "Evan"],
    "Age": [27, 24, 23, 22, 32],
    "Country": [
        "UK",
        "Canada",
        "China",
        "South Africa",
        "USA",
    ],
    "Course": [
        "Python",
        "Data Structures",
        "English",
        "Machine Learning",
        "Web Development",
    ],
    "Marks": [85, 72, 100, 89, 76],
}

# cast a dictionary to a DF
df = pd.DataFrame(x)
b = df[["Marks"]]
# is case sensitive
c = df[["Country", "Course"]]
d = df["Student"]

# loc[row_label, column_label]
# iloc[row_index, column_index]
df2 = df
df2 = df2.set_index("Student")
# set the index column to the student col
print(df2.loc["Samuel", "Country"])
