install:
	python3 setup.py install


clean:
	rm -rf my_ip_public.egg-info dist build my_ip_public/__pycache__ my_ip_public/providers/__pycache__/
