Data Sources Used
1) Facebook Graph API - this nifty platform allows user to collect Facebook data for a specified user. 
- Requires an Access Token which can be obtained via https://developers.facebook.com/docs/graph-api
2) Instagram via OAuth - this platform was used to collect data for a specified user.
- Requires an Access Token which can be obtained via https://www.instagram.com/developer/

- These two data sources are incorporated through a secrets.py file that contains the access tokens for Facebook and Instagram. 

Additional pointers for how to get started:
- Make sure Facebook, Instagram, and Plotly are installed.
- For Plotly, head over to their site (plot.ly), make an account, and obtain a username and API key. Make sure to put the Plotly API key to your secrets.py

Brief Description of code structure:
- When you run ‘python3 proj_final.py’ and number of things happen. 
- First, the method Facebook_Scan collects likes, tags, and create-time from your FB account. It stores the data into a cache (Facebook_Cache_File.json) for faster processing. 
- Second, the method get_weekly_results is responsible for organizing the data by weekdays so associating how many likes/tag you have in a particular day of the week (i.e. you have 23 likes on a Tuesday). 
- Third, the method write_sql_fb is responsible for getting all that data and putting them into a dedicated database. 
- Finally, starting from the method make_interactive() the program then prepares the data to upload to plotly. From there the user can specify what kind of visual they want to see. 

***The structure above is for the Facebook portion; however, the Instagram portion follows the same convention. 

User Guide:
- Make sure all the necessary packages are installed. Look over lines 1-5 and install as necessary. 
- Run “python3 proj_final.py”
- Make a selection as to what kind of data you want to visualize on a graph.
        1. Average Number of Facebook Likes and Tags Given Day of the Week
        2. Average Number of Instagram Likes Given Day of the Week
        3. Total Number of Facebook Likes and Tags Given Day of the Week
        4. Total Number of Instagram Likes Given Day of the Week

***NOTE**** If you enter anything other than 1-4 or ‘exit’, the program will notify the user that an invalid selection was made. And it will prompt the user to acknowledge this should the user wish to run the program again. Failure to acknowledge will result in the program terminating. 
