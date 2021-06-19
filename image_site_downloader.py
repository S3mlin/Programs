#! python3
# image_site_downloader - searches for a category of photos and downloads all the resulting images

import requests, os, bs4, sys

os.makedirs('Image_downloads', exist_ok=True)
print('Searching...')
res = requests.get('http://imgur.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,features="html.parser")
image_elem = soup.select('#imagelist img')
print(list(image_elem))
if image_elem == []:
    print('There were no results of the search.')
else:
    for i in range (len(image_elem)):
        image_url = 'http:' + image_elem[i].get('src')
        print('Downloading image... %s' % image_url)
        res = requests.get(image_url)
        res.raise_for_status()
        image_file = open(os.path.join('Image_downloads', os.path.basename(image_url)), 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

print('Done.')