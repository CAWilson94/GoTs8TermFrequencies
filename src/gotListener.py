from tweepy import Stream 
from tweepy.streaming import StreamListener 


class GoTListener(StreamListener): 

    def on_data(self, data): 
        try: 
            with open('output_files/example_file.json', 'a') as f: 
                f.write(data)
                return True
        except BaseException as e: 
            print('Error on_data: {}'.format(e))

    def on_error(self, status): 
        print(status)
        return True 

