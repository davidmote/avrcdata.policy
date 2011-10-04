from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from avrc.aeh.testing import CLINICAL_FIXTURE

from zope.configuration import xmlconfig

class avrcdataPolicy(PloneSandboxLayer):

    defaultBases = (CLINICAL_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import avrcdata.policy
        xmlconfig.file('configure.zcml', avrcdata.policy, context=configurationContext)
                
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'avrcdata.policy:default')

AVRCDATA_POLICY_FIXTURE = avrcdataPolicy()
AVRCDATA_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(AVRCDATA_POLICY_FIXTURE,), name="leadtheway:Integration")
