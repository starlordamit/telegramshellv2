import os

TOKEN = os.environ.get("1804803062:AAEtGz4iN-_7VXqHSgR6jwzE_dHk4qzrSuo", '')

ENABLED_USERS = os.environ.get("1188151881", '')
ENABLED_USERS = {1188151881}

CMD_WHITE_LIST = {}
CMD_BLACK_LIST = {'rm'}
CMD_BLACK_CHARS = {';', '\n'}
ONLY_SHORTCUT_CMD = False

MAX_TASK_OUTPUT = int(os.environ.get("MAX_TASK_OUTPUT", 500))

PROXY_URL = os.environ.get("ALL_PROXY", '')

SC_MENU_ITEM_ROWS = (
    (
        ('pwd', 'pwd'),  # display name, command, is script
        ('ls', 'ls'),
        ('ls -lh', 'ls -lh'),
    ),
    (
        ('ls -lha', 'ls -lha'),
        ('Demo Script', 'demo.py', True),
    ),
)

SC_MENU_ITEM_CMDS = {}
for row in SC_MENU_ITEM_ROWS:
    for cmd in row:
        SC_MENU_ITEM_CMDS[cmd[1]] = cmd

REQUEST_KWARGS = {
    'proxy_url': PROXY_URL
}

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPTS_ROOT_PATH = os.path.join(ROOT_PATH, 'scripts')
