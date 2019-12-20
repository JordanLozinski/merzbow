#!usr/bin/env python3
"""Handles CLI and spins up Crawlers."""
import json
import os
from pathlib import Path
import click
from crawlers import Crawler
from crawlers.CTYPES import CTYPES

@click.command()
@click.option('-o', '--output_dir', default="output/", type=click.Path(file_okay=False, writable=True), help="Directory to output videos to.")
@click.argument('filepath', type=click.Path(exists=True))
def merzbow(filepath, output_dir):
    """
    Spins up the appropriate Crawler for the specified query(ies).
    Arguments:
        filepath: Path to a query file or directory of query files.
        output_dir: The directory to spit video/audio files out to. (Defaults to output/)
    """
    paths = set()
    filepath = Path(filepath)
    output_dir = Path(output_dir)

    if not output_dir.exists():
        os.mkdir(output_dir)


    if filepath.is_dir():
        for querypath in filepath.iterdir():
            paths.add(querypath)
    else:
        paths.add(filepath)

    for path in paths:
        with path.open('r') as f:
            query = json.loads(f.read())
            if "CRAWLER_TYPE" not in query:
                raise KeyError("CRAWLER_TYPE needs to be specified in %s" % path.as_posix())
            if query["CRAWLER_TYPE"] not in CTYPES:
                raise KeyError("Invalid CRAWLER_TYPE specified in %s" % path.as_posix())
            crawler = CTYPES[query["CRAWLER_TYPE"]](query, output_dir)
            # Pass it off to a separate thread?

