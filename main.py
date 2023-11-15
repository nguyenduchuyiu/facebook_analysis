from CrawlModule import Crawler
from PreProcessingModule import Processor

FANPAGE_PATH = 'insightmatlong' 

def main():
    fb_crawler = Crawler()
    post_data = fb_crawler.get_post_data(fanpage_path=FANPAGE_PATH, page_number=50)

    fb_processor = Processor(post_data=post_data)
    post_df = fb_processor.convert_to_dataframe()

    path = "Data/" + FANPAGE_PATH + '.csv'
    post_df.to_csv(path, index=False) 
main()