from selenium import webdriver
from bs4 import BeautifulSoup as bsoup
import time


def scroll_page(driver, pixel=1500, tempo=1.5, qt_scrolls=10):
    print('Aguarde...')
    SCROLL_PAUSE_TIME = tempo
    # Get scroll height
    carregar = qt_scrolls
    x = 0
    y = pixel
    
    for i in range(carregar):
        # Scroll down to bottom
        time.sleep(SCROLL_PAUSE_TIME)
        driver.execute_script(f"window.scrollTo({str(x)}, {str(y)});")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        x = y
        y += 1500
    
        get_news()
        
    try:
        ffox.close()
        ffox.exit()
    except:
        pass

def get_news():
    global ffox, lista_links
    page_yt = ffox.page_source

    with open('pagesource.html', mode='w+', encoding='utf-8') as page:
        page.write(ffox.page_source)

    soup = bsoup(page_yt, features='lxml')
    for a in soup.find_all('a', href=True):
        if '/watch?v=' in a['href']:
            lista_links.append(a['href'])

def start_ripping(canal, qt_scrolls, tempo_scr):
    global ffox, lista_links
    yt_channel = canal # sort popularity
    lista_links = list()

    ffox = webdriver.Firefox()
    ffox.get(yt_channel)

    scroll_page(driver=ffox, pixel=1500, tempo=tempo_scr, qt_scrolls=qt_scrolls)

    print(f'Encontramos: {len(lista_links)} elementos')

    lista_links = list(set(lista_links))
    print(f'Encontramos: {len(lista_links)} elementos únicos')

    with open('links_canal.txt', mode='w+', encoding='utf-8') as lnks:
        for lnk in lista_links:
            lnks.write(f'https://www.youtube.com/{lnk}\n')

    print('Salvao em um .txt chamado: links_canal.txt')

start_ripping(canal='https://www.youtube.com/c/ODESZA/videos', qt_scrolls=20, tempo_scr=0.5)
# canal = link do canal
# qt_scrolls = quantas vezes irá rolar a página
# tempo = depois uma rolada (rs) de página, quanto tempo irá esperar para rolar mais uma vez :D
