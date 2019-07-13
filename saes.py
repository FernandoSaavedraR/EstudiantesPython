import click

import controlador as clients_commands

CLIENTS_TABLE = '.alumnos.csv'
@click.group()
@click.pass_context
def cli(ctx): #ctx viene de click pass_Content
    ctx.obj = {}
    ctx.obj['alumnos'] = CLIENTS_TABLE

cli.add_command(clients_commands.all)
