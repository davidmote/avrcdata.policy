from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from avrc.aeh.testing import CLINICAL_FIXTURE

from zope.configuration import xmlconfig


class AvrcDataPolicy(PloneSandboxLayer):

    defaultBases = (CLINICAL_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import avrcdata.policy as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'avrcdata.policy:default')


AVRCDATA_POLICY_FIXTURE = AvrcDataPolicy()

AVRCDATA_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(AVRCDATA_POLICY_FIXTURE,),
    name="AvrcData:Integration"
    )
