import xml.dom.minidom

from django.test import TestCase

from flashpolicies import policies


class PolicyGeneratorTests(TestCase):
    """
    Tests for the policy-file generation utilities.
    
    """
    def test_policy_type(self):
        """
        Test that the correct ``DOCTYPE`` declaration is generated.
        
        """
        policy = policies.new_policy()
        self.assertEqual(policy.doctype.systemId, 'http://www.adobe.com/xml/dtds/cross-domain-policy.dtd')
        self.assertEqual(policy.doctype.name, 'cross-domain-policy')
        self.assertEqual(len(policy.childNodes), 2)

    def test_policy_root_element(self):
        """
        Test that the correct root element is inserted.
        
        """
        policy = policies.new_policy()
        self.assertEqual(policy.documentElement.tagName, 'cross-domain-policy')
        self.assertEqual(len(policy.documentElement.childNodes), 0)

    def test_allow_access_domain(self):
        """
        Test that adding access for a domain inserts the proper
        element and attribute.
        
        """
        policy = policies.new_policy()
        policies.allow_access_from(policy, 'media.example.com')
        self.assertEqual(len(policy.documentElement.childNodes), 1)
        self.assertEqual(len(policy.getElementsByTagName('allow-access-from')), 1)
        access_elem = policy.getElementsByTagName('allow-access-from')[0]
        self.assertEqual(len(access_elem.attributes), 1)
        self.assertEqual(access_elem.getAttribute('domain'), 'media.example.com')

    def test_allow_access_ports(self):
        """
        Test that adding port access for socket connections inserts
        the proper attribute.
        
        """
        policy = policies.new_policy()
        ports='80,8080,9000-10000'
        policies.allow_access_from(policy, 'media.example.com', to_ports=ports)
        access_elem = policy.getElementsByTagName('allow-access-from')[0]
        self.assertEqual(len(access_elem.attributes), 2)
        self.assertEqual(access_elem.getAttribute('to-ports'), ports)

    def test_allow_access_secure(self):
        """
        Test that setting non-secure access for a domain inserts the
        proper attribute.
        
        """
        policy = policies.new_policy()
        policies.allow_access_from(policy, 'media.example.com', secure=False);
        access_elem = policy.getElementsByTagName('allow-access-from')[0]
        self.assertEqual(len(access_elem.attributes), 2)
        self.assertEqual(access_elem.getAttribute('secure'), 'false')

    def test_site_control(self):
        """
        Test that adding meta-policy information inserts the proper
        element and attributes.
        
        """
        for permitted in policies.VALID_SITE_CONTROL:
            policy = policies.new_policy()
            policies.site_control(policy, permitted)
            self.assertEqual(len(policy.documentElement.childNodes), 1)
            self.assertEqual(len(policy.getElementsByTagName('site-control')), 1)
            control_elem = policy.getElementsByTagName('site-control')[0]
            self.assertEqual(len(control_elem.attributes), 1)
            self.assertEqual(control_elem.getAttribute('permitted-cross-domain-policies'), permitted)

    def test_bad_site_control(self):
        """
        Test that meta-policies are restricted to the values permitted
        by the specification.
        
        """
        policy = policies.new_policy()
        self.assertRaises(TypeError, policies.site_control, policy, 'not-valid')

    def test_simple_policy(self):
        """
        Test that creating a simple policy with a list of domains
        returns a correct policy document.
        
        """
        domains = ['media.example.com', 'api.example.com']
        policy = policies.simple_policy(domains)
        self.assertEqual(len(policy.documentElement.childNodes), 2)
        self.assertEqual(len(policy.getElementsByTagName('allow-access-from')), 2)
        domain_elems = policy.getElementsByTagName('allow-access-from')
        for i, domain in enumerate(domains):
            self.assertEqual(domain,
                             policy.documentElement.getElementsByTagName('allow-access-from')[i].getAttribute('domain'))

    def test_no_access_policy(self):
        """
        Test that creating a policy which permits no access returns a
        correct policy document.
        
        """
        policy = policies.no_access_policy()
        self.assertEqual(len(policy.documentElement.childNodes), 1)
        self.assertEqual(len(policy.getElementsByTagName('site-control')), 1)
        control_elem = policy.getElementsByTagName('site-control')[0]
        self.assertEqual(control_elem.getAttribute('permitted-cross-domain-policies'), 'none')


class PolicyViewTests(TestCase):
    urls = 'flashpolicies.test_urls'

    def test_simple(self):
        response = self.client.get('/crossdomain1.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/x-cross-domain-policy')
        policy = xml.dom.minidom.parseString(response.content)
        self.assertEqual(len(policy.getElementsByTagName('allow-access-from')), 2)
        domain_elems = policy.getElementsByTagName('allow-access-from')
        domains = ['media.example.com', 'api.example.com']
        for i, domain in enumerate(domains):
            self.assertEqual(domain,
                             policy.getElementsByTagName('allow-access-from')[i].getAttribute('domain'))

    def test_no_access(self):
        response = self.client.get('/crossdomain2.xml')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/x-cross-domain-policy')
        policy = xml.dom.minidom.parseString(response.content)
        self.assertEqual(len(policy.getElementsByTagName('site-control')), 1)
        self.assertEqual(policy.getElementsByTagName('site-control')[0].getAttribute('permitted-cross-domain-policies'),
                         'none')
