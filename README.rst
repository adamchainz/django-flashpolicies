.. -*-restructuredtext-*-

.. image:: https://travis-ci.org/ubernostrum/django-flashpolicies.svg?branch=master
    :target: https://travis-ci.org/ubernostrum/django-flashpolicies

This application enables simple Flash cross-domain access policies for
`Django <https://www.djangoproject.com>`_ sites. For example, the
following URL pattern is all you'd need to set up cross-domain access
for Flash files served from your media server::

    url(r'^crossdomain.xml$',
        'flashpolicies.views.simple',
        {'domains': ['media.yoursite.com']}),

Various other views are included, handling other common and
not-so-common cases, as well as utilities for generating custom
cross-domain policies.

Full documentation for all functionality is also included and
`available online
<http://django-flashpolicies.readthedocs.org/>`_.
