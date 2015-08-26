import click
from .instance import UniformInstance, PowerInstance

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
@click.option('--beta', '-b', default=0.5, type=float,
        help='The beta value used in the powerlaw distribution. Range [0,1]')
def main(variables, clauses, clause_size, distribution, beta):
    if distribution == "uniform":
        sat = UniformInstance(variables, clauses, clause_size)
    elif distribution == "powerlaw":
        sat = PowerInstance(beta, variables, clauses, clause_size)

    sat.generate()

    click.echo(str(sat))

if __name__ == '__main__':
    main()
