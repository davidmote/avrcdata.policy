import unittest2 as unittest
from avrcdata.policy.testing import AVRCDATA_POLICY_INTEGRATION_TESTING
from plone.app.testing import applyProfile

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = AVRCDATA_POLICY_INTEGRATION_TESTING

    def test_indexing_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('collective.indexing'))        

    def test_datepicker_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('jyu.z3cform.datepicker'))     

    def test_caching_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('plone.app.caching'))   

    def test_ldap_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('plone.app.ldap')) 

    def test_aeh_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('avrc.aeh'))

    def test_arv_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('hive.arv')) 

    def test_lab_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('hive.lab')) 
    
    def test_symptom_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('hive.symptom')) 


