---
window: [terminal]
---

# US National Team Test Analytic Site

This is a multi-page website that lets the user run analytics on USRowing National Team data. This website uses Python, JavaScript, HTML, CSS and SQL.

## Terms

* USRowing is the the governing body of the US National Team for rowing.
* An "erg" (aka ergometer) is a rowing machine that simulates the rowing motion. This removes all external conditions that rowers face when racing on the water. By comparing erg times, rowers can compare raw strength.

## Background

Outside of the classroom, my passion is rowing.

On the USrowing website, there is a page called "National Team Erg Testing". See below for a description taken from the website.

```

From USRowing:

"As part of Talent Identification and Development, USRowing collects erg scores for all athletes who want to be considered for the National Team at all levels; U19, U23, Senior and Para. Submission deadlines and required distance is listed below.  Only the athlete's name, age, affiliation, and scores will be posted. Scores will be listed alphabetically.

Scores will be considered for discretionary invitations to selection camps. USRowing expects athletes to submit at least one 6k and one 2k during the 7-month period in which the data will be collected.

The deadline to submit scores will be the last day of the month and scores will be posted to the USRowing website within the first 7 days of the following month. "

```

Most notably, this page contains links to a form and separate pages for each month of data submitted. The monthly submissions posted at this time start from November of 2021 and go through May of 2022.

### Creating the Database - `general.db`

I first created excel spreadsheets for every page of data on the USRowing website. I inputted the data from the website into these CSVs and made sure the formatting was consistent amon all files. This led to the addition of columns for event and classification, and even changing the all the times to follow HH:MM:SS format rather than the original MM:SS format (the latter is more commonly used among rowers). I then saved these as CSVs and uploaded them into my codespace.

In my codespace, I created a database called `general.db` and tables for each CSV sheet within this database. I coded up a program called `upload.py`, which took in one command line arguenment (the file's name) and reads the data into a specific table in `general.db`. I also created a CSV called "total.csv", which contains the data of all tables combined, and read it into the database as the table `"total"`.

Below is a list of the CSVs I used. These and upload.py can be found in the folder `csv/`.

*`"april_2022.csv"`
*`"dec_2021.csv"`
*`"feb_2022.csv"`
*`"jan_2022.csv"`
*`"march_2022.csv"`
*`"may_2022.csv"`
*`"nov_2022.csv"`
*`"total.csv"`


That was how I created and stored my data in my database! Below is the result of the `".schema"` command in SQL for `general.db`.

'''

.schema
CREATE TABLE nov21 (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE dec21 (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE jan22 (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE feb22 (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE mar22 (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE apr22 (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE may22 (
    event TEXT NOT NULL,
	  athlete TEXT NOT NULL,
	  distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL, hash TEXT NOT NULL
);
CREATE TABLE total (
    event TEXT NOT NULL,
    athlete TEXT NOT NULL,
    distance TEXT NOT NULL,
    time TIME NOT NULL,
    classification TEXT
);

'''

### `app.py`

In `app.py`, there are a lot of imports at the top of the page. Among this is CS50's SQL module and a few helper functions. Then code to configure the application and the session to use filesystem. It also sets `db.execute` (from CS50's library) to query `general.db`.

The `"/"` route leads to the page `"index.html"`. This is the main page of my website. There is a login decorator on this page, so you need to login to access it.

The `"/login` route is what logs the user into the system. It uses `check_password_hash` to compare hashes of users' passwords. `login` also "remembers" that a user is logged in by storing his/her/their `user_id`, an INTEGER, in `session`. That way, any of this file's routes can check which user, if any, is logged in. Once the user has successfully logged in, `login` will redirect to `"/"`, taking the user to their home page.

The `"/logout"` route simply clears `session`, effectively logging a user out.

The `"/register" route ensures that the user fills all necesary data to create an account before it inserts that into the database. For instance, it will kick back an apology if a username or password is not provided.

The `"/data"` route displays all of the data inside the database on one webpage. This data is organized by event, using a SQL command and Jinga.


The `"/quicksearch"` route allows the user to decide what parts of the data they want to view, then displays that data. The user makes selections via a drop down menu. This selection is sent back to app.py through the form and is run through if-statements. Each if-statement corresponds to a possible selection by the user. Each if-statement then executed a specific SQL commmand, which then is displayed via Jinga into the HTML file! This is shown at the bottom of the page. By default, all the data will be displayed in this part of the page until the user submits a selection.

### `helpers.py`

Inside `helpers.py`, there is `apology`. It essentially just renders the  template, `apology.html`. It also defines within itself another function, `escape`. This function just replaces the special characters in apologies. By defining `escape` inside of `apology`, the fuction is scoped to the latter, so no other functions will be able to call it.

The `login_required` function is also present in `helpers.py`.

### `static/`

This is my `static/` folder. Inside of this is `"styles.css"`, as well as my images. The image `"usrowing_oar.png"` is the image of the USRowing oar above the title `"USNT Test Analytics"`. The image `"usrowing_logo.png"` is the USRowing logo, which is the background of the page. This is used across every page on my website. The image `"drop_down_icon.png"` is the image of little arrow that is used on my `"/quicksearch"` menu (this rotates down when the menu is clicked on).

### `templates/`

This is my `templates/` folder. Inside `templates/` I have the following html files: `apology.html`, `data.html`, `index.html`, `layout.html`, `login.html`, `quicksearch_result.html` and `register.html`. The titles correspond to the parts of app.py they relate to (exceptions being `layout.html`, but that is just the baseline layout for each page.)
