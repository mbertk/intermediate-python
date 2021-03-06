"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    # open the file
    with open(neo_csv_path) as  csv_file:
        neos = set()
        # read with dictreader -> iterate over
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            neos.add(NearEarthObject(row['pdes'], row['pha'] == 'Y', row['name'], row['diameter']))
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cads = set()
    # open file
    f = open(cad_json_path)
    # get dict from json object
    dict = json.load(f)

    # find indices of data
    indices = {}
    data = ['des', 'cd', 'dist', 'v_rel']
    for element in data:
        indices[element] = dict['fields'].index(element)

    for row in dict['data']:
        cads.add(CloseApproach(row[indices['des']], row[indices['cd']],
                               row[indices['dist']], row[indices['v_rel']]))

    return cads
