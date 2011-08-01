from fixture_generator import fixture_generator

from sponsors.models import Sponsor

@fixture_generator(Sponsor)
def test_sponsors():
	cars = Sponsor.objects.create(name="Cars.com", slug="cars-dot-com", 
	homepage_link="http://www.cars.com", 
	careers_link="http:www.newcars.com/about/", 
	short_description="Cars.com provided food, drinks, and mentoring at the LA PyLadies' Django Day workshop on July 23, 2011.",
	description="<p>Cars.com provided food, drinks, and mentoring at the LA PyLadies' Django Day workshop on July 23, 2011.</p><p>Many of the Cars.com developers are also active participants in IRC channel #pyladies and at various LA PyLadies events.</p>", 
	category="IK")
