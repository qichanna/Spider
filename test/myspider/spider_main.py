import urllib

from test.myspider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParse()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 100:
                    break
                count += 1
            except:
                print('craw failed')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

    # urld ='http://v2.mukewang.com/e68ac736-375c-41b1-a79a-12f1157a595f/L.mp4?auth_key=1463405417-0-0-e18c7d1a2a491dccf3f3fceb770db606'
    # f = open('p.mp4', 'wb')
    # req = urllib.request.Request(urld, headers={'Referer': 'http://www.imooc.com'})
    # data = urllib.request.urlopen(req).read()
    # f.write(data)
    # f.close()
