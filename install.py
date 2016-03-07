#!/usr/bin/python

import sys
import os
from subprocess import call
import platform

def execute(str):
	print str
	call(str.split())

install_path = "/usr/local"
x11_include_path = ""
x11_lib_path = ""

if platform.system() == "Darwin":
	x11_include_path = "-I/opt/X11/include"
	x11_lib_path = "-L/opt/X11/lib"

if len(sys.argv) == 2:
	if (sys.argv[1] == "help"):
		print "install.py = build and install"
		print "install.py clean = uninstall"
	elif (sys.argv[1] == "clean"):
		execute("rm -rf " + install_path + "/include/dlib")
		execute("rm -rf " + install_path + "/lib/libdlib.a")
		if os.path.exists("build"):
			execute("rm -rf build")
	else:
		print "Command not recognized"
	sys.exit(0)

if not os.path.exists("dlib"):
	print "Please run this inside dlib dir"
	sys.exit(0)

if os.path.exists("build"):
	execute("rm -rf build")

execute("mkdir build")
os.chdir("build")

execute("cp -R ../dlib .")
execute("g++ -O3 -c " + x11_include_path + " ./dlib/all/source.cpp -o source.o -DDLIB_JPEG_SUPPORT")
execute("ar cr libdlib.a source.o")

execute("cp -R dlib " + install_path + "/include")
execute("cp libdlib.a " + install_path + "/lib")
