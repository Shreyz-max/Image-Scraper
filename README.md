# Image-Scraper
A flask based Image Scraper that scrapes images from google to display first five images.

This project has been deployed in **Heroku**.

To see the deployed website follow the link

(https://imagescraper101.herokuapp.com/)


## Overview of the deployemnt

### Initial Search page
[![Screenshot-from-2020-10-02-09-55-26.png](https://i.postimg.cc/BZ7JsJDx/Screenshot-from-2020-10-02-09-55-26.png)](https://postimg.cc/DmG9PkxZ)

### Shows the results
[![Screenshot-from-2020-10-02-09-56-20.png](https://i.postimg.cc/WbQjFS5z/Screenshot-from-2020-10-02-09-56-20.png)](https://postimg.cc/D8dRRQk3)

## How do I use this ? 

- Clone the repo in your terminal using :
`git clone https://github.com/Shreyz-max/Image-Scraper.git`
or download the zip file from github and extract it.

- move to the location repo is downloaded `cd ./Image-Scraper`
- run ```pip install -r requirements.txt```
- run ```python ./app.py```

It will run the development server in DEBUG mode. Go to: http://localhost:5000/ and check out the website.

## For Heroku Deployment follow these steps:

- `cd. /Image-Scraper`

- `git commit -m "Initial commit"`

- Install heroku CLI using (https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

- Register for an account

- run `heroku login`

- run `heroku git:remote -a project-name` Type the name of your project in place of project-name

- run `git push heroku master`

- To test your app (https://project-name.herokuapp.com/) follow this link where *project-name* is the name of your project.
