# BRACU Student Connect Helper

A small browser-based helper for BRACU Connect.

The project is designed for GitHub Pages. The public page only hosts the launcher and instructions. Course and seat information is loaded inside the already signed-in BRACU Connect tab, so BRACU session data is not stored in this repository or sent to GitHub Pages.

## Features

- Uses the current BRACU Connect login session
- No Selenium or local Python setup required
- Searches course code, faculty, day, time, room, and section
- Shows total seat, booked seat, remaining seat, and status
- Filters sections with available seats
- Refreshes live seat information without another login
- Works for the academic level returned by the current BRACU session

## Project Structure

```text
bracu-student-connect-helper/
├── .github/
│   └── workflows/
│       └── pages.yml
├── assets/
│   ├── css/
│   │   └── site.css
│   └── js/
│       └── site.js
├── bookmarklet/
│   ├── source.js
│   └── bookmarklet.txt
├── .gitignore
├── .nojekyll
├── LICENSE
├── README.md
└── index.html
```

## How It Works

1. GitHub Pages hosts the project page.
2. The project page provides a browser bookmark launcher.
3. Sign in to BRACU Connect normally.
4. Run the launcher from the BRACU Connect tab.
5. The helper reads BRACU APIs from the same signed-in origin and displays a searchable dashboard over the current page.

The helper does not ask for a BRACU password, Google password, access token, refresh token, or cookie.

## Deploy With GitHub Pages

1. Upload the project files to the repository root.
2. Open the repository on GitHub.
3. Go to **Settings > Pages**.
4. Under **Build and deployment**, select **GitHub Actions**.
5. Push or commit the files to `main`.
6. The included workflow deploys the site automatically.

The site URL will normally be:

```text
https://<github-username>.github.io/<repository-name>/
```

## Install The Launcher

1. Open the deployed GitHub Pages site.
2. Click **Copy launcher**.
3. Create a new browser bookmark.
4. Name it `BRACU Connect Helper`.
5. Paste the copied text into the bookmark's URL field.
6. Open BRACU Connect and sign in normally.
7. Click the `BRACU Connect Helper` bookmark.

## Seat Calculation

The live seat-status endpoint returns the current booked-seat count for each section.

```text
Remaining Seat = Total Seat - Booked Seat
```

Status rules:

```text
Remaining > 0   Available
Remaining = 0   Full
Remaining < 0   Overbooked
```

The **Available seats only** option shows only sections where remaining seat is greater than zero.

## Updating The Helper

Edit:

```text
bookmarklet/source.js
```

After changing it, rebuild `bookmarklet/bookmarklet.txt` by replacing line breaks with spaces while keeping the JavaScript valid. The repository currently includes both files so the deployed page works without a build step.

## Privacy

The hosted page itself does not receive BRACU session cookies or tokens. The launcher runs on `connect.bracu.ac.bd` and uses the browser's existing signed-in session to request BRACU data from BRACU.

## Disclaimer

This is an independent helper project and is not an official BRAC University application. BRAC University may change its website or API structure at any time, which can require updates to this project.
