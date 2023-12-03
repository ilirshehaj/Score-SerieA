# Score-SerieA
As a Serie A fan, I have started this Project to answer one question that I always had in my mind:   
Can I have an overview of the current Serie A standings, and in the same place a detailed overview of historical matches for each team?

## Serie A - Standings
Here the result is shown in an Excel file, under the sheet "Seria A - Standings".

It consists of a table with these columns:
```
1.Ranking
2.Team
3.Games Played
7.Diff Goals
9.Points
```

## Team - Details
Here the result will be part of the same Excel file as the Standings, but it will contain a separate sheet for each team. For Example: sheet "Inter", sheet "Juventus" etc...  
Each sheet will consist of a table with details from the last 8 games and 2 upcoming ones with these columns:
```
1.Date
2.Match (Team Home vs Team Away)
3.Score
4.Match Result (W - Win, D-Draw, L-Loss)
```

## Execution
The program will be executed through cmd/terminal.  
After navigating to the Project folder, execute the command:
```
python main.py
```
