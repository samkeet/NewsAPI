import json
import requests
import sys
import utils


class News:
    '''Wrapped class to fetch news feeds.
    '''
    def __init__(self, source=''):
        self.api_key = ''
        self.news_source = source
        # self.sort_by = sort
        self.articles_host = 'https://newsapi.org/v1/articles?'
        self.source_host = 'https://newsapi.org/v1/sources?language=en'

    def my_request(self):
        '''Send a request for the newsfeed.
        '''
        # https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=
        source = 'source=' + self.news_source
        api = '&apiKey=' + self.api_key
        utils.log(api, source)
        result = requests.get(self.articles_host + source + api)
        # utils.log(type(result))
        if result.status_code == 400:
            utils.log('Invalid News Source')
            utils.enlist_sources()
        elif result.status_code == 200:
            result_json = result.text
            # utils.log(result_json)
            articles_list = json.loads(result_json)['articles']
            for each_article in articles_list:
                print(each_article['title'], '\n', each_article['url'], '\n')


if __name__ == '__main__':
    utils.load_args()
    utils.log(utils.args)
    # if utils.args.source_list and not utils.args.source and not utils.args.articles:
    #     utils.enlist_sources()
    if utils.args.articles and not utils.args.source:
        utils.log('Retry. Enter news source: \n')
    else:
        News(sys.argv[3]).my_request()
