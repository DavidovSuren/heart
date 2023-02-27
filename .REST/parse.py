import urllib.request, json

'''
31, 30
https://content.kissloveodsk.ru/wp-json/wp/v2/posts?categories=${cat}&per_page=100

http://127.0.0.1:9999/api/events/?format=json&ordering=date
'''

with urllib.request.urlopen("https://content.kissloveodsk.ru/wp-json/wp/v2/posts?categories=29&per_page=100") as url: #skip=100
    data = json.load(url)

for d in data:
    if d['acf']['openmounth'] and int(d['acf']['openmounth']) < 11 and int(d['acf']['openmounth']) > 1:
        print(d['acf']['openmounth'], d['acf']['openday'])
        print(d['title']['rendered'])
        print(d['acf']['card_content'])
        print(d['fimg_url'])
        print('---')