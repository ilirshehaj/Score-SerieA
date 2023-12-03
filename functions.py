# Here are all the functions used to retrieve data from SofaScore
import pandas as pd
from bs4 import BeautifulSoup

# Get HTML from a web address
def get_html(page, driver):
    # get page source from driver
    driver.get(page)
    source = driver.page_source
    #get html from the source
    html = BeautifulSoup(source, 'html.parser')
    return html, driver
#Create Final Excel
def create_excel(today, df, out_rank_table, out_team_sheets):
    with pd.ExcelWriter(f'Result{today}.xlsx') as writer:
        df.to_excel(writer, sheet_name='Serie A - Standings', index=False)
        lc_index = 0
        for df_item in out_team_sheets:
            df_item.to_excel(writer, sheet_name=out_rank_table[lc_index]['Team'], index=False)
            lc_index+=1