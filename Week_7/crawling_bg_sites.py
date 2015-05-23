import json
import requests
import bs4
import matplotlib.pyplot as plt


class Histogram():

    def __init__(self):
        self.dict = {}

    def add(self, key):
        if key not in self.dict.keys():
            self.dict[key] = 1
        else:
            self.dict[key] += 1

    def count(self, key):
        if key not in self.dict.keys():
            return None
        else:
            return self.dict[key]

    def items(self):
        lst = []
        for key in self.dict.keys():
            lst.append((key, self.dict[key]))
        return lst

    def get_dict(self):
        return self.dict


def rename_server(server):
    if 'Apache' in server:
        server = 'Apache'
    elif 'IIS' in server:
        server = 'IIS'
    elif 'nginx' in server:
        server = 'nginx'
    elif 'lighttpd' in server:
        server = 'lighttpd'
    else:
        server = 'others'

    return server


def make_request(histogram, url_preffix, url_suffix):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    r = requests.head(url_preffix + url_suffix, headers=headers, timeout=10, allow_redirects=True)
    a_server = r.headers['Server']
    a_server = rename_server(a_server)
    histogram.add(a_server)

    print(a_server)


def crawl_websites(histogram, url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text)
    index = 0
    for link in soup.select('a'):
        try:
            make_request(histogram, url, link.attrs.get('href'))
            print('Crawled ' + str(index) + ' pages')
        except Exception as e:
            print(e)
            pass
        index += 1
    print()


def main():

    h = Histogram()
    hist = Histogram()

    h.add("Apache")
    h.add("Apache")
    h.add("nginx")
    h.add("IIS")
    h.add("nginx")

    # print(h.count("Apache") == 2)  # True
    # print(h.count("nginx") == 2)  # True
    # print(h.count("IIS") == 1)  # True
    # print(h.count("IBM Web Server") is None)

    crawl_websites(hist, 'http://register.start.bg/')
    print(hist.items())

    d = hist.get_dict()
    keys = list(d.keys())
    values = list(d.values())

    X = list(range(len(keys)))

    plt.bar(X, list(d.values()), align="center")
    plt.xticks(X, keys)

    plt.title(".bg servers")
    plt.xlabel("Server")
    plt.ylabel("Count")

    plt.savefig("histogram.png")

if __name__ == '__main__':
    main()
