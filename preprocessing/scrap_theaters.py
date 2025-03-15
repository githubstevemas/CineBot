import json

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "referer": "https://www.allocine.fr/seance/salle_gen_csalle=P0057.html",
    "referrerPolicy": "strict-origin-when-cross-origin"
}

BODY = {
    "filters": []
}


def get_towns_theaters(towns_urls):

    theaters_datas = []

    for town_url in towns_urls:

        response = requests.get(town_url)
        main_soup = BeautifulSoup(response.text, "html.parser")

        try:
            town_title = main_soup.find('div', class_='titlebar-title titlebar-title-xl').text
            town_name = town_title.split(" à ")[-1].strip()

            theaters_containers = main_soup.find_all('div', class_='meta meta-theater')

            for theater in theaters_containers:

                theater = theater.find('h2', class_='title')

                theater_title = theater.text.strip()
                theater_url = theater.find('a')['href']
                theater_ref = theater_url[-10:-5]

                # print(f"{theater_title} : {theater_ref}")

                theater_data = {
                    "town-name": town_name,
                    "theater-name": theater_title,
                    "theater-ref": theater_ref
                }

                theaters_datas.append(theater_data)

        except Exception as e:
            print(f"ERROR : {e} for url : {town_url}")

    return theaters_datas


def get_towns_urls(town_containers):

    towns_urls_list = []

    for container in town_containers:

        towns_urls_containers = container.find_all('a', class_='titlebar-link')

        for town in towns_urls_containers:
            towns_urls_list.append(f"https://www.allocine.fr{town['href']}")

    return towns_urls_list


def get_towns_containers(departments_urls):

    towns_urls_list = []

    for url in departments_urls:
        response = requests.get(url)
        main_soup = BeautifulSoup(response.text, "html.parser")

        hred_containers = main_soup.find_all('div', class_='hred')
        towns_containers = []

        for container in hred_containers:
            if container.get("class") == ["hred"]:
                towns_containers.append(container)

        towns_urls_list.extend(get_towns_urls(towns_containers))

    return towns_urls_list


def get_departments_urls(main_url):

    response = requests.get(main_url)
    main_soup = BeautifulSoup(response.text, "html.parser")

    departement_container = main_soup.find_all('div', class_='mdl-more gd small-crop')[1]
    departments = departement_container.find_all('a', class_='mdl-more-item')

    departments_list = []

    for department in departments:
        departments_list.append(f"https://www.allocine.fr{department['href']}")

    return departments_list


def scrap_theaters():
    departements = get_departments_urls("https://www.allocine.fr/salle/")
    towns_urls_list = get_towns_containers(departements)

    theaters_datas = get_towns_theaters(towns_urls_list)

    with open('data/theaters_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(theaters_datas, json_file, ensure_ascii=False, indent=4)
