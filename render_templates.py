import csv
import os
import json
import random


# Read from the csv files (all??) in directory
male_athelete_dir = "drive_download/athletes/mens_team"
female_athelete_dir = "drive_download/athletes/womens_team"

count = 0
male_athletes_table = ""
female_athletes_table = ""

# Data required to render templates
athlete_data_male = []
athlete_data_female = []


# load data requires a directory and an athlete list that will be modified to hold dictionaries where every dictionary is the data of a student in the directory
def load_data(directory, athlete_list):
    # Read csv files for files in directory
    for filename in os.listdir(directory):

        with open(directory + "/" + filename, 'r') as fh:
            
            table = csv.reader(fh)
            
            # Want reset for every new athlete
            athlete_dict = {}
            season_list = []
            career_list = []

            #Store the id and name
            athlete_dict['name'] = next(table)
            athlete_dict['id'] = next(table)

            for row in table:

                # grab data only if a row is not empty nor a header
                if len(row) != 0 and row != ['Name', 'Overall Place', 'Grade', 'Time', 'Date', 'Meet', 'Comments', 'Photo']:


                    # Check if the row is season record row (denoted by having a value in the grade column)
                    if row[2] != '':
                        season_list.append(row)
                    else: # Append all other races to their total career
                        career_list.append(row)
            
            athlete_dict["season_record"] = season_list
            athlete_dict["career"] = career_list

            # Append completed student dictionary into athlete_list
            athlete_list.append(athlete_dict)

            # pretty_print = json.dumps(athlete_dict, indent=2)
            # print(pretty_print)
    
#athlete list is data structure returned from load_data
def template_table(athlete_list):
    template_html = ""

    for athlete_dict in athlete_list:

        # pretty_print = json.dumps(athlete_dict, indent=2)
        # print(pretty_print)
        # For every athlete we want to add in a new row within our table

        image_path = f"images/AthleteImages/{athlete_dict['id'][0]}.jpg"

        template_html += f"""
        <tr>
            <td>
                <div class="athlete_table_box">                    
                    <a href="athlete_pages/{athlete_dict['id'][0]}.html" tabindex="-1"> 
                        <img src="{image_path}" class="athlete_img" alt="img of {athlete_dict['name'][0]}, id: {athlete_dict['id']}" width="100" height="100"> 
                    </a>
                    <div id="athlete_name_box">
                        <a href="athlete_pages/{athlete_dict['id'][0]}.html" class="athlete_name"> {athlete_dict['name'][0]} </a>
                        <p>{athlete_dict['id'][0]}</p>
                    </div>
                </div>
            </td>
        </tr>
        """
    
    return template_html



load_data(male_athelete_dir,athlete_data_male)
load_data(female_athelete_dir,athlete_data_female)
male_athletes_table = template_table(athlete_data_male)
female_athletes_table = template_table(athlete_data_female)
# print(athlete_data_male)
# with open('output.txt', 'w') as file:
#     file.write(str(athlete_data_male))

index_html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deliverable 3 - Personal</title> <!--Title TK-->

    <link rel="icon" type="images/icon.png" href="images/icon.png">

    <link rel="stylesheet" href="css_files/reset.css"> 
    <link rel="stylesheet" href="css_files/default.css">
    <link rel="stylesheet" href="css_files/screen_size.css"> 
    <link rel="stylesheet" href="css_files/light.css"> 
    <link rel="stylesheet" href="css_files/high_contrast.css"> 

</head>
<body>
    
    <!--nav bar-->
    <div class="navbar">
        <a href="https://www.athletic.net/" id="logo">
            <img src="images/site_logo.jpeg" alt="site logo">
            <!-- IMG TK-->
        </a>
        <ul id="nav-links">
            <li><a href="https://www.google.com/">Login</a></li>
        </ul>
    </div>

    <div class="modes">
        <label for="theme-switch">Choose theme: </label>
        <select id="theme-switch" class="theme-switch">
            <option value="dark-mode">Default</option>
            <option value="light-mode">Light Mode</option>
            <option value="high-contrast">High Contrast</option>
        </select>
    </div>

    <!--Main box-->
    <div class="main_box">
     <!--Main box 1-->
        <div id="team_box">
            <a href="index.html" tabindex="-1">
                <img src="images/aa_skyline.jpg" class="team_img" alt="team Ann Arbor Skyline logo" width="175" height="175">
            </a>
            <h1><a href="index.html">Ann Arbor Skyline</a></h1>
            <h3> Ann Arbor 48104, MI </h3>
        </div>
        <!--Main box 2 Comments-->
        <div id="comment_box" tabindex="0">
            <h2>Comments</h2>
            <div>
                <p>Team Comments and Announcements goes here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ac risus id sem egestas mattis. Proin pellentesque diam eu orci tincidunt, sit amet congue quam tempor. Donec vulputate ligula eu eleifend viverra. Aenean congue aliquet dui et accumsan. Proin vulputate nisi et dolor convallis aliquam.</p>
            </div>
        </div>

        <!--Main box 3-->
        <div id="athletes">
            <h2>Athletes</h2>
            <div class="table_container">
                <div class="inner_table_container">
                    <table>
                        <tr>
                            <th>Mens</th>
                        </tr>
                        <tbody>
                            {male_athletes_table}
                        </tbody>
                    </table>
                </div>
                <div class="inner_table_container">
                    <table>
                        <tr>
                            <th>Womens</th>
                        </tr>
                        <tbody>
                            {female_athletes_table}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!--Main box 4-->
        <footer class="footer">
            <nav>
                <ul>
                    <li><a href="https://www.google.com/">Credidentials</a></li> 
                    <li><p>Charlie H from Deliverable 2</p></li>
                    <li><p>Poyraz G from Deliverable 2, 3, and 4</p></li>
                </ul> 
            </nav>
        </footer>
    </div>

    <script src="js/javascript.js"></script>

</body>
</html>
"""
# print(index_html_template)

with open("index.html", 'w') as file:
    file.write(index_html_template)

def season_record(athletic_dict):
    temp_html = ""
    # Loop over the season record for current athlete
    for record in athletic_dict['season_record']:
        temp_html += f"""
            <tr>
                <td>{record[1]}</td>
                <td>{record[2]}</td>
                <td>{record[3]}</td>
            </tr>
        """
    
    return temp_html

def career_record(athletic_dict):
    temp_html = ""
    # Loop over all the races an athlete has done
    for record in athletic_dict['career']:
        temp_html += f"""
            <tr>
                <td id="important">{record[1]}</td>
                <td id="important">{record[3]}</td>
                <td id="notimportant">{record[4]}</td>
                <td id="important">{record[5]}</td>
                <td id="notimportant">{record[6]}</td>
            </tr>
        """
    return temp_html

# print(athlete_data_male[0]['name'])
# print(season_record(athlete_data_male[0]))

# print(career_record(athlete_data_male[0]))

def render_student_html(athlete_dict, template_html):
    image_path = f"../images/AthleteImages/{athlete_dict['id'][0]}.jpg"

    random_value = random.randint(25, 85)

    temp_html = ""
    # Everything after title
    temp_html = f"""
    <div id="profile_box">
        <img src="{image_path}" class="athlete_img" alt="img of {athlete_dict['name'][0]}, id: {athlete_dict['id']}">
        <h2>{athlete_dict['name'][0]}</h2>
        {athlete_dict['id'][0]}

        <div class="athlete-performance">
            <div class="progress-container">
                <div class="progress-bar" style="--progress: {random_value}%;"></div>
            </div>
            <p style="font-weight: bold;">Performance over time bar is coming soon</p>
        </div>
    </div>

    <div id="season_box">
        <h2>Season Record</h2>

        <table>
            <tr>
                <th>Year 📅</th>
                <th>Grade 🏫</th>
                <th>Time ⏱️</th>
            <tr>
            {season_record(athlete_dict)}
        </table>
    </div>

    <div id="record_box">
        <h3>Career Record</h3>
        <table id="athlete_personal">
            <tr>
                <th id="important">Overall Place 📊</th>
                <th id="important">Time ⏱️</th>
                <th id="notimportant">Date 📅</th>
                <th id="important">Meet 🤝👨‍👨‍👧‍👦🏃</th>
                <th id="notimportant">Comments 💬</th>
            <tr>
            {career_record(athlete_dict)}
        </table>
    </div>

    <!--Main box 4-->
    <footer class="footer">
        <nav>
            <ul>
                <li><a href="https://www.google.com/">Credidentials</a></li> 
                <li><p>Charlie H from Deliverable 2</p></li>
                <li><p>Poyraz G from Deliverable 2, 3, and 4</p></li>
            </ul> 
        </nav>
    </footer>

    <script src="../js/javascript.js"></script>

</body>
</html>
    """
    template_html += temp_html
    return template_html
        
def render_html(athlete_list, student_html_template):
    # Loop over every student in athlete list
    for athlete_dict in athlete_list:
        with open(f"athlete_pages/{athlete_dict['id'][0]}.html", 'w') as file:
            file.write(render_student_html(athlete_dict, student_html_template))


student_html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deliverable 3 - Personal</title> <!--Title TK-->

    <link rel="icon" type="../images/icon.png" href="../images/icon.png">

    <link rel="stylesheet" href="../css_files/reset.css"> 
    <link rel="stylesheet" href="../css_files/default.css"> 
    <link rel="stylesheet" href="../css_files/screen_size.css"> 
    <link rel="stylesheet" href="../css_files/light.css"> 
    <link rel="stylesheet" href="../css_files/high_contrast.css"> 

</head>
<body>

    <a href="#profile_box" class="fab">
        <img src="../images/arrow_up.png" alt="Scroll to top" />
    </a>
    
    <!--nav bar-->
    <div class="navbar">
        <a href="https://www.athletic.net/" id="logo">
            <img src="../images/site_logo.jpeg" alt="site logo">
            <!-- IMG TK-->
        </a>
        <ul id="nav-links">
            <li><a href="https://www.google.com/">Login</a></li>
        </ul>
    </div>

    <a href="#record_box" class="skip_to_content">Skip to Content</a>

    <div class="modes">
        <label for="theme-switch">Choose theme: </label>
        <select id="theme-switch" class="theme-switch" onchange="document.body.className = this.value">
            <option value="dark-mode">Default</option>
            <option value="light-mode">Light Mode</option>
            <option value="high-contrast">High Contrast</option>
        </select>
    </div>

    <!--Main box-->
    <div class="main_box">
     <!--Main box 1-->
        <div id="team_box">
            <a href="../index.html" tabindex="-1">
                <img src="../images/aa_skyline.jpg" class="team_img" alt="team Ann Arbor Skyline logo" width="175" height="175">
            </a>
            <h1><a href="../index.html">Ann Arbor Skyline</a></h1>
            <h3> Ann Arbor 48104, MI </h3>
        </div>
"""

render_html(athlete_data_male, student_html_template)
render_html(athlete_data_female, student_html_template)
