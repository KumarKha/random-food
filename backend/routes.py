from flask import Blueprint, jsonify

from parser import parse_mcdonalds_menu, parse_wendys_menu

routes = Blueprint("routes",__name__)


@routes.route("/mcdonalds",methods=["GET"])
def get_mcdonalds_menu():
    return jsonify(parse_mcdonalds_menu())

@routes.route("/wendys", methods=["Get"])
def get_wendys_menu():
    return jsonify(parse_wendys_menu())