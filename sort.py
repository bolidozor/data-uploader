#!/usr/bin/python

import os, sys
import shutil
from time import gmtime, strftime
import config

Station = config.Station
# config.StationSpace
path = config.path
path_audio = config.path_audio
path_image = config.path_image
path_data = config.path_data
path_sort = config.path_sort
Version = config.Version


def sort(file, name):
	shutil.copy2(path+"station.cfg", path_sort+"station.cfg")
	if file=="audio":
		soubor=path+path_audio
		soubor_new=path_sort+path_audio+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"
		print "\t\t SORT.PY >>", soubor_new
		if not os.path.exists (soubor_new):
			os.makedirs(soubor_new)
		os.rename(soubor+name,soubor_new+name)
	elif file=="image":
		print "\t\t SORT.PY >>", "obr"
		soubor=path+path_image
		soubor_new=path_sort+path_image+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"+name[:+10][-2:]+"/"
		print "\t\t SORT.PY >>", soubor_new
		if not os.path.exists(soubor_new):
			os.makedirs(soubor_new)
		os.rename(soubor+name,soubor_new+name)
	elif file=="data":
		print "\t\t SORT.PY >>", "data"
		soubor=path+path_data
		soubor_new=path_sort+path_data+name[:+4]+"/"+name[:+6][-2:]+"/"+name[:+8][-2:]+"/"
		print "\t\t SORT.PY >>", soubor_new
		if not os.path.exists(soubor_new):
			os.makedirs(soubor_new)
		if not name == strftime("%Y%m%d%H", gmtime()) + "_" + Station + "_meta.dat":
			os.rename(soubor+name,soubor_new+name)
		else:
			print "\t\t SORT.PY >>", "##### Soubor: '" + strftime("%Y%m%d%H", gmtime()) + "_" + Station + ".dat" + "' byl preskocen"
			shutil.copy2(soubor+name, soubor_new+name)
		#print "\t\t SORT.PY >>", "DATUM "
	elif file=="config":
		shutil.copy2(path+name, path_sort+name)


def sortall():
	f = open('Log-RMDS-py','a')

	if not os.path.exists(path+path_audio):
		print  "\t\t SORT.PY >>", "Audio source path ", path+path_audio, " does NOT EXIST"
		f.write('SORT.PY\t||!' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' audio source path ' + path + path_audio + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path+path_data):
		print  "\t\t SORT.PY >>", "Data source path ", path+path_data, " does NOT EXIST"
		f.write('SORT.PY\t||!' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' data source path ' + path + path_data + " does NOT EXIST" +'\n')
		f.close()
		exit(0)
	if not os.path.exists(path+path_image):
		print  "\t\t SORT.PY >>", "Image source path ", path+path_image, " does NOT EXIST"
		f.write('SORT.PY\t||!' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' image source path ' + path + path_image + " does NOT EXIST" +'\n')
		f.close()
		exit(0)


	f.write('SORT.PY\t|| ' + strftime("%d %b %Y %H:%M:%S", gmtime()) + ' Zacatek Sortingu \n')
	dirList=os.listdir(path+path_audio)
	print "\t\t SORT.PY >>", "----------------------------------- Audio sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if   fname[-4:]==".wav":
			sort("audio", fname)
			print "\t\t SORT.PY >>", "++++ zvuk wav"
		elif fname[-4:]==".aux":
			print "\t\t SORT.PY >>", "++++ zvuk aux"
			sort("audio", fname)

	dirList=os.listdir(path+path_data)
	print "\t\t SORT.PY >>", "----------------------------------- Data sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if fname[-4:]==".dat":
			print "\t\t SORT.PY >>", "++++ data"
			sort("data", fname)

	dirList=os.listdir(path)
	print "\t\t SORT.PY >>", "----------------------------------- Config sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if fname[-4:]==".cfg":
			print "\t\t SORT.PY >>", "++++ config"
			sort("config", fname)

	dirList=os.listdir(path+path_image)
	print "\t\t SORT.PY >>", "----------------------------------- Image sorting"
	for fname in dirList:
		print "\t\t SORT.PY >>", fname
		if fname[-4:]==".jpg":
			print "\t\t SORT.PY >>", "++++ obrazek"
			sort("image", fname)
	f.write('SORT.PY\t||\t >> ' + strftime("%Y%m%d%H", gmtime()) + ' Konec sort.py - \n')
	f.close()

def SortSpecLab():
	list = os.listdir(config.path+config.path_data)
	for soubor in list:
		path_add = soubor[:4]+"/"+soubor[4:][:2]+"/"+soubor[6:][:2]+"/"
		print soubor + " -- " + path_add
		print soubor [:10] + "is not "+ strftime("%Y%m%d%H", gmtime())
		if not os.path.exists(config.path_sort+config.path_data+path_add):
			print "LABEL: >> Folder is NOT exist"
			os.makedirs(config.path_sort+config.path_data+path_add)
		if soubor [:10] is not strftime("%Y%m%d%H", gmtime()):
			shutil.copy2(config.path+config.path_data+soubor, config.path_sort+config.path_data+path_add+soubor)
		else:
			shutil.copy2(config.path+config.path_data+soubor, config.path_sort+config.path_data+path_add+soubor)
	global SortEnd
	SortEnd = False

def SortRadObs():
	list = os.listdir(config.path+config.path_data)
	for soubor in list:
		if soubor[:1] is not ".":
			path_local = config.path_sort+config.path_data+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"
			print path_local + soubor
			if not os.path.exists(path_local):
				os.makedirs(path_local)
			if soubor[:10] is not strftime("%Y%m%d%H", gmtime()):
				shutil.move(config.path+config.path_data+soubor, path_local+soubor)
			else:
				shutil.copy2(config.path+config.path_data+soubor, path_local+soubor)
	list = os.listdir(config.path+config.path_audio)
	for soubor in list:
	    if soubor[:1] is not ".":
		    path_local = config.path_sort+config.path_audio+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"+soubor[8:10]+"/"
		    print path_local + soubor
		    if not os.path.exists(path_local):
		        os.makedirs(path_local)
		    shutil.move(config.path+config.path_audio+soubor, path_local+soubor)
	list = os.listdir(config.path+config.path_image)
	for soubor in list:
	    if soubor[:1] is not ".":
		    path_local = config.path_sort+config.path_image+soubor[:4]+"/"+soubor[4:6]+"/"+soubor[6:8]+"/"+soubor[8:10]+"/"
		    print path_local + soubor
		    if not os.path.exists(path_local):
				os.makedirs(path_local)
		    shutil.move(config.path+config.path_image+soubor, path_local+soubor)
	list = os.listdir(config.path)
        for soubor in list:
	    print "!!!!-----! " + soubor	
            if  os.path.isfile(config.path+soubor):
		print " - file"
		path_local = config.path_sort
		shutil.copy2(config.path+soubor, config.path_sort+soubor)
	global SortEnd
	SortEnd = False



def main():
	global SortEnd
	SortEnd = True
	while SortEnd:
		try:
			if config.Version is "Bolidozor_14":
				SortSpecLab()
			elif config.Version is "RadObs_14_7":
				SortRadObs()
		except Exception, e:
			print "ERROR in SORT.PY", e

	print "\t\t SORT.PY >>", strftime("%d %b %Y %H:%M:%S", gmtime()), " Konec\n"
if __name__ == "__main__":
	main()
