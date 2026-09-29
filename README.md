# BRACU Course Seat Finder

A local tool for checking BRACU course seat status using the active BRACU Connect session in Chrome.

## Features

- Reuses the same Chrome session when possible
- Opens Chrome in Incognito mode
- Uses the active BRACU login session
- Reads course and seat data from BRACU Connect APIs
- Shows course, section, faculty, day, time, room, total seat, booked seat, remaining seat, and status
- Supports course search and available-seat filtering
- Keeps browser, API, data, and dashboard code separated for easier maintenance

## Project Structure

```text
bracu-seat-finder/
├── README.md
├── requirements.txt
├── .gitignore
├── settings.example.json
├── run.py
└── bracu_seat_finder/
    ├── __init__.py
    ├── browser.py
    ├── capture.py
    ├── config.py
    ├── data.py
    ├── dashboard.py
    ├── templates/
    │   └── dashboard.html
    └── static/
        ├── dashboard.css
        └── dashboard.js
```

## Requirements

- Windows
- Google Chrome
- Python 3.10 or newer
- BRACU Connect account

## Setup

Install the dependency:

```bash
pip install -r requirements.txt
```

Copy `settings.example.json` to `settings.json`, then set the BRACU student ID:

```json
{
  "student_id": 75867
}
```

`settings.json` is ignored by Git.

## Run

```bash
python run.py
```

On the first run, Chrome opens in Incognito mode. Complete the BRACU / Google SSO login in that Chrome window.

While the same Chrome window remains open, later runs reuse the same browser session.

## Seat Calculation

The live seat-status API value is treated as the current booked-seat count for each section.

```text
Remaining Seat = Total Seat - Booked Seat
```

Status rules:

- Available: remaining seat is greater than 0
- Full: remaining seat is 0
- Overbooked: remaining seat is below 0

The available-seat filter only shows rows where remaining seat is greater than 0.

## GitHub

This repository can be pushed to GitHub normally. The current version is a local browser-session application and is not intended to run directly on GitHub Pages because it depends on the user's authenticated BRACU Chrome session.
