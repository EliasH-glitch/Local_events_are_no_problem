# Local events in Olomouc. No problem #

Made this for getting specific events in Olomouc 🏙️

## How it works 🛠️ ##

- I used `GET()` to scrape the webside (for olomouc => `[Akce Olomouc](https://www.olomouc.cz/akce-kalendar)) 🤐
- **BeautifulSoup** 🍲 to get the event **data** (Name, Time/Date, Location)
- All filtered by **custom filter func**

## Output ##

- Output are all events **filtered** out and **categorized** (in my case by **location**)
- Syntax looks like this 👉👉 **Date/Time | Name | Location**

## What didnt worked out 🙅‍♀️ ##

At the beginning I wanted to use llm for the filter and categorization but the **hallucinations** were serious issues

Tried different sys prompts and models but it became **overcomplicated** for this use case

## AI usage 🤖 ##

Mainly Claude for brainstorming and optimalization of sys prompt i didn't end up using

## License 📖 ##

This project is under **MIT license**