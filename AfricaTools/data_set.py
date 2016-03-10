import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


class DataSet(object):
    """Class representing a collection of stations."""

    def __init__(self):
        self.df = None

    def read(self, filename):
        """Reads dataset into a Pandas frame from a csv file.
        :param filename: csv filename.
        :type filename: str
        """

        # Read.
        self.df = pd.read_csv(filename)

        # Original file actually has a lot more data. Extract Africa.
        self.df = self.df[(self.df.Longitude > -30) & (self.df.Longitude < 60)]
        self.df = self.df[(self.df.Latitude > -45) & (self.df.Latitude < 45)]

    def plot(self):
        """
        Uses basemap to plot stations.
        :return:
        """

        lat = self.df.loc[:, "Latitude"].as_matrix()
        lon = self.df.loc[:, "Longitude"].as_matrix()

        image = Basemap(projection="ortho", lon_0=20, lat_0=5, resolution="c")
        image.drawcoastlines()
        image.fillcontinents(color="coral", lake_color="aqua")

        x, y = image(lon, lat)
        image.plot(x, y, "bo")
        plt.show()
