from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("td",{"class":"titleColumn"})
rating_containers=page_soup.findAll("td",{"class":"ratingColumn imdbRating"})


container = containers[0]
rating_container = rating_containers[0]
film_name = "films_details.csv"
f = open(film_name,"w")
header = "film_name,casting,release_year\n"
f.write(header)


for container in containers:
	film_name = container.a.text
	film_cast = container.a["title"]
	release_year = container.span.text
	f.write(film_name + "," + film_cast.replace(",","|") + "," + release_year + "\n")
	print("casting     :" + film_cast)
	print("release_year:" + release_year)




