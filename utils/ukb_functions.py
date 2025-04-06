# utils/ukb_functions.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_data_coding_ukb(data_coding, number_attempts=5, time_duration=5):
    """
    Download and parse data coding metadata from UK Biobank Showcase.

    Parameters:
    - data_coding (str or int): The ID of the data coding to fetch.
    - number_attempts (int): How many times to retry on failure.
    - time_duration (int): Time (in seconds) to wait between attempts.

    Returns:
    - pandas.DataFrame: The data coding table, or None if failed.
    """
    
    specific_messages = {
        '19': 'There are ICD10 coding.',
        '2': 'There are SOC2000 coding.',
        '87': 'There are ICD9 coding.',
    }

    alternative_url_codings = {'123', '240', '259', '4', '744'}

    data_coding = str(data_coding)

    if data_coding in specific_messages:
        print(f"ℹ️  {specific_messages[data_coding]}")
        return None

    if data_coding in alternative_url_codings:
        url = f"https://biobank.ndph.ox.ac.uk/showcase/coding.cgi?id={data_coding}&nl=1"
    else:
        url = f"https://biobank.ndph.ox.ac.uk/showcase/coding.cgi?id={data_coding}"

    for attempt in range(number_attempts):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', {'border': '0', 'cellspacing': '2'})

            if table is None:
                raise ValueError("Could not find a data coding table on the page.")

            headers = [th.text.strip() for th in table.find_all('th')]
            rows = [
                [td.text.strip() for td in tr.find_all('td')]
                for tr in table.find_all('tr')[1:]
            ]

            return pd.DataFrame(rows, columns=headers)

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(time_duration)

    print("❌ Failed to download data coding.")
    return None
