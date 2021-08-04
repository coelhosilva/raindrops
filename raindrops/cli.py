import argparse
from pathlib import Path


__version__ = "v0.0.1"


MAP_TEMPLATE_FILES = {
    'cloudbuild_yaml.template': 'cloudbuild.yaml',
    'env_yaml.template': 'env.yaml',
    'gcloudignore.template': '.gcloudignore',
    'cloud_function_http.template': 'main.py',
    'cloud_function_pubsub.template': 'main.py',
}
COMMONS_TEMPLATE_FILES = [
    'cloudbuild_yaml.template',
    'env_yaml.template',
    'gcloudignore.template',
    'requirements.template'
]
THIS_PARENT_PATH = Path(__file__).parent
TEMPLATES = THIS_PARENT_PATH / 'templates'


def init_folder(folder_path):
    """Create a folder in case it doesn't exist."""
    folder_path = Path(folder_path)
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path


def init_file(file_path, contents):
    file_path.write_text(contents)


def init_files(path_files):
    for p in path_files:
        init_file(p[0], p[1].read_text())


def init_template_files(folder_path, function_type):
    if function_type == 'http':
        files = ['cloud_function_http.template']
    elif function_type == 'pubsub':
        files = ['cloud_function_pubsub.template']
    elif function_type == 'gcs':
        files = ['cloud_function_gcs.template']
    elif function_type == 'firestore':
        files = ['cloud_function_firestore.template']

    files += COMMONS_TEMPLATE_FILES
    paths_origin = [TEMPLATES / f for f in files]
    paths_destination = [folder_path / MAP_TEMPLATE_FILES[f] for f in files]
    paths = zip(paths_destination, paths_origin)
    init_files(paths)


def init_function_project(parsed_arguments):
    init = parsed_arguments.init
    if init == "http":
        target_folder = init_folder("function_http")
        init_template_files(target_folder, 'http')
    elif init == "pubsub":
        target_folder = init_folder("function_pubsub")
        init_template_files(target_folder, 'pubsub')


def init_arguments(parser):
    parser.add_argument(
        "-i",
        "--init",
        dest="init",
        required=False,
        type=str,
        help="Init a Cloud Function project."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"raindrops {__version__}"
    )

    return parser


def parse_arguments(parser):
    args = parser.parse_args()
    parsed_arguments = args

    return parsed_arguments


def get_appropriate_function(parsed_arguments):
    if "init" in parsed_arguments:
        function = init_function_project
    return function


def execute_commands(parsed_arguments):
    get_appropriate_function(parsed_arguments)(parsed_arguments)
    return


def main():
    parser = init_arguments(argparse.ArgumentParser(description=""))
    execute_commands(parse_arguments(parser))


if __name__ == "__main__":
    main()
