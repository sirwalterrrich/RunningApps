
# Race Predictor & Pace Tracker

This web app provides estimated race finish times based on fitness data, while tracking your current pace, average pace, and goal pace. It also includes a stopwatch, countdown timer, and a fun soundboard feature using the pygame library.


## Features

**Race Predictor:** Estimate your race completion time based on distance and time.

**Pace and Speed Tracking:** Track your current pace, average pace, and goal pace in both miles and kilometers.

**Stopwatch and Countdown Timer:** Time yourself with precision.

**Soundboard:** Play different sounds using buttons at the bottom of the app.


## Tech Stack

**Backend:** Python (Flask)

**Frontend:** HTML, CSS (with a custom styles.css), JavaScript

**Sound Handling:** pygame library for sound effects

**Digital Display Style:** Custom CSS for sports-watch-style UI elements
## Screenshots


![App Screenshot](https://raw.githubusercontent.com/sirwalterrrich/RunningApps/refs/heads/main/race_predictor_app/app_screenshot.png).

## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```


To get the web app running on your local machine, follow these steps:

**Prerequisites**
Python 3.x
pygame library for sound effects

**Installation**
Clone the Repository
## Run Locally

Clone the project

```bash
  git clone https://github.com/your-github-username/race-predictor-app.git

```

Go to the project directory

```bash
  cd race-predictor-app
```

Create a virtual environment and Install Dependencies

**Flask**

**pygame**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

```

Start the server

```bash
  python app.py
```


## Documentation

[Documentation](https://linktodocumentation)

**Customization**

You can change the race predictor calculations in the app.py file.

To change or add new sounds, replace the sound files in the project directory and update the soundboard logic in app.py.
