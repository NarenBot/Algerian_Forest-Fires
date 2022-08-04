import pandas as pd
import numpy as np
import math

class RandomBatchModeling:

    def outframe(list_values, input_data, scaling, model):
        # Creating random values and flooring the values 
        length = len(list_values)
        rand = np.linspace(np.random.randint(length),np.random.randint(length), input_data)
        floor = []
        for i in rand:
            floor.append(math.floor(i))
        # Getting the random rows from database
        arr = []
        for i in floor:
            arr.append(list_values[i])
        # Dataframe and making scalable to predict the model
        df = pd.DataFrame(arr)
        scaled_data = scaling.transform(df)
        output = model.predict(scaled_data)
        df['PREDICTED'] = output
        # For styling the Dataframe and writing to HTML
        myhtml = df.style.set_properties(**{'font-size':'14pt', 'font-family':'Calibri', 
        'border-collapse':'collapse', 'background-color':'black', 'color':'lawngreen', 
        'border': '2px solid brown', 'padding': '10px','border-bottom-left-radius': '25px'}).render()

        return myhtml