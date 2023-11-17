import pandas as pd

class Processor():
    
    def __init__(self, data=[]) -> None:
        self.data = data


    # Convert a list to a dataframe
    def convert_to_dataframe(self, data):
        post_df = pd.DataFrame(columns=data[0].keys(), 
                               index=range(len(data)), 
                               data=data)
        return post_df
    

    # Read csv file
    def read_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
        except FileNotFoundError:
            print("File not found.")


    # Filter useful columns
    def filter_column(self):
        raw_df = self.convert_to_dataframe()
        filter_df = raw_df[['post_id', 'text', 'time',
                            'timestamp', 'image', 'post_url']]
        return filter_df
