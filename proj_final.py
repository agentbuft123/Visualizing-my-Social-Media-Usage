import secrets
import unittest, sqlite3, json, requests, datetime, calendar, csv, facebook, instagram
from pprint import pprint
import plotly.plotly as py
import plotly.graph_objs as go

CACHE_FNAME = "Facebook_Cache_File.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

def Facebook_Scan(access_token_in):
    graph = facebook.GraphAPI(access_token=access_token_in, version="2.12")
    tagged_pics = graph.request('me?fields=id,name,photos.limit(100){tags{name},created_time,likes}')
    user_id = tagged_pics['id']

    list_of_pics = tagged_pics['photos']['data']
    data = []
    if user_id in CACHE_DICTION:
        print("Accessing Facebook cache file. Please wait...")
        data = CACHE_DICTION[user_id]
    else:
        print("Pinging Facebook. Please wait...")
        for pic in list_of_pics:
            time = pic['created_time']
            y, m, d = (int(time.split('-')[0]), int(time.split('-')[1]), int(time.split('-')[2][:2]))
            weekday = calendar.day_name[datetime.datetime(y, m, d).weekday()]

            tags = pic['tags']['data']
            names = []
            for tag in tags:
                names.append(tag['name'])

            like_count = 0
            if 'likes' in pic.keys():
                for like in pic['likes']:
                    like_count += 1

            data.append((weekday, len(names), like_count))

        CACHE_DICTION[user_id] = data
        filename = open(CACHE_FNAME, 'w')
        filename.write(json.dumps(CACHE_DICTION))
        filename.close()
    return data

# This portion is responsible for organizing the data into a clean dictionary format

def get_weekly_results(list_of_data):

    weekday_dict = {"Monday": {"posts": 0, "number_of_tags": 0, "likes": 0}, "Tuesday": {"posts": 0, "number_of_tags": 0, "likes": 0},
    "Wednesday": {"posts": 0, "number_of_tags": 0, "likes": 0}, "Thursday": {"posts": 0, "number_of_tags": 0, "likes": 0},
    "Friday": {"posts": 0, "number_of_tags": 0, "likes": 0}, "Saturday": {"posts": 0, "number_of_tags": 0, "likes": 0},
    "Sunday": {"posts": 0, "number_of_tags": 0, "likes": 0}}



    for post in list_of_data:
        if post[0] == "Monday":
            weekday_dict["Monday"]['posts'] += 1
            weekday_dict["Monday"]['number_of_tags'] += post[1]
            weekday_dict["Monday"]['likes'] += post[2]
        elif post[0] == "Tuesday":
            weekday_dict["Tuesday"]['posts'] += 1
            weekday_dict["Tuesday"]['number_of_tags'] += post[1]
            weekday_dict["Tuesday"]['likes'] += post[2]
        elif post[0] == "Wednesday":
            weekday_dict["Wednesday"]['posts'] += 1
            weekday_dict["Wednesday"]['number_of_tags'] += post[1]
            weekday_dict["Wednesday"]['likes'] += post[2]
        elif post[0] == "Thursday":
            weekday_dict["Thursday"]['posts'] += 1
            weekday_dict["Thursday"]['number_of_tags'] += post[1]
            weekday_dict["Thursday"]['likes'] += post[2]
        elif post[0] == "Friday":
            weekday_dict["Friday"]['posts'] += 1
            weekday_dict["Friday"]['number_of_tags'] += post[1]
            weekday_dict["Friday"]['likes'] += post[2]
        elif post[0] == "Saturday":
            weekday_dict["Saturday"]['posts'] += 1
            weekday_dict["Saturday"]['number_of_tags'] += post[1]
            weekday_dict["Saturday"]['likes'] += post[2]
        else:
            weekday_dict["Sunday"]['posts'] += 1
            weekday_dict["Sunday"]['number_of_tags'] += post[1]
            weekday_dict["Sunday"]['likes'] += post[2]


    tags_average = {}
    tags_total = {}
    for day in weekday_dict.keys():
        numppl = weekday_dict[day]['number_of_tags']
        numlikes = weekday_dict[day]['likes']
        tags_total[day] = (numppl, numlikes)

    return tags_total

# This portion is responsible for organizing the data into a clean dictionary format

def get_weekly_results_average(list_of_data):
    weekday_dict = {"Monday": {"posts": 0, "number_of_tags": 0, "likes": 0}, "Tuesday": {"posts": 0, "number_of_tags": 0, "likes": 0},
    "Wednesday": {"posts": 0, "number_of_tags": 0, "likes": 0}, "Thursday": {"posts": 0, "number_of_tags": 0, "likes": 0},
    "Friday": {"posts": 0, "number_of_tags": 0, "likes": 0}, "Saturday": {"posts": 0, "number_of_tags": 0, "likes": 0},
    "Sunday": {"posts": 0, "number_of_tags": 0, "likes": 0}}
    for post in list_of_data:
        if post[0] == "Monday":
            weekday_dict["Monday"]['posts'] += 1
            weekday_dict["Monday"]['number_of_tags'] += post[1]
            weekday_dict["Monday"]['likes'] += post[2]
        elif post[0] == "Tuesday":
            weekday_dict["Tuesday"]['posts'] += 1
            weekday_dict["Tuesday"]['number_of_tags'] += post[1]
            weekday_dict["Tuesday"]['likes'] += post[2]
        elif post[0] == "Wednesday":
            weekday_dict["Wednesday"]['posts'] += 1
            weekday_dict["Wednesday"]['number_of_tags'] += post[1]
            weekday_dict["Wednesday"]['likes'] += post[2]
        elif post[0] == "Thursday":
            weekday_dict["Thursday"]['posts'] += 1
            weekday_dict["Thursday"]['number_of_tags'] += post[1]
            weekday_dict["Thursday"]['likes'] += post[2]
        elif post[0] == "Friday":
            weekday_dict["Friday"]['posts'] += 1
            weekday_dict["Friday"]['number_of_tags'] += post[1]
            weekday_dict["Friday"]['likes'] += post[2]
        elif post[0] == "Saturday":
            weekday_dict["Saturday"]['posts'] += 1
            weekday_dict["Saturday"]['number_of_tags'] += post[1]
            weekday_dict["Saturday"]['likes'] += post[2]
        else:
            weekday_dict["Sunday"]['posts'] += 1
            weekday_dict["Sunday"]['number_of_tags'] += post[1]
            weekday_dict["Sunday"]['likes'] += post[2]


# This portion is responsible for getting the total and the average tags per weekday

    tags_average = {}
    tags_total = {}
    for day in weekday_dict.keys():
        numppl = weekday_dict[day]['number_of_tags']
        numpics = weekday_dict[day]['posts']
        numlikes = weekday_dict[day]['likes']
        try:
            avg_tag = numppl / numpics
            avg_likes = numlikes / numpics
            tags_average[day] = (avg_tag, avg_likes)
            tags_total[day] = (numppl, numlikes)

        except:
            return tags_average

# This portion is responsible for writing the SQL database via table

def write_sql_averages_fb(averages_dict):
    conn = sqlite3.connect("Facebook.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Facebook_Averages")
    cur.execute("CREATE TABLE Facebook_Averages (Weekday TEXT, AvgLikes NUMBER, AvgTags NUMBER)")

    for day in averages_dict.keys():
        tup = (day, averages_dict[day][1], averages_dict[day][0])
        cur.execute('INSERT INTO Facebook_Averages (Weekday, AvgLikes, AvgTags) VALUES (?,?,?)', tup)
        conn.commit()

    cur.close()

# EFFECTS: takes in a dictionary of data and writes it to sql file and csv
def write_sql_fb(facebook_data):
    conn = sqlite3.connect("Facebook.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Facebook_Data")
    cur.execute("CREATE TABLE Facebook_Data (Weekday TEXT, Num_Tags NUMBER, Num_Likes NUMBER)")
    for data in facebook_data:
        tup = (data[0], data[1], data[2])
        cur.execute('INSERT INTO Facebook_Data (Weekday, Num_Tags, Num_Likes) VALUES (?,?,?)', tup)
        conn.commit()

    cur.close()


# This portion makes the function calls to Facebook

data = Facebook_Scan(secrets.fb_access_token)
write_sql_fb(data)
fb_avgs = get_weekly_results_average(data)
fb_tots = get_weekly_results(data)
write_sql_averages_fb(fb_avgs)



CACHE_FNAME = "Instagram_Cache_File.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

# Get instagram post data depending on user
def get_instagram_data(access_token_in):
    data = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(access_token_in)
    posts_str = requests.get(data).text
    posts = json.loads(posts_str)['data']
    user_id = posts[0]['user']['id']

    if user_id in CACHE_DICTION:
        print ("Accessing Instagram cache file. Please wait...")
        insta_data = CACHE_DICTION[user_id]
    else:
        print ("Pinging Instagram. Please wait...")
        data_tups = []
        for post in posts:
            timestamp = datetime.datetime.fromtimestamp(int(post['created_time']))
            weekday = calendar.day_name[timestamp.weekday()]
            data_tups.append((post['user']['id'], post['likes']['count'], weekday))

        CACHE_DICTION[user_id] = list(data_tups)
        insta_data = data_tups
        filename = open(CACHE_FNAME, 'w')
        filename.write(json.dumps(CACHE_DICTION))
        filename.close()
    return insta_data


# Sort data into a dictionary sorted by weekday
def get_ig_weekly_results(list_of_data):
    user_id = list_of_data[0][0]
    weekday_dict = {"Monday": {"posts": 0, "likes": 0}, "Tuesday": {"posts": 0, "likes": 0},
    "Wednesday": {"posts": 0, "likes": 0}, "Thursday": {"posts": 0, "likes": 0},
    "Friday": {"posts": 0, "likes": 0}, "Saturday": {"posts": 0, "likes": 0},
    "Sunday": {"posts": 0, "likes": 0}}
    for post in list_of_data:
        if post[2] == "Monday":
            weekday_dict["Monday"]['posts'] += 1
            weekday_dict["Monday"]['likes'] += post[1]
        elif post[2] == "Tuesday":
            weekday_dict["Tuesday"]['posts'] += 1
            weekday_dict["Tuesday"]['likes'] += post[1]
        elif post[2] == "Wednesday":
            weekday_dict["Wednesday"]['posts'] += 1
            weekday_dict["Wednesday"]['likes'] += post[1]
        elif post[2] == "Thursday":
            weekday_dict["Thursday"]['posts'] += 1
            weekday_dict["Thursday"]['likes'] += post[1]
        elif post[2] == "Friday":
            weekday_dict["Friday"]['posts'] += 1
            weekday_dict["Friday"]['likes'] += post[1]
        elif post[2] == "Saturday":
            weekday_dict["Saturday"]['posts'] += 1
            weekday_dict["Saturday"]['likes'] += post[1]
        else:
            weekday_dict["Sunday"]['posts'] += 1
            weekday_dict["Sunday"]['likes'] += post[1]
    average_likes = {}
    for weekday in weekday_dict:
            average_likes[weekday] = weekday_dict[weekday]['likes']
    average_likes["User ID"] = int(user_id)
    return average_likes



def get_ig_weekly_avg_results(list_of_data):
    user_id = list_of_data[0][0]
    weekday_dict = {"Monday": {"posts": 0, "likes": 0}, "Tuesday": {"posts": 0, "likes": 0},
    "Wednesday": {"posts": 0, "likes": 0}, "Thursday": {"posts": 0, "likes": 0},
    "Friday": {"posts": 0, "likes": 0}, "Saturday": {"posts": 0, "likes": 0},
    "Sunday": {"posts": 0, "likes": 0}}
    for post in list_of_data:
        if post[2] == "Monday":
            weekday_dict["Monday"]['posts'] += 1
            weekday_dict["Monday"]['likes'] += post[1]
        elif post[2] == "Tuesday":
            weekday_dict["Tuesday"]['posts'] += 1
            weekday_dict["Tuesday"]['likes'] += post[1]
        elif post[2] == "Wednesday":
            weekday_dict["Wednesday"]['posts'] += 1
            weekday_dict["Wednesday"]['likes'] += post[1]
        elif post[2] == "Thursday":
            weekday_dict["Thursday"]['posts'] += 1
            weekday_dict["Thursday"]['likes'] += post[1]
        elif post[2] == "Friday":
            weekday_dict["Friday"]['posts'] += 1
            weekday_dict["Friday"]['likes'] += post[1]
        elif post[2] == "Saturday":
            weekday_dict["Saturday"]['posts'] += 1
            weekday_dict["Saturday"]['likes'] += post[1]
        else:
            weekday_dict["Sunday"]['posts'] += 1
            weekday_dict["Sunday"]['likes'] += post[1]
    average_likes = {}
    for weekday in weekday_dict:
        if weekday_dict[weekday]['posts'] != 0:
            average_likes[weekday] = (weekday_dict[weekday]['likes'] / weekday_dict[weekday]['posts'])
        else:
            average_likes[weekday] = weekday_dict[weekday]['likes']
    average_likes["User ID"] = int(user_id)
    return average_likes



def write_sql_ig(weekly_data):
    conn = sqlite3.connect("Instagram.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Insta_Total_Likes")
    cur.execute("""CREATE TABLE Insta_Total_Likes (user_id NUMBER, Monday NUMBER, Tuesday NUMBER,
                    Wednesday NUMBER, Thursday NUMBER, Friday NUMBER, Saturday NUMBER, Sunday NUMBER)""")
    tup = (weekly_data["User ID"], weekly_data['Monday'], weekly_data['Tuesday'], weekly_data['Wednesday'], weekly_data['Thursday'], weekly_data['Friday'], weekly_data['Saturday'], weekly_data['Sunday'])
    cur.execute('INSERT INTO Insta_Total_Likes (user_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES (?,?,?,?,?,?,?,?)', tup)
    conn.commit()

    cur.close()

def write_sql_averages_ig(weekly_data):
   conn = sqlite3.connect("Instagram.sqlite")
   cur = conn.cursor()

   cur.execute("DROP TABLE IF EXISTS Insta_AvgLikes")
   cur.execute("""CREATE TABLE Insta_AvgLikes (user_id NUMBER, Monday NUMBER, Tuesday NUMBER,
                   Wednesday NUMBER, Thursday NUMBER, Friday NUMBER, Saturday NUMBER, Sunday NUMBER)""")
   tup = (weekly_data["User ID"], weekly_data['Monday'], weekly_data['Tuesday'], weekly_data['Wednesday'], weekly_data['Thursday'], weekly_data['Friday'], weekly_data['Saturday'], weekly_data['Sunday'])
   cur.execute('INSERT INTO Insta_AvgLikes (user_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES (?,?,?,?,?,?,?,?)', tup)
   conn.commit()

   cur.close()


# This portion is responsible for making the function calls to Instagram -> getting the actual data

data_list = get_instagram_data(secrets.ig_access_token)
totally = get_ig_weekly_results(data_list)
write_sql_ig(totally)
weekly = get_ig_weekly_avg_results(data_list)
write_sql_averages_ig(weekly)


# Starting from this portion, this component is responsible for generating the visuals via Plotly
py.sign_in(secrets.plotly_username, secrets.plotly_api_key)

def make_interactive():

    def ask_for_input():
        user_input = input(
        '''Please choose which data visualization you'd like to see (or enter 'exit' to quit)!
        1. Average Number of Facebook Likes and Tags Given Day of the Week
        2. Average Number of Instagram Likes Given Day of the Week
        3. Total Number of Facebook Likes and Tags Given Day of the Week
        4. Total Number of Instagram Likes Given Day of the Week
        Enter: ''')

        if user_input == '1':

# This portion is responsible for generating Facebook Average # of likes visuals

            fb_avglikes = []
            fb_avgtags = []
            days = []

            for day in fb_avgs:
                fb_avglikes.append(fb_avgs[day][1])
                fb_avgtags.append(fb_avgs[day][0])
                days.append(day)

            data1 = go.Bar(x = days, y = fb_avglikes, name = "Average Number of Likes Per Post")
            data2 = go.Bar(x = days, y = fb_avgtags, name = "Average Number of Tags Per Post")

            layout = go.Layout(title = "Average Number of Facebook Likes and Tags", barmode = 'group', xaxis = dict(title = 'Day of the Week'), yaxis = dict(title = "Average count"))
            data = [data1, data2]
            figure = go.Figure(data=data,layout=layout)

            py.plot(figure, filename="Facebook Likes and Tags Visualization")
            print("Operation successful!")
            ask_for_input()
        elif user_input == '2':

# This portion is responsible for generating Instagram Average # of Likes visual

            weeklyData = []
            weekdays = []

            for day in weekly:
                if (len(weekdays) < 7):
                    weeklyData.append(weekly[day])
                    weekdays.append(day)

            data = [go.Bar(x = weekdays, y = weeklyData)]

            layout = go.Layout(title = "Average Number of Instagram Likes", xaxis = dict(title = 'Day of the Week'), yaxis = dict(title = "Likes"))
            figure = go.Figure(data=data,layout=layout)

            py.plot(figure, filename="Instagram Likes Visualization")
            print("Operation successful!")
            ask_for_input()

        elif user_input == '3':

# This portion is responsible for generating Facebook total Likes&Tags visual

            fb_Totlikes = []
            fb_Tottags = []
            days = []

            for day in fb_avgs:
                fb_Totlikes.append(fb_tots[day][1])
                fb_Tottags.append(fb_tots[day][0])
                days.append(day)

            data1 = go.Bar(x = days, y = fb_Totlikes, name = "Total Likes Per Post")
            data2 = go.Bar(x = days, y = fb_Tottags, name = "Total Tags Per Post")

            layout = go.Layout(title = "Total Number of Facebook Likes and Tags", barmode = 'group', xaxis = dict(title = 'Day of the Week'), yaxis = dict(title = "Total Number"))
            data = [data1, data2]
            figure = go.Figure(data=data,layout=layout)

            py.plot(figure, filename="Facebook Likes and Tags Visualization")
            print("Operation successful!")
            ask_for_input()

        elif user_input == '4':


# This portion is responsible for generating Instagram likes visual

            weeklyData = []
            weekdays = []

            for day in totally:
                if (len(weekdays) < 7):
                    weeklyData.append(totally[day])
                    weekdays.append(day)

            data = [go.Bar(x = weekdays, y = weeklyData)]

            layout = go.Layout(title = "Total Number of Instagram Likes", xaxis = dict(title = 'Day of the Week'), yaxis = dict(title = "Total Likes"))
            figure = go.Figure(data=data,layout=layout)

            py.plot(figure, filename="Instagram Likes")
            print("Operation successful!")
            ask_for_input()

        elif user_input == 'exit':
            print("Ciao!")
            #return None

        else:
            confirm_input = input("You have inputted an invalid selection. Type 'y' to acknowledge and try again:")
            if confirm_input == 'y':
                ask_for_input()
            else:
                print("Sorry, this program doesn't cater to people who can't follow directions! Good bye!")



    ask_for_input()


if __name__ == "__main__":
    make_interactive()
