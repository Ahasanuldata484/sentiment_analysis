🟢SQL querys & guide
 
Basic guide  
as for the Loading Excel file (absolute path) 
#You will have to copy the file path of your Excel file.
#paste it in note pad or any other word application 
#then copy that from that application than past it on the (absolute path) section.
  
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
