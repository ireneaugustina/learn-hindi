# Learn Hindi

A simple browser-based project for learning the Hindi alphabet and practicing pronunciation of vowels and consonants.

## Overview

This project is a lightweight interactive webpage that displays Hindi letters and allows users to click each one to hear its pronunciation using the browser's speech synthesis engine. It is designed as a beginner-friendly learning tool for students who are starting to learn Hindi script.

## Features

- Interactive grid of Hindi vowels and consonants
- Click-to-hear pronunciation for each letter
- On-screen tracing practice and printable dotted worksheets for every vowel and consonant
- Romanized transliteration for easier reading
- Clean, minimal interface with no framework or build setup required
- Works as a static web page

## Project Structure

- `index.html` — main app UI, styling, and JavaScript logic
- `README.md` — project overview and usage instructions

## How to Run

You can open the app directly in a browser:

1. Open `index.html` in your browser, or
2. Serve the folder locally with a static server, for example:

```bash
python -m http.server 8000
```

Then visit:

```text
http://localhost:8000
```

Select **Practice tracing**, then select any dotted letter to trace it on screen with a mouse or touchscreen. **Done** keeps your trace on the letter card and restores it when reopened; use **Clear** to start again, or choose **Print worksheet** to practice on paper.

## Notes

- Pronunciation depends on the browser and operating system voice support.
- Chrome and Edge generally provide the best Hindi voice support.
- If a Hindi voice is not available, the page may not produce audio.

## Technologies Used

- HTML
- CSS
- JavaScript
- Web Speech API

## Purpose

This project is intended to help beginners recognize and pronounce Hindi letters in a simple, accessible way without needing a separate app or installation.