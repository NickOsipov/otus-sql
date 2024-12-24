"""
File: tasks.py
Description: This file contains the tasks that can be run using the invoke command.
"""

import os

from invoke import task
from invoke.context import Context

POSTGRES_PATH = os.path.join("infra", "postgres")

@task
def hello(cxt, word="World"):
    """Say hello to the world"""
    cxt.run(f"echo 'Hello {word}'")

@task
def postgres_up(cxt: Context) -> None:
    """Start the postgres container"""
    cxt.run(f"cd {POSTGRES_PATH} && docker-compose up -d")

@task
def postgres_down(cxt: Context) -> None:
    """Stop the postgres container"""
    cxt.run(f"cd {POSTGRES_PATH} && docker-compose down")
