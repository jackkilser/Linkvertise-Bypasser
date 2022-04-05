import requests
import webbrowser
import sys

def linkvertise_bypasser(links):
    # print(f"Dealing with links {links}")
    linkvertise_links = links
    bypasser_link = f'https://bypass.bot.nu/bypass2'

    returned_links = []
    for linkvertise_link in linkvertise_links:
        returned_links.append(requests.get(f'{bypasser_link}?url={linkvertise_link}'))
    return returned_links

try:
    arguments = sys.argv[1:]
    if len(arguments) > 0:
        # print(f"Received arguments: {arguments}")
        destinations = [i.json().get('destination') for i in linkvertise_bypasser(arguments)]
        for x,i in enumerate(destinations):
            print(f"\n{x+1} - {i}")

   
   
        sys.exit(1)
except:
    print('')