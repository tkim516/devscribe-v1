import ast
import json
from io import BytesIO
from flask import Flask

def extract_routes_from_ast(file_obj):
    """
    Parses a Flask application from a BytesIO object to extract route definitions using AST.

    Args:
        file_obj (BytesIO): File-like object containing the Python source code.

    Returns:
        dict: A dictionary representing OpenAPI paths and methods.
    """
    source_code = file_obj.read().decode("utf-8")  # Convert bytes to string
    tree = ast.parse(source_code)

    routes = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Extract decorator info
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call) and hasattr(decorator.func, "attr"):
                    if decorator.func.attr == "route":  # @app.route()
                        path = decorator.args[0].s if decorator.args else "/"
                        methods = ["GET"]  # Default to GET if no method specified

                        # Extract methods from decorator kwargs
                        for kw in decorator.keywords:
                            if kw.arg == "methods":
                                methods = [m.s for m in kw.value.elts]  # List of method strings

                        # Extract docstring as endpoint description
                        docstring = ast.get_docstring(node) or "No description available."

                        # Construct OpenAPI path entry
                        if path not in routes:
                            routes[path] = {}

                        for method in methods:
                            routes[path][method.lower()] = {
                                "summary": node.name,
                                "description": docstring,
                                "responses": {
                                    "200": {"description": "Success"}
                                }
                            }

    return routes


def generate_openapi_spec(file_obj, title="Flask API", version="1.0.0"):
    """
    Generates an OpenAPI specification for a Flask app from a BytesIO object.

    Args:
        file_obj (BytesIO): File-like object containing the Python source code.
        title (str): Title of the API.
        version (str): Version of the API.

    Returns:
        dict: OpenAPI specification.
    """
    paths = extract_routes_from_ast(file_obj)

    openapi_spec = {
        "openapi": "3.0.0",
        "info": {
            "title": title,
            "version": version,
            "description": "Auto-generated OpenAPI spec from Flask routes."
        },
        "paths": paths
    }
    return openapi_spec
