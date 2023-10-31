from g4f.gui.server.app import app
from g4f.gui.server.backend import Backend_Api
from g4f.gui.server.website import Website

import os
import webbrowser
from argparse import ArgumentParser


def run_gui(host: str = '0.0.0.0', port: int = 80, debug: bool = False) -> None:
    config = {
        'host': host,
        'port': port,
        'debug': debug
    }

    site = Website(app)
    for route in site.routes:
        app.add_url_rule(
            route,
            view_func=site.routes[route]['function'],
            methods=site.routes[route]['methods'],
        )

    backend_api = Backend_Api(app)
    for route in backend_api.routes:
        app.add_url_rule(
            route,
            view_func=backend_api.routes[route]['function'],
            methods=backend_api.routes[route]['methods'],
        )

    if os.environ['AUTO_LAUNCH'] == 'true':
        url = f"http://127.0.0.1:{port}"
        webbrowser.open(url, new=0, autoraise=True)
    print(f"Running on port {config['port']}")

    app.run(**config)
    print(f"Closing port {config['port']}")


def gui_parser():
    parser = ArgumentParser(description="Run the GUI")
    parser.add_argument("-host", type=str, default="0.0.0.0", help="hostname")
    parser.add_argument("-port", type=int, default=os.environ['USER_PORT'], help="port")
    parser.add_argument("-debug", action="store_true", help="debug mode")
    return parser


def run_gui_args(args):
    host = args.host
    port = args.port
    debug = args.debug
    run_gui(host, port, debug)


if __name__ == "__main__":
    parser = gui_parser()
    args = parser.parse_args()
    run_gui_args(args)
