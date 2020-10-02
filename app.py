from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import os
from flask_cors import cross_origin, CORS


app = Flask(__name__)


def del_photos():
    directory = './static/pics/'
    files_to_remove = [os.path.join(directory, f) for f in os.listdir(directory)]
    for files in files_to_remove:
        os.remove(files)
    return 0


@cross_origin()
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        del_photos()
        keyword = request.form.get('search')
        image_keyword = keyword.split()
        image_word = '+'.join(image_keyword)
        k = image_word.replace('+', '')
        url = 'https://www.google.com/search?tbm=isch&q=' + image_word
        header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/43.0.2357.134 Safari/537.36"}
        link = requests.get(url)
        html = BeautifulSoup(link.text, 'html.parser')
        list_of_images = html.findAll("img", {"class": "t0fcAb"})
        list_of_image_url = [image['src'] for image in list_of_images]
        count = 1
        user_images = []
        for image_url in list_of_image_url:
            if count > 5:
                break
            else:
                store = 'static/pics/' + k + str(count) + '.jpg'
                urlretrieve(image_url, store)
                store_path = '/pics/' + k + str(count) + '.jpg'
                user_images.append(store_path)
                count += 1
        return render_template('result.html', user_images=user_images)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
