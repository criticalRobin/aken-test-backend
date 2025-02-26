from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from .models import News
from .serializers import NewsSerializer


class ScrapeNewsView(APIView):
    def get(self, request):
        url = "https://www.infobae.com/espana/agencias/2025/02/26/temas-del-dia-de-efe-economia-del-jueves-27-de-febrero-de-2025/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title_element = soup.find(
            "p", class_="paragraph", attrs={"data-mrf-recirculation": "Links inline"}
        )
        title = title_element.text.strip() if title_element else "Título no disponible"

        author_element = soup.find("span", class_="author-name")
        author = author_element.text.strip() if author_element else "Desconocido"

        date_element = soup.find("span", class_="sharebar-article-date")
        time = date_element.text.strip() if date_element else "Desconocido"

        summary_element = soup.find(
            "p", class_="paragraph", attrs={"data-mrf-recirculation": "Links inline"}
        )
        summary = (
            summary_element.text.strip() if summary_element else "Resumen no disponible"
        )

        news, created = News.objects.get_or_create(
            title=title, defaults={"author": author, "time": time, "summary": summary}
        )

        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
