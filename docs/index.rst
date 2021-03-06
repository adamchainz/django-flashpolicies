django-flashpolicies |version|
==============================

This application enables simple management of Flash cross-domain
policies (which are required for Flash content to access information
across domains) for `Django <https://www.djangoproject.com/>`_-powered
sites. Cross-domain policies are represented by an XML file format,
and this application generates and serves the appropriate XML.

In many cases, the same policy file will also be understood by
Microsoft's Silverlight browser plugin, which supports the Adobe Flash
format as a fallback in the absence of a file in its own native
cross-domain policy format.

In the simplest case, you'll just set up one URL pattern, pointing the
URL ``/crossdomain.xml`` to the view
:func:`flashpolicies.views.simple` and passing a list of domains from
which you want to allow access. For example, to allow access from
Flash content served from ``media.example.com``, you could place the
following in the root URLconf of your Django site (along with the
appropriate ``import`` statement to make :mod:`flashpolicies.views`
available):

.. code-block:: python

    url(r'^crossdomain.xml$',
        flashpolicies.views.simple,
        {'domains': ['media.example.com']}),

Documentation contents
----------------------

.. toctree::
   :maxdepth: 1

   install
   views
   policies
   faq

.. seealso::

   * `Overview of cross-domain policy files <http://kb2.adobe.com/cps/142/tn_14213.html>`_
   * `Policy file format specification <http://www.adobe.com/devnet/articles/crossdomain_policy_file_spec.html>`_
   * `Adobe's recommendations for use of Flash cross-domain policies <http://www.adobe.com/devnet/flashplayer/articles/cross_domain_policy.html>`_
   * `Microsoft's documentation on support in Silverlight for cross-domain requests <https://msdn.microsoft.com/en-us/library/cc645032(v=vs.95).aspx>`_
