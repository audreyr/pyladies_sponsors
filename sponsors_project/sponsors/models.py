from django.db import models
from django.utils.translation import ugettext_lazy as _

class Sponsor(models.Model):
    """
        Sponsor model
    """

    CATEGORY_CHOICES = (
    	('GO', 'Gold'),
    	('SI', 'Silver'),
    	('BR', 'Bronze'),
    	('IK', 'In-Kind'),
    )

    name = models.CharField(_('Name'), max_length=200)
    slug = models.SlugField()
    pub_date = models.DateField(_('Date Published'), auto_now_add=True)
    logo = models.ImageField(_('Logo'), upload_to='sponsor_logos', null=True, blank=True)
    link = models.URLField(_('Link'), null=True, blank=True)
    description = models.TextField(_('Description'), max_length=1000)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def __unicode__(self):
        return u'%s' % self.name

