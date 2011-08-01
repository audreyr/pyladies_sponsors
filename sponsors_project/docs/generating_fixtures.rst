===================
Generating fixtures
===================

Create something like sponsors/fixture_gen.py.

Then run something like this::

	cd sponsors_project
	python manage.py generate_fixture sponsors.test_sponsors > sponsors/fixtures/initial_data.txt
	cd sponsors/fixtures/
	mv initial_data.txt initial_data.json
	cd ../../
	python manage.py syncdb --noinput
	python manage.py migrate
	python manage.py runserver