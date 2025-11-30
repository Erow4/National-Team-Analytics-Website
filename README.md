---
window: [terminal]
url: https://youtu.be/nc3260VgfkU
---

# USRowing National Team Analytics Site

Created a multi-page website for analyzing USRowing National Team data using Python, JavaScript, HTML, CSS, and SQL. The site allowed users to view ordered data subsets, with a dropdown menu for event/category selection. I processed the data in CSV format, uploaded it to a SQL database via a Python program, and used HTML/CSS for a user-friendly UI. The site executed SQL queries on data from multiple Excel CSVs based on user selections.

## Terms

* USRowing is the the governing body of the US National Team for rowing.
* An "erg" (aka ergometer) is a rowing machine that simulates the rowing motion. This removes all external conditions that rowers face when racing on the water, which allows rowers to compare their raw speeds.

## Background

Outside of the classroom, my passion is rowing.

On the USrowing website, there is a page called "National Team Erg Testing". See below for the description of the page taken from the website.

```

From USRowing:

"As part of Talent Identification and Development, USRowing collects erg scores for all athletes who want to be considered for the National Team at all levels; U19, U23, Senior and Para. Submission deadlines and required distance is listed below.  Only the athlete's name, age, affiliation, and scores will be posted. Scores will be listed alphabetically.

Scores will be considered for discretionary invitations to selection camps. USRowing expects athletes to submit at least one 6k and one 2k during the 7-month period in which the data will be collected.

The deadline to submit scores will be the last day of the month and scores will be posted to the USRowing website within the first 7 days of the following month. "

```

Most notably, this page contains links to a form and separate pages for each month of data submitted. The monthly submissions available start from November of 2021 and go through May of 2022.


### The Program

To compile and run the program, please type 'flask run'. Then copy/paste the given link into another tab. This website uses Python, JavaScript, HTML, CSS and SQL.

#### 'Register'

This is the register page. You will need to register an account. Please type in your username and password, as well as your password confirmation.

#### 'Login'

This is the login page. Please type in your username and password to login.

#### 'Home'

This is the homepage. You have full access to all the links now that you have registered/logged in. These links include 'HOME', 'DATA' and 'QUICKSEARCH'.

#### 'Data'

This is the data page! It displays all of the data in the system, ordered by event (default order).

NOTE: if there is no value listed for Classification, that means that there is no Classification for that entry.

#### 'Quicksearch'

This is the quicksearch page! Use the drop-down menu to select an option to be displayed. By default, all data will be shown, but this will change after a selection has been submitted! There are many options,such as 'Distance: 2k', 'Distance: 6k', 'All: Classification', and many more. After you make a selection, the data will be displayed accordingly!


NOTE: if there is no value listed for Classification, that means that there is no Classification for that entry.


