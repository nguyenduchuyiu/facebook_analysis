import pandas as pd

class Processor():
    
    def __init__(self, post_data):
        self.post_data = post_data


    def convert_to_dataframe(self):
        post_df = pd.DataFrame(columns=self.post_data[0].keys(), 
                               index=range(len(self.post_data)), 
                               data=self.post_data)
        return post_df
    

    # Filter useful columns
    def filter_column(self):
        raw_df = self.convert_to_dataframe()
        filter_df = raw_df[['post_id', 'text', 'time',
                            'timestamp', 'image', 'post_url']]
        return filter_df
