import click
from data_set import DataSet


@click.group()
def cli():
    pass


# noinspection PyIncorrectDocstring
@cli.command()
@click.option("--file", type=click.Path(readable=True), help="CSV filename", required=True)
def plot_stations(filename):
    """
    Read in a saved stations file and plot it.
    """

    dataset = DataSet()
    dataset.read(filename)
    dataset.plot()
