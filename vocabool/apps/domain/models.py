from django.db import models
from django.contrib.auth.models import User
from vocabool.apps.helpers import ellipsify
from django.conf.global_settings import LANGUAGES # i18n language codes

class Vocabulary(models.Model):
    """List of userterms, owned by a user."""
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User) # TODO: editable=False
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'vocabularies'

    def __str__(self):
        return self.name

    # TODO: def count items
    def count(self):
        return self.terms.count()

# TODO: Limit languages
# TODO: Limit backwards relations with related_name='+' https://docs.djangoproject.com/en/dev/ref/models/fields/

class Term(models.Model):
    """A term in any language."""
    text = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')

    class Meta:
        unique_together = ('text', 'language') # TODO: case insensitive

    def __str__(self):
        return ellipsify(self.text)

class Clarification(models.Model):
    """A {definition, translation, list of synonyms} of a term."""
    term = models.ForeignKey(Term)
    text = models.CharField(max_length=200)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    created = models.DateTimeField(auto_now_add=True)

    # TODO: type = {definition, translation, synonyms}

    def __str__(self):
        return ellipsify(self.text)


class Userterm(models.Model):
    """
    A term that is owned by a user and belongs to a vocabulary,
    cherry picked clarification, and optional custom definition by user.
    """
    term = models.ForeignKey(Term)
    vocabulary = models.ForeignKey(Vocabulary, related_name='terms')
    created = models.DateTimeField(auto_now_add=True)
    clarifications = models.ManyToManyField(Clarification)
    custom_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return ellipsify(self.term.text)
