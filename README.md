# Olx offer crawler

Crawler to extract all worthy data about offers and put it into the database. It also has a web server to comfortably check the offers.

## Requirements

Check the `requirements.txt`

## Install dependencies

To install necessary modules, run

```zsh
pip install --user -r requirements.txt
```

## URLS

The `URLS` file should contain URLs of a search request. When you search something on OLX  it opens a page with offers, copy the URL to `URLS` file

Every crawler run will bring to you the newest offers to your database

##  Run crawler

To start the crawler run

```zsh
python run_crawler.py
```

It will read the URLs from the `URLS` file and crawl them.

## Check the offers

Run the web server 

```zsh
python run_server.py
```

It will start the server, go to `localhost:5000` to open the web.

## Modify the web engine

Crawler use the `PhantomJS` [driver](https://github.com/blooser/olxoffercrawler/blob/master/olxoffercrawler/crawler.py#L16) default. Feel free to change it for something other. 

For more go to https://www.seleniumhq.org/projects/webdriver/.

## Copyright

Blooser 
