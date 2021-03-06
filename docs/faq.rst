.. _faq:


Frequently asked questions
==========================

The following notes answer common questions, and may be useful to you
when installing, configuring or using django-flashpolicies.


Why do I need a cross-domain policy file?
-----------------------------------------

Much like JavaScript, the Adobe Flash player by default has a
same-origin policy; a Flash player instance on one domain cannot load
data from another domain.

A cross-domain policy file allows you, as the owner of a domain, to
specify exceptions to this, allowing loading of data from another
domain (for example, if you have data hosted on a CDN).

In order to prevent security issues caused by loading data from
untrusted domains, your cross-domain policy file should permit *only*
those domains you know are trustworthy (i.e., because those domains
are under your control, and you can prevent malicious content from
being placed on them).


Why doesn't this application generate Silverlight's format?
-----------------------------------------------------------

The Microsoft Silverlight plugin has a same-origin sandbox like Flash,
and its native format for cross-domain policies is a file called
``clientaccesspolicy.xml``. However, if ``clientaccesspolicy.xml`` is
not found on the target domain, or otherwise returns an error,
Silverlight will fall back to requesting and obeying a Flash
``crossdomain.xml`` file.

This means that a single file -- ``crossdomain.xml`` in the Flash
format -- suffices for both Flash and Silverlight. Additionally,
Silverlight is no longer supported in current versions of Microsoft's
own Edge browser, support for it is in the process of being
dropped/disabled in other major browsers, and Microsoft has announced
that Silverlight will reach end-of-life in 2021, meaning that the
Silverlight-only format corresponds to an already-small and shrinking,
and soon to be nonexistent, supported base.


What versions of Django are supported?
--------------------------------------

As of django-flashpolicies |version|, Django 1.8 and 1.9 are
supported.

Older versions of Django may work, but are not supported. In
particular, the behavior of the ``APPEND_SLASH`` setting in some old
Django versions may be problematic: on very old versions of Django,
``APPEND_SLASH`` always adds a trailing slash even if the URL would
match without it. This makes it impossible to serve a master policy
file, which must have *exactly* the URL ``/crossdomain.xml``, with no
trailing slash.


What versions of Python are supported?
--------------------------------------

As of ``django-flashpolicies`` |version|, Django 1.8 and 1.9 are
supported, on Python 2.7, 3.3, 3.4 or 3.5. Although Django 1.8
supported Python 3.2 at initial release, Python 3.2 is now at its
end-of-life and ``django-flashpolicies`` no longer supports it.


Why are the elements in a different order each time I serialize my policy?
--------------------------------------------------------------------------

Internally, a :class:`~flashpolicies.policies.Policy` stores
information about permitted domains and headers in dictionaries, keyed
by domain names. The resulting XML is generated by iterating over
these dictionaries.

In older versions of Python, iteration over a dictionary would produce
the same order of keys each time provided the set of keys was
identical. Newer versions of Python include a feature, for security
purposes, known as hash randomization; this means that two
dictionaries with the same set of keys can and will at times iterate
over those keys in different orders.

Hash randomization is enabled by default on Python 3.3, and can be
enabled on older releases. If you are seeing inconsistent ordering for
``allow-access-from`` and ``allow-http-request-headers-from``
elements, it is due to hash randomization being enabled.

Since this does not affect the well-formedness or validity of the
resulting XML document, it is not a bug, and you should not attempt to
disable hash randomization in Python.


Why shouldn't I use wild-card (i.e., '*') domains in my policy?
---------------------------------------------------------------

Use of wild-card entries in a policy effectively negates much of the
security gain that comes from explicitly specifying the permitted
domains. Unless you can and do vigilantly control all possible
domains/subdomains matching a wild-card entry, use of one will expose
you to the possibility of loading malicious content.


How am I allowed to use this module?
------------------------------------

django-flashpolicies is distributed under a `three-clause BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_. This is an
open-source license which grants you broad freedom to use,
redistribute, modify and distribute modified versions of
django-flashpolicies. For details, see the file ``LICENSE`` in the
source distribution of django-flashpolicies.

.. _three-clause BSD license: http://opensource.org/licenses/BSD-3-Clause


I found a bug or want to make an improvement!
---------------------------------------------

The canonical development repository for django-flashpolicies is
online at
<https://github.com/ubernostrum/django-flashpolicies>. Issues and pull
requests can both be filed there.

