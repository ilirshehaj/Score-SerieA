#Main logic of the Sofa Score scraping tool for Serie A
import functions as f
import global_var as gl
import pandas as pd
from selenium import webdriver
from datetime import date
import re

def main():
    today = date.today()
    # dd/mm/YY
    today = today.strftime("%d%m%y")
    # define main page to call 
    seriea_page = gl.seriea_page
    #create new driver
    driver = webdriver.Chrome()
    # Get HTML    
    html = f.get_html(seriea_page, driver)
    # Import global variables
    team_link = gl.team_link
    rank_class = gl.rank_class
    rank_value = gl.rank_value 
    rank_name = gl.rank_name
    rank_name_live = gl.rank_name_live
    match_date = gl.match_date
    match_result = gl.match_result
    match_details = gl.match_details
    match_details_new = gl.match_details_new
    # Logic for Ranking
    tags = html.find_all('div', attrs={'class': rank_class})
    teams = html.find_all('div', attrs={'class': team_link})
    out_rank_table=[]
    for tag in tags:
        out_rank_dict = {}
        item_tags = tag.find_all('div', attrs={'class': rank_value})
        # Ranking
        out_rank_dict['Ranking'] = item_tags[0].text
        # Team
        item_names = tag.find_all('span', attrs={'class': rank_name})
        if item_names == []:
            item_names = tag.find_all('span', attrs={'class': rank_name_live})
        out_rank_dict['Team'] = item_names[0].text   
        # Games Played
        out_rank_dict['Games Played'] = item_tags[2].text
        # Diff goals
        out_rank_dict['Diff Goals'] = item_tags[3].text
        # Points
        out_rank_dict['Points'] = item_tags[4].text
        out_rank_table.append(out_rank_dict)
    df = pd.DataFrame(out_rank_table)    
    # Logic for team details
    out_team_sheets=[]
    # Iterate through all Serie A teams
    for count in range(0,20):
        out_team_table=[]
        # Prepare link for each team
        href = teams[0].findAll('a', href=True)[count]['href']
        link = 'https://www.sofascore.com' + href
        # Get HTML
        html = f.get_html(link, driver)
        matches = html.find_all('div', attrs={'class': match_details})
        index=0
        for match in matches:
            out_team_dict = {}
            # Match Date
            lc_date = html.find_all('div', attrs={'class': match_date})[index].text
            lc_date = lc_date[0:8] + ' ' + lc_date[8:]
            out_team_dict['Date'] = lc_date
            # Match Details (Teams & Score)
            match_detail = matches[index].find_all('div', attrs={'class': match_details_new})[0].text
            out_team_dict['Match'] = ''.join(filter(str.isalpha, match_detail))  
            lc_match = re.sub(r"(\w)([A-Z])", r"\1 \2", out_team_dict['Match']) 
            out_team_dict['Match'] = lc_match
            out_team_dict['Score'] = ''.join(filter(str.isdigit, match_detail))  
            lc_score = re.sub(r"(\w)([0-9])", r"\1 \2", out_team_dict['Score'])
            lc_score = lc_score.replace(" ", "-")
            if lc_score == "":
                out_team_dict['Score'] = "TBD"
            else:    
                out_team_dict['Score'] = lc_score
            # Match Result
            lc_result = []
            lc_result = html.find_all('div', attrs={'class': match_result})
            if lc_result != []:
                out_team_dict['Match Result'] = lc_result[index].text
            out_team_table.append(out_team_dict)
            index+=1
        df1 = pd.DataFrame(out_team_table)
        out_team_sheets.append(df1)
    #Create Final Excel
    f.create_excel(today, df, out_rank_table, out_team_sheets)
# Execute Program
if __name__ == "__main__":
    main()