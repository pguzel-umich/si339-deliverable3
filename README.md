# OVERVIEW

Our Python script processes data for male and female athletes from CSV files from the given drive folder. We did not upload the CSV files to GitHub because there were simply too many.
Our short program generates different HTML tables with the provided athlete data. For our index page, it creates a table inside a table to include both female and male athletes. Furthermore, we added a set of functions with loops to make individual HTML pages for each athlete.

The output includes an HTML page (index.html) with links to individual athlete profiles (athlete_id.html) containing their personal records.

## How It Works
The program reads CSV files from directories (drive_download/athletes/mens_team and drive_download/athletes/womens_team). Then, it takes each athlete’s data into dictionaries, separating their season and career records. Afterwards, it creates a main page (index.html) with a table that includes two tables inside (men and women); furthermore each cell includes athletes' profile images, names, IDs, and hyperlinks their individual pages. The program creates an individual HTML page for each athlete with their season and career performance records.\

In short, our program creates index.html for all athletes and individual HTML files in the athlete_pages/ directory for each athlete.

1. **`load_data(directory, athlete_list)`**: Reads CSV files from the directory and organizes athlete data into dictionaries, adding them to a list.

2. **`template_table(athlete_list)`**: Generates an HTML table of athletes with links to their individual profile pages.

3. **`season_record(athlete_dict)`**: Returns an HTML table of an athlete's season records.

4. **`career_record(athlete_dict)`**: Returns an HTML table of an athlete's career records.

5. **`render_student_html(athlete_dict, template_html)`**: Adds an athlete's profile picture, name, and ID with template_html.

6. **`render_html(athlete_list, student_html_template)`**: Creates individual HTML files for each athlete with student_html_template.


### Data Requirements
For phyton code to run, we require just the CSV files that include athlete and event data. Download the files from the drive provided by SI339 staff. We put all the files on the drive and called drive_download for easy access and navigation. The two below are the files we absolutely need. We find all the data names and tags in these two files. The rest of the data on GitHub is required for HTML5 documents to run correctly and include all the other data, the data that we do not need to create the HTML5 files themselves (images, favicon, logo, etc.).
* drive_download/athletes/mens_team
* drive_download/athletes/womens_team

## How To Use
Clone the project and navigate to the project directory. Download the data stated in **Data Requirements** and place the folders properly. Then, in order to run the program, simply enter the provided line below to your terminal:
 **`python render_templates.py`**

The script will generate:
* A main HTML page (index.html) displaying tables of all athletes with links to their profile pages.
* Each athlete's Individual HTML profile (athlete_id.html) pages contain their season and career records. To prevent overpopulation in the main working directory, these will be placed in the athlete_pages/directory.

## GitHub Data Structure
github                                                  \
&emsp;&emsp; athlete_pages                              \
&emsp;&emsp;&emsp;&emsp; [athlete_id].html              \
&emsp;&emsp; index.html                                 \
&emsp;&emsp; render_templates.py                        \
&emsp;&emsp; images                                     \
&emsp;&emsp;&emsp;&emsp; AthleteImages                  \
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [athlete_id].jpg   \
&emsp;&emsp;&emsp;&emsp; icon.png                       \
&emsp;&emsp;&emsp;&emsp; images.jpeg                    \
&emsp;&emsp;&emsp;&emsp; site_logo.png                           
