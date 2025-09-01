from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#
# Abstract Base Class for Multivariate Analysis
# ----------------------------------------------
# This class defines a template for performing multivariate analysis.
# Subclasses can override specific steps like correlation heatmap and pair plot generation.

class MutlivariateAnalysisTemplate(ABC):
    def analyze(self,df:pd.DataFrame):
        """
        Perform a comprehensive multivariate analysis by generating a correlation heatmap and pair plot.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.

        Returns:
        None: This method orchestrates the multivariate analysis process.
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)
    @abstractmethod
    def generate_correlation_heatmap(df:pd.DataFrame):
        """
        Generate and display a heatmap of the correlations between features.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.

        Returns:
        None: This method should generate and display a correlation heatmap.
        """
        pass
    @abstractmethod
    def generate_pairplot(df:pd.DataFrame):
        """
        Generate and display a pair plot of the selected features.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.

        Returns:
        None: This method should generate and display a pair plot.
        """
        pass

#Concrete class for Multivariate Analysis with Correlation Heatmap and Pair Plot

#This class implements the methods to generate a correlation heatmap and a pairplot

class SimpleMultivariateAnalysis(MutlivariateAnalysisTemplate):
    def generate_correlation_heatmap(df:pd.DataFrame):
        # return super().generate_correlation_heatmap()
        """
        Generates and displays a correlation heatmap for the numerical features in the DataFrame

        Parameter:
        df(pd.DataFrame): The dataframe containing the data to be analyzed

        Returns:
        None: Displays a heatmap showing correlations between numerical features.
        """
        plt.figure(figsize=(12,10))
        sns.heatmap(df.corr(),annot=True,fmt=".2f",cmap="coolwarm",linewidth=0.5)
        plt.title("Correlation Heatmap")
        plt.show()
    
    def generate_pairplot(df):
        # return super().generate_pairplot()
        """
        Generates and displays a pair plot for the selected features in the dataframe.

        Parameters:
        df (pd.DataFrame): The dataframe containing the data to be analyzed.

        Returns:
        None: Displays a pair plot for the selected features.
        """
        sns.pairplot(df)
        plt.suptitle("Pair Plot of Selected Features",y=1.02)
        plt.show()
        
# Example usage
if __name__ == "__main__":
    # Example usage of the SimpleMultivariateAnalysis class.

    # Load the data
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Perform Multivariate Analysis
    # multivariate_analyzer = SimpleMultivariateAnalysis()

    # Select important features for pair plot
    # selected_features = df[['SalePrice', 'Gr Liv Area', 'Overall Qual', 'Total Bsmt SF', 'Year Built']]

    # Execute the analysis
    # multivariate_analyzer.analyze(selected_features)
    pass