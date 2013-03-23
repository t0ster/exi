from fabric.api import *


def exi():
    env.hosts = ["xchg.com:53"]
    env.supervisorapp = "exi.xchg.com"
    env.path = "/srv/exi.xchg.com"
    env.venv_path = "/srv/exi.xchg.com/env"
    env.user = "www-data"


def of():
    env.hosts = ["xchg.com:53"]
    env.supervisorapp = "of.xchg.com"
    env.path = "/srv/of.xchg.com"
    env.venv_path = "/srv/of.xchg.com/env"
    env.user = "www-data"


def venv(cmd):
    bin_path = "%s/bin" % env.venv_path
    return run("%s/%s" % (bin_path, cmd))


def venv_python(cmd):
    python_path = "%s/bin/python" % env.venv_path
    return run("%s %s" % (python_path, cmd))


def deploy():
    with cd(env.path):
        run("git fetch")
        run("git reset --hard origin/master")
        venv("pip install -r requirements.txt")
        run("sudo supervisorctl restart %s" % env.supervisorapp)
