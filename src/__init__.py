from os.path import abspath, dirname, join

PROJECT_ROOT = abspath(dirname(__file__))

RESOURCE_PATH = join(PROJECT_ROOT, 'resources')
ASSETS_PATH = join(RESOURCE_PATH, 'assets')
SCORE_PATH = join(ASSETS_PATH, 'score')
LOG_PATH = join(PROJECT_ROOT[:-3], 'log')
