from fabric.api import *
from fabric.contrib.project import rsync_project


env.host_string = 'some_user@94.75.245.143'

exclude_list = ['.*', '*.pyc', 'local_settings.*', 'fabfile.*']	



proj_path_remote = "/home/some_user/webapps/xfume/xfume"
proj_path_local = "/Users/xfu/Desktop/www/xfume_env/xfume/"

code_path_remote = "/home/some_user/webapps/xfume/xfume/xfume"
code_path_local = "/Users/xfu/Desktop/www/xfume_env/xfume/xfume/"




def sync_project():
	rsync_project(proj_path_remote,
		proj_path_local, delete=True, exclude=exclude_list)

def sync_code():
	rsync_project(code_path_remote,
		code_path_local, delete=True, exclude=exclude_list)


def start():
	run("/home/some_user/webapps/xfume/bin/start")

def stop():
	run("/home/some_user/webapps/xfume/bin/stop")

def reload_server():
	run("/home/some_user/webapps/xfume/bin/restart")


def read_log():
	run("cat /home/some_user/webapps/xfume/logs/xfume.uwsgi.log")


#-----shortcut-------
def up():
	sync_project()


def upp():
	sync_code()


def dp():
	up()
	reload_server()


def dpp():
	upp()
	reload_server()


def re():
	reload_server()







