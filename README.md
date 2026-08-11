# Browser Credentials Extractor
## What this code does

This repository contains a single Python script, `main.py`, which is designed to locate and extract saved browser login credentials from Windows user profiles for several Chromium-based browsers.

The script attempts to:
- ensure required Python packages are present by creating `requirements.txt` and installing missing dependencies if needed
- read Chrome/Edge/Opera GX/Brave encrypted browser credentials stored on disk
- decrypt stored passwords using Windows DPAPI and browser encryption keys
- write extracted credentials to a local log file named `cl.log`
- upload the generated log file and a `cl.log` attachment to a Discord webhook
- present a decoy fake system repair interface after execution

## What it is made to do

The script is built to behave like a simple browser credential grabber and an appearance-based system tool. It contains two main modes of operation:

1. `main()`
   - removes any existing `requirements.txt`
   - builds a list of supported Chromium browsers and their Windows profile paths
   - for each browser, attempts to locate the local state file and login database
   - decrypts stored login credentials and logs them to `cl.log`
   - sends the log file to a hard-coded Discord webhook

2. `Decoy()`
   - simulates a fake system repair process with status messages
   - prints a banner and fake scan/fix results
   - offers a prompt to continue or exit, though the script’s real activity has already occurred before this decoy

## Key implementation details

- `ec_key()` extracts the browser encryption key from a browser `Local State` JSON file.
- `dp()` decrypts Chromium password blobs using either AES-GCM with the browser key or Windows DPAPI.
- `bp()` scans browser profiles, copies the `Login Data` SQLite database, and extracts credentials from the `logins` table.
- The script uses `tempfile.NamedTemporaryFile` to create a temporary copy of the database and `sqlite3` to query it.
- A Discord webhook URL is hard-coded in the source.
- The script imports `requests`, `termcolor`, `pywin32`, and `pycryptodome`.

## Warnings and disclaimer

- This code is dangerous and resembles credential theft behavior.
- It is not well-written or safe for real-world use.
- It is not recommended to execute this script on any system other than a controlled test environment.
- The author is not liable for how anyone uses or modifies this code.

## Current limitations and concerns

- The script will delete and recreate `requirements.txt` without preserving existing contents.
- It uses hard-coded browser paths and a hard-coded Discord webhook URL.
- It assumes the environment is Windows and that the required modules can be installed automatically.
- It lacks any proper error reporting beyond simple exception handling.
- The `Decoy()` functionality is only cosmetic and does not repair anything.

## Author / GitHub

- GitHub: https://github.com/Kilovfhh

---

**Note:** This README documents the script behavior factually. It does not endorse using or spreading malicious code.
