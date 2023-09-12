import requests
from bs4 import BeautifulSoup
webhook_url = 'https://discord.com/api/webhooks/1147838120084115526/q7aP3YKBUNNJYrfTXWDP8a0DaN_iZbzXLK7dv6zUx5FgbRQltfNc-igrCsH9jkRWpDkr'
newspapers = [
    {
        'name': 'O Jogo',
        'url': 'https://www.vercapas.com/capa/o-jogo.html',
    },
    {
        'name': 'Record',
        'url': 'https://www.vercapas.com/capa/record.html',
    },
    {
        'name': 'A Bola',
        'url': 'https://www.vercapas.com/capa/a-bola.html',
    },
]
def send_newspaper_cover(newspaper):
    response = requests.get(newspaper['url'])
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        image_element = soup.find('img', {'alt': newspaper['name']})

        if image_element:
            image_url = image_element['src']

            payload = {
                'content': f'Capa de hoje do jornal {newspaper["name"]}:',
                'embeds': [
                    {
                        'image': {'url': image_url}
                    }
                ]
            }

            response = requests.post(webhook_url, json=payload)

            if response.status_code == 204:
                print(f'{newspaper["name"]} cover sent successfully')
            else:
                print(f'Failed to send {newspaper["name"]} cover. Status code: {response.status_code}')
        else:
            print(f'Image not found on {newspaper["name"]} webpage')
    else:
        print(f'Failed to fetch {newspaper["name"]} webpage. Status code: {response.status_code}')

for newspaper in newspapers:
    send_newspaper_cover(newspaper)
