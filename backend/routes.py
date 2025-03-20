from flask import Blueprint, jsonify, request

from parser import mcdonalds_menu, wendys_menu

routes = Blueprint("routes",__name__)


@routes.route("/mcdonalds",methods=["GET"])
def get_mcdonalds_menu():
    force_refresh = request.args.get('refresh','false').lower() =='true'
    print(force_refresh)
    return jsonify(mcdonalds_menu(force_refresh))

@routes.route("/wendys", methods=["Get"])
def get_wendys_menu():
    force_refresh = request.args.get('refresh','false').lower() =='true'
    return jsonify(wendys_menu(force_refresh))