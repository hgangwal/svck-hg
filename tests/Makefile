all:
	@echo "\ntesting rule for global variables..."
	python3 ../bin/svck.py -t ../tests/test_cl_gvar.sv
	@echo "\ntesting rule for variable types encapsulation in a class..."
	python3 ../bin/svck.py -t ../tests/test_cl_encap.sv
	@echo "\ntesting rule for naming sytle consistency..."
	python3 ../bin/svck.py -t ../tests/test_cl_mixed_naming.sv
	@echo "\ntesting rule for comments..."
	python3 ../bin/svck.py -t ../tests/test_comments.sv
	@echo "\ntesting rule for package encapsulation..."
	python3 ../bin/svck.py -t ../tests/test_cl_packageencapsulate_p.sv
	@echo "\ntesting rule for nested conditions..."
	python3 ../bin/svck.py -t ../tests/test_cl_nestedconditions_p.sv


