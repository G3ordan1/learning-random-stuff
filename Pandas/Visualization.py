# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv('homelessness.csv', index_col=0)
# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print("info", homelessness.info())

# Print the shape of homelessness
print("shape", homelessness.shape)

# Print a description of homelessness
print("describe", homelessness.describe())

# Print the values of homelessness
print("values", homelessness.values)

# Print the column index of homelessness
print("columns", homelessness.columns)

# Print the row index of homelessness
print("row index", homelessness.index)

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print("sort", homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(
    ["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (
    homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness["region"].isin(
    ["South Atlantic", "Mid-Atlantic"])]

# See the result
print(south_mid_atlantic)

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * \
    homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values(
    'indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
