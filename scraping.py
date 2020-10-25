from bs4 import BeautifulSoup
import requests
# import numpy as np
# import pandas as pd

def main():
    team = input("Team informatie van: ")
    webscrape(team)

def webscrape(team):
    URL = "http://kvtempo.nl/competitie/teams/tempo-" + team
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    teamInfo = None

    for match in soup.findAll(class_="teamdata")[-1].findAll("tr"):
        match_data = match.findAll("td")
        print(match_data)
        # if match_data:
        #     date = match_data[0].text
        #     hometeam = match_data[1].text
        #     outteam = match_data[2].text
        #     hometeamscore = match_data[3].text
        #     outteamscore= match_data[5].text

        #     print(date)
    
            # teamInfo = pd.DataFrame({'date': date,
            #                         'hometeam': hometeam,
            #                         'outteam': outteam,
            #                         'hometeamscore': hometeamscore,
            #                         'outteamscore': outteamscore})


    print(teamInfo)


if __name__ == "__main__":
    main()