# Instagram Saved Posts Downloader

Download all your Instagram saved posts in bulk — images & videos — using Python and Instaloader.
 
##  Requirements

- Python 3.x
- pip
 
## Installation

**1. Install dependencies**

```bash
pip install instaloader browser-cookie3
```

**2. Clone this repo**

```bash
git clone https://github.com/hariomop12/instagram-saved-downloader
cd instagram-saved-downloader
```

 

##  Setup — Export Browser Cookies

This script uses your browser cookies to log in (no password needed).

> ✅ Supported browsers: Firefox, Zen Browser, LibreWolf (any Firefox-based browser)

**Step 1** — Find your cookies.sqlite file:

```bash
# Firefox
~/.mozilla/firefox/XXXXXXXX.default-release/cookies.sqlite

# Zen Browser
~/.var/app/app.zen_browser.zen/.zen/XXXXXXXX.Default (release)/cookies.sqlite
```

**Step 2** — Copy it to the project folder:

```bash
cp "/path/to/your/cookies.sqlite" ./cookies.sqlite
```

**Step 3** — Open `download_saved.py` and set your Instagram username:

```python
USERNAME = "your_instagram_username"
```

---

## ▶️ Usage

> ⚠️ **Close your browser before running the script** — otherwise cookies.sqlite will be locked.

```bash
python3 download_saved.py
```

Posts will be saved in the `:saved/` folder.

---

## 📁 Project Structure

```
instagram-saved-downloader/
├── download_saved.py   # main script
├── cookies.sqlite      # your browser cookies (gitignored)
├── .gitignore
├── README.md
└── :saved/             # downloaded posts go here (gitignored)
```

---

## ⚠️ Notes

- Instagram has rate limits — the script automatically retries on errors (don't panic if you see 403 warnings)
- There is a 4 second delay between each download to avoid getting blocked
- `cookies.sqlite` and `:saved/` are in `.gitignore` — your data won't be pushed to GitHub

---

## 🛠️ Built With

- [Instaloader](https://instaloader.github.io/)
- [browser-cookie3](https://github.com/borisbabic/browser_cookie3)