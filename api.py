from fastapi import FastAPI
import feedparser

app = FastAPI()

# Lista de feeds RSS
RSS_FEEDS = {
    "InfoMoney": "https://www.infomoney.com.br/feed/",
    "Exame": "https://exame.com/feed/"
}

# Função para buscar as notícias
def ler_rss(url):
    feed = feedparser.parse(url)
    noticias = []
    for post in feed.entries:
        noticias.append({
            "titulo": post.title,
            "link": post.link,
            "descricao": post.description
        })
    return noticias

# Rota para pegar notícias de um site específico
@app.get("/noticias/{site}")
def pegar_noticias(site: str):
    if site in RSS_FEEDS:
        return {"site": site, "noticias": ler_rss(RSS_FEEDS[site])}
    return {"erro": "Site não encontrado"}

# Rota para listar todos os sites disponíveis
@app.get("/sites")
def listar_sites():
    return {"sites_disponiveis": list(RSS_FEEDS.keys())}

