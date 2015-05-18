import click
from . import Instance, Distribution

@click.command()
@click.option('--variables', '-n', default=5, type=int,
        help='Number of variables.')
@click.option('--clauses', '-m', default=3, type=int,
        help='Number of clauses.')
@click.option('--clause-size', '-k', default=3, type=int,
        help='The size of each clause.')
def main(variables, clauses, clause_size):
    sat = Instance(variables, clauses, clause_size)
    sat.generate()

    click.echo(str(sat))

if __name__ == '__main__':
    main()
