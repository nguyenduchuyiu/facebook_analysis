from CrawlModule import Crawler
from PreProcessingModule import Processor

FANPAGE_PATH = 'insightmatlong' 
PAGE_NUMBER = 10
file_path = "Data/" + FANPAGE_PATH + '.csv'

# Crawl data
def craw():
    # Initialize 
    fb_crawler = Crawler()
    fb_processor = Processor()

    # Get post data
    post_data = fb_crawler.get_post_data(fanpage_path=FANPAGE_PATH, page_number=PAGE_NUMBER)

    # Convert post data from a list to a dataframe
    post_data_df = fb_processor.convert_to_dataframe(data=post_data)

    # Write post data into a csv file for later usage
    post_data_df.to_csv(file_path, index=False) 


# Pre-Process data
def preProcess():
    fb_processor = Processor()

    # Read data from a csv file
    fb_processor.read_data(file_path=file_path)



def main():
    # craw()
    preProcess()


main()