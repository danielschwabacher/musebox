import click

@click.command()
@click.option('--properties', default="properties.txt", help='Location of the configuration file which MuseBox should use.')

def run_from_cli(properties):
    click.echo("MuseBoxPy v0.0.1, using properties: " + properties)

if __name__ == '__main__':
    run_from_cli()