def google_search(url):
    return "https://www.google.it/search?q={}".format(url)


def urls_from_file(filename):
    with open(filename) as f:
        urls = [google_search(url.strip()) for url in f.readlines()]
    return urls
