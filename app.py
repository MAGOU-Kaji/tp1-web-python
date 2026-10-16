import csv
import sys
from pathlib import Path

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse, JsonResponse
from django.urls import path

BASE_DIR = Path(__file__).resolve().parent

settings.configure(
    DEBUG=True,
    SECRET_KEY="cle-de-developpement",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)


def accueil(request):
    html = (BASE_DIR / "releve.html").read_text(encoding="utf-8")
    return HttpResponse(html)


def style(request):
    css = (BASE_DIR / "style.css").read_text(encoding="utf-8")
    return HttpResponse(css, content_type="text/css")


def bonjour(request, ville):
    return HttpResponse(f"Bonjour depuis {ville} !")


def api_prix(request):
    with open(BASE_DIR / "prix.csv", encoding="utf-8") as f:
        lignes = list(csv.DictReader(f))
    return JsonResponse(lignes, safe=False)


urlpatterns = [
    path("", accueil),
    path("style.css", style),
    path("bonjour/<str:ville>", bonjour),
    path("api/prix", api_prix),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)