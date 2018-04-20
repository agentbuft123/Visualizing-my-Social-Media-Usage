{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red5\green99\blue193;}
{\*\expandedcolortbl;;\csgenericrgb\c1961\c38824\c75686;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\b\fs24 \cf0 Data Sources Used\

\b0 1) Facebook Graph API - this nifty platform allows user to collect Facebook data for a specified user. \
- Requires an Access Token which can be obtained via {\field{\*\fldinst{HYPERLINK "https://developers.facebook.com/docs/graph-api"}}{\fldrslt \cf2 \ul \ulc2 https://developers.facebook.com/docs/graph-api}}\
2) Instagram via OAuth - this platform was used to collect data for a specified user.\
- Requires an Access Token which can be obtained via {\field{\*\fldinst{HYPERLINK "https://www.instagram.com/developer/"}}{\fldrslt \cf2 \ul \ulc2 https://www.instagram.com/developer/}}\
\
- These two data sources are incorporated through a secrets.py file that contains the access tokens for Facebook and Instagram. \
\

\b Additional pointers for how to get started:\

\b0 - Make sure Facebook, Instagram, and Plotly are installed.\
- For Plotly, head over to their site (plot.ly), make an account, and obtain a username and API key. Make sure to put the Plotly API key to your secrets.py\
\

\b Brief Description of code structure:\

\b0 - When you run \'91python3 proj_final.py\'92 and number of things happen. \
- First, the method Facebook_Scan collects likes, tags, and create-time from your FB account. It stores the data into a cache (Facebook_Cache_File.json) for faster processing. \
- Second, the method get_weekly_results is responsible for organizing the data by weekdays so associating how many likes/tag you have in a particular day of the week (i.e. you have 23 likes on a Tuesday). \
- Third, the method write_sql_fb is responsible for getting all that data and putting them into a dedicated database. \
- Finally, starting from the method make_interactive() the program then prepares the data to upload to plotly. From there the user can specify what kind of visual they want to see. \
\
***The structure above is for the Facebook portion; however, the Instagram portion follows the same convention. \
\

\b User Guide:\

\b0 - Make sure all the necessary packages are installed. Look over lines 1-5 and install as necessary. \
- Run \'93python3 proj_final.py\'94\
- Make a selection as to what kind of data you want to visualize on a graph.\
        1. Average Number of Facebook Likes and Tags Given Day of the Week\
        2. Average Number of Instagram Likes Given Day of the Week\
        3. Total Number of Facebook Likes and Tags Given Day of the Week\
        4. Total Number of Instagram Likes Given Day of the Week\
\
***NOTE**** If you enter anything other than 1-4 or \'91exit\'92, the program will notify the user that an invalid selection was made. And it will prompt the user to acknowledge this should the user wish to run the program again. Failure to acknowledge will result in the program terminating. }