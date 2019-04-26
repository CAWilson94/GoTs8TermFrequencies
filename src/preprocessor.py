import json 

class PreProcessor (): 
    """ A sexy preprocessor to grab the parts of the data required """

    def example_output(self, file_name):
        with open(file_name, 'r') as f: 
            line = f.readline() 
            tweet = json.loads(line)
            print(json.dumps(tweet, indent=4))



