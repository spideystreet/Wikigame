import os
import requests
from bs4 import BeautifulSoup
import random

def get_random_wikipedia_page():
    response = requests.get('https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard')
    return response.url, response.text

def extract_links(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    content_div = soup.find(id='bodyContent')
    links = content_div.find_all('a', href=True)
    return [(link.get_text(), link['href']) for link in links if link['href'].startswith('/wiki/') and ':' not in link['href']]

def display_links(links, current_page, start_index=0):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("************************ WikiGame ****")
    for i, (text, link) in enumerate(links[start_index:start_index+20], start=1):
        print(f"{i:02d} - {text}")
    if start_index > 0:
        print("98 - Page précédente")
    if len(links) > start_index + 20:
        print("99 - Page suivante")

def main():
    start_url, start_content = get_random_wikipedia_page()
    end_url, _ = get_random_wikipedia_page()
    current_url = start_url
    current_content = start_content
    history = []
    turn = 0
    start_index = 0

    while current_url != end_url:
        history.append(current_url)
        links = extract_links(current_content)
        display_links(links, current_url, start_index)

        try:
            choice = int(input("Votre choix : "))
            if choice == 98:
                start_index = max(0, start_index - 20)
            elif choice == 99:
                start_index += 20
            elif 1 <= choice <= 20:
                next_link = links[start_index + choice - 1][1]
                current_url = 'https://fr.wikipedia.org' + next_link
                current_content = requests.get(current_url).text
                turn += 1
            else:
                print("Choix invalide. Réessayez.")
        except (ValueError, IndexError):
            print("Choix invalide. Réessayez.")
        except Exception as e:
            print(f"Erreur : {e}")
            break

    print(f"Bravo! Vous avez atteint la cible en {turn} tours.")
    print("Historique des pages visitées:")
    for page in history:
        print(page)

if __name__ == '__main__':
    main()
