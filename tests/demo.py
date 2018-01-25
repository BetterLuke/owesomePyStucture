import click

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@click.command()
@click.confirmation_option(prompt="are u sure?", callback=abort_if_false)
def dropdb():
    click.echo('Dropped all tables!')

dropdb()
