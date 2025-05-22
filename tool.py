import requests

def shorten_link(full_link, link_name):
    API_KEY = '18a8ec884aa34aa71b452ba1e0688be0'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {
        'key': API_KEY,
        'short': full_link,
        'name': link_name
    }

    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')  # Just for spacing

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title:', title)
        print('Link:', short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)


# Get input from the user
link = input('Enter a link: >> ')
name = input('Link name: >> ')

# Call the function with user input
shorten_link(link, name)