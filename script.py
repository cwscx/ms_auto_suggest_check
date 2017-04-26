#!/usr/bin/env python

import sys
import os
import re

def error_msg(msg):
	print("Error: ", msg)
	sys.exit(-1)

if __name__ == "__main__":
	config_path = os.path.relpath("config")
	cwd = os.getcwd()

	if not os.path.exists(config_path):
		error_msg("No config file in the directory")

	# Get all the configuration parameters
	config_dict = {}
	with open(config_path, "r") as config_file:
		for line in config_file:
			matches = re.split("\s*:\s*", line)
			config_dict[matches[0].strip()] = matches[1].strip()

	# Direct MS autosuggestion's output to file "1"
	predict_py_exec_cmdl = "python predict.py " + config_dict["ms_key"] + " " + config_dict["word"] + " > 1"
	os.system(predict_py_exec_cmdl)
	
	
	# process:
	# 1. Make -C [PA_dir] clean
	# 2. rename [PA_dir]/Makefile -> [PA_dir]/Makefile_cp
	# 3. cp [AS]/Makefile -> [PA_dir]/Makefile
	# 4. Make -C [PA_dir]
	# 5. [PA_dir]/predict min_size step_size iter_time dict_name + word + num_completion > 2
	# 6. Make -C [PA_dir] clean
	# 7. rm [PA_dir]/Makefile
	# 8. mv [PA_dir]/Makefile_cp [PA_dir]/Makefile
	pa_path = config_dict["pa_absolute_dir"]
	pa_makefile_path = pa_path + "/Makefile"
	
	clean_pa_dir = "make -C " + pa_path + " clean"
	os.system(clean_pa_dir)

	rename_pa_makefile = "mv " + pa_makefile_path + " " + pa_makefile_path + "_cp"
	os.system(rename_pa_makefile)

	cp_new_makefile = "cp Makefile " + pa_path
	os.system(cp_new_makefile)

	make_predict = "make -C " + pa_path
	os.system(make_predict)

	run_pa_predict = pa_path + "/predict " + config_dict["min_size"] + " " + \
	config_dict["step_size"] + " " + config_dict["iter_time"] + " " + \
	config_dict["dict_absolute_dir"] + " " + config_dict["word"] + " " + \
	config_dict["num_completion"] + " > 2"
	os.system(run_pa_predict)

	os.system(clean_pa_dir)
	
	rm_new_makefile = "rm " + pa_makefile_path
	os.system(rm_new_makefile)

	restore_makefile = "mv " + pa_makefile_path + "_cp " + pa_makefile_path
	os.system(restore_makefile)