class Linear:
    """
    A class to handle the basic training and pridiction capability
    of a Linear Regression model while storing the slope and intercept.
    """
    def __init__(self):

        self.slope = 0
        self.intercept = 0

    def fit(self, x, y):
        """ 
        A function to set the slope and intercept of the line of regression i.e. fit the line to the given data.

        Args:
            x (list(float)): The independent variable values
            y (list(float)): The dependent variable values
        """

        self.slope = 0
        self.intercept = 0

        assert len(x)==len(y)

        x_sq = [i**2 for i in x]

        xy = [i*j for i,j in zip(x,y)]

        sum_x = sum(x)
        sum_y = sum(y)

        sum_x_sq = sum(x_sq)
        sum_xy = sum(xy)

        n=len(x)

        self.slope = ((n*sum_xy)-(sum_x*sum_y))/((n*sum_x_sq)-sum_x**2)

        self.intercept = ((sum_y*sum_x_sq)-(sum_x*sum_xy))/((n*sum_x_sq)-sum_x**2)

    def predict(self, x):
        """Predicts the values of the dependent variable based on the independent variable provided

        Args:
            x (list(float)): The independent variable values

        Returns:
            list(float): The predicted dependent values
        """
        
        y = [self.slope*i+self.intercept for i in x]

        return y

    def __repr__(self):

        return "Slope: "+str(self.slope)+"\nIntercept: "+str(self.intercept)
