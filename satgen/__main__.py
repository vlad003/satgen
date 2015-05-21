import click
from . import Instance, Distribution

@click.command()
@click.option('--variables', '-n', default=5, type=int,
        help='Number of variables.')
@click.option('--clauses', '-m', default=3, type=int,
        help='Number of clauses.')
@click.option('--clause-size', '-k', default=3, type=int,
        help='The size of each clause.')
@click.option('--distribution', '-d', default="uniform",
        type=click.Choice(['uniform', 'powerlaw']),
        help='The distribution of variables amongst clauses')
def main(variables, clauses, clause_size, distribution):
    if distribution == "uniform":
        d = Distribution.uniform
    elif distribution == "powerlaw":
        d = Distribution.powerlaw

    sat = Instance(variables, clauses, clause_size, d)
    sat.generate()

    click.echo(str(sat))

if __name__ == '__main__':
    main()
