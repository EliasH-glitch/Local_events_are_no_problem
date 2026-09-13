import requests
from bs4 import BeautifulSoup
import datetime
import time
import ollama


def scrape_scrape(date):

    api_url = f"https://www.olomouc.cz/akce-kalendar/{date.year}/{date.month:02d}/{date.day:02d}"

    headers = {"User-Agent": "Mozilla/5.0 (personal event script)"}

    response = requests.get(api_url, headers=headers)

    html_raw_response = response.text

    events = BeautifulSoup(html_raw_response, "html.parser")


    event_blocks = events.find_all("div", class_="aBox")

    for event in event_blocks:
        try:
            title = event.find("h2").text.strip()
            podnadpises = event.find_all("p", class_="podnadpis")
            time = podnadpises[0].text.strip()
            location = podnadpises[1].text.strip()

            # no DNES in output
            if "DNES" in time:
                time = time.replace("DNES", day.strftime("%A %-d. %-m."))

            event_dict = {
                "Name": title,
                "Time": time,
                "Location": location
            }

            all_events.append(event_dict)

        except AttributeError:
            print("stupid add 😆")

def filter(plugged_events):
    # no duplications
    seen = set()
    unique_events = []
    
    for thing in plugged_events:
        key = (thing["Name"], thing["Time"])
        if key not in seen:
            unique_events.append(thing)
            seen.add(key)

    # sorting by categories
    sport_locs = {"Andrův stadion", "Zimní stadion"}
    namesti_locs = {"Horní náměstí", "Dolní náměstí"}
    add_fil_names = {"Bruslení veřejnosti"}

    global wanted_events_olomouc, wanted_events_naplavka, wanted_events_flora, wanted_events_namesti, wanted_events_sport

    wanted_events_sport = []
    wanted_events_namesti = []
    wanted_events_flora = []
    wanted_events_naplavka = []
    wanted_events_olomouc = []

    for event in unique_events:
        if event["Location"] in sport_locs and not(event["Name"] in add_fil_names):
            wanted_events_sport.append(event)
        elif event["Location"] in namesti_locs and not(event["Name"] in add_fil_names):
            wanted_events_namesti.append(event)
        elif event["Location"] == "Výstaviště Flora" and not(event["Name"] in add_fil_names):
            wanted_events_flora.append(event)
        elif event["Location"] == "Olomoucká náplavka" and not(event["Name"] in add_fil_names):
            wanted_events_naplavka.append(event)
        elif event["Location"] == "Olomouc" and not(event["Name"] in add_fil_names):
            wanted_events_olomouc.append(event)
        else:
            pass

def print_it_out():

    print("Next month is 👇👇👇")

    # sporting events

    print("Sport stuff:")

    for event in wanted_events_sport:
        print(f"- {event["Time"]} | {event["Name"]} | {event["Location"]}")

    # namesti events

    print("Naměstí stuff:")

    for event in wanted_events_namesti:
        print(f"- {event["Time"]} | {event["Name"]} | {event["Location"]}")

    # flora events

    print("Flora stuff:")

    for event in wanted_events_flora:
        print(f"- {event["Time"]} | {event["Name"]} | {event["Location"]}")

    # naplavka events

    print("Náplavka stuff:")

    for event in wanted_events_naplavka:
        print(f"- {event["Time"]} | {event["Name"]} | {event["Location"]}")

    # Olomouc events

    print("General Olomouc stuff:")

    for event in wanted_events_olomouc:
        print(f"- {event["Time"]} | {event["Name"]} | {event["Location"]}")

    print("Enjoy events of next month 👍👌")

all_events = []

start = datetime.date(2026, 9, 1)
end = datetime.date(2026, 9, 30)

day = start

while day <= end:
    scrape_scrape(day)
    print(f"Scraping day: {day}")
    day += datetime.timedelta(days=1)
    time.sleep(0.5)

filter(all_events)

print_it_out()
