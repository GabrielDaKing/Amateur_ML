import sys
sys.path.insert(1, 'amateur_ml')
from data.c_data import weather


class NBayes:
    """
    A class to handle the basic training and pridiction capability
    of a Naive Bayes Classification model while.
    """
    def __init__(self, data, indept_col = -1) -> None:
        self.data = data
        if indept_col == -1:
            self.indept_col = len(self.data[0]) - 1
        else:
            self.indept_col = indept_col

        self.class_var = dict()

        for i in range(len(self.data)):
            if (self.data[i][self.indept_col]) in self.class_var:
                self.class_var[self.data[i][self.indept_col]] += 1
            else:
                self.class_var[self.data[i][self.indept_col]] = 1

        self.model = dict()

        self.train()

    def train(self):

        for j in range(len(self.data[0]) - 1):
            if j != self.indept_col:

                vals = set()

                for i in range(len(self.data)):

                    vals.add(self.data[i][j])
                
                    if (str(self.data[i][j] + '|' + self.data[i][self.indept_col])) in self.model:
                        self.model[str(self.data[i][j]) + '|' + str(self.data[i][self.indept_col])] += 1
                    else:
                        self.model[str(self.data[i][j]) + '|' + str(self.data[i][self.indept_col])] = 1

                for item in vals:
                    for key, value in self.class_var.items():

                        if (str(item) + '|' + str(key)) in self.model:
                            self.model[str(item) + '|' + str(key)] /= value


    def predict(self, new_data):
        
        result = dict()
        total = 0

        for item in self.class_var.keys():
            temp = 1
            for data in new_data:
                temp *= self.model[str(data)+'|'+item]
            temp *= self.class_var[item]
            result[item] = temp
            total += temp

        for item in result.keys():
            result[item] = result[item]/total

        return max(result, key=result.get), result[max(result, key=result.get)]

    def __repr__(self) -> str:

        result = ''

        for key, value in self.model.items():
            result += 'P(' + str(key) + ')' + ': ' + str(round(value,3)) + '\n'

        return result

def test():
    data = weather

    model = NBayes(data)

    print(model)

    new_data = ["Sunny", "Hot", "Normal", "False"]
    print(model.predict(new_data))

if __name__=="__main__":
    test()



                        

            

                    


            



