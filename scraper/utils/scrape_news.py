from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from scraper.models import News


class Command(BaseCommand):
    help = "Scrape news from Infobae"

    def handle(self, *args, **kwargs):
        url = "https://www.infobae.com/espana/agencias/2025/02/26/temas-del-dia-de-efe-economia-del-jueves-27-de-febrero-de-2025/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1").text.strip()
        author = (
            soup.find("a", class_="author").text.strip()
            if soup.find("a", class_="author")
            else "Desconocido"
        )
        time = soup.find("time")["datetime"] if soup.find("time") else "Desconocido"
        summary = (
            soup.find("div", class_="article-excerpt").text.strip()
            if soup.find("div", class_="article-excerpt")
            else "Resumen no disponible"
        )

        News.objects.create(title=title, author=author, time=time, summary=summary)
        self.stdout.write(self.style.SUCCESS("Noticia extraída y guardada con éxito"))
