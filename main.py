from utils.ukb_functions import get_data_coding_ukb

# Call the function
df = get_data_coding_ukb()

# Show result
if df is not None:
    print(df.head())
else:
    print("No data returned.")
