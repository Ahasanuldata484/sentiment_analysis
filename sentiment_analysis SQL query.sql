🟢SQL querys & guide

As for the Loading Excel file (absolute path)
Clicking on the excel file > Right click > copy as path this may not work, even though the part is correct. to be sure it works⬇️
#1 You will have to copy the file path of your Excel file.
#2 Paste it in note pad or any other word application 
#3 Press Win + v (For Windows) Or Command (⌘) + 4 And clear your clipboard (to avoid any conflicts)
#4 Now copy the file path witch you have pasted earlier on your word application, finally paste it on the (Absolute path) section

To check the full table👇
SELECT * FROM analysis.sentiment_analysis;

To check any year👇 just change the year
SELECT * FROM analysis.sentiment_analysis WHERE year = 2016;

If you want to filter a timestamp by a date range👇
SELECT * FROM analysis.sentiment_analysis 
WHERE year >= '20xx' AND year < '20zz';

For all sentiment positive or negative check👇
SELECT * FROM analysis.sentiment_analysis WHERE sentiment LIKE 'positive%';

For more details 👇
SELECT * 
FROM analysis.sentiment_analysis 
WHERE year = 2016 
  AND platform = 'twitter' 
  AND sentiment = 'negative';
