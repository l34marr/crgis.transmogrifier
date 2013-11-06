.. contents::

Introduction
============

crgis.transmogrifier offers custom import/export pipelines for the CRGIS project based on Transmogrifier.

Installation
============

Add this line in the eggs section of your ``buildout.cfg``::

    eggs =
        ...
        plone.app.transmogrifier
        collective.transmogrifier
        transmogrify.sqlalchemy
        crgis.transmogrifier

    zcml =
        ...
        plone.app.transmogrifier
        collective.transmogrifier
        collective.transmogrifier-meta
        transmogrify.sqlalchemy

