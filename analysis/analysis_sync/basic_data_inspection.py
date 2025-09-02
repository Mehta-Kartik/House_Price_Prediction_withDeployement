from abc import ABC,abstractmethod
import pandas as pd
#Making Abstract class for data Inspection Strategies
#This class will define common interfaces for data inspection
#Subclass must implement the inspect method
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self,df:pd.DateOffset):
        """
        Perform a specific type of data inspection.
        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is to be performed.
        Returns:
        None: This method prints the inspection results directly.
        """
        pass

#Making Concrete Method for Data Type Inspection
class DataTypeInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts to the console.
        """
        print("\n Data Types and Non-null Counts:")
        print(df.info())

#Making Concrete Method for Summary Statistics Inspection
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df:pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints summary statistics to the console.
        """
        print("\n Summary Statistics (Numerical Features):")
        print(df.describe())
        print("\n Summary Statistics (Categorical Data)")
        print(df.describe(include=["O"]))

#Context class that uses a DataInspectionStrategy
class DataInspector:
    def __init__(self,strategy:DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy
    def set_strategy(self,strategy:DataInspectionStrategy):
        """
        Setting a new strategy for DataInspection

        Parameter:strategy that should be object of DataInspectionStratefy

        Return:
        None
        """
        self._strategy=strategy
    def execute_inspection(self,df:pd.DataFrame):
        """
        Executes the inpection using the current strategy

        Parameter:
        df(pd.Datagrame):The dataframe to be inspected

        Returns:
        None Executes the current strategy's inspection
        """
        self._strategy.inspect(df)
if __name__=="__main__":
    # Example usage of the DataInspector with different strategies.

    # Load the data
    df = pd.read_csv('D:\Project1\House Price Prediction with Deployement\OurProject\extracted_data\AmesHousing.csv')

    # Initialize the Data Inspector with a specific strategy
    inspector = DataInspector(DataTypeInspectionStrategy())
    inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    inspector.execute_inspection(df)
    pass