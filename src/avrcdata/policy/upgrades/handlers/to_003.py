from Products.CMFCore.utils import getToolByName
from avrc.aeh.upgrades.handlers import to_020
from avrc.aeh import Logger as default_logger

def import_(context, logger=default_logger):
    to_020.import_(context, logger)
    portal_setup = getToolByName(context, 'portal_setup')
    ## Now make sure our other products are set up
    portal_setup.runImportStepFromProfile("profile-hive.lab:default", 'typeinfo')
    portal_setup.runImportStepFromProfile("profile-hive.arv:default", 'typeinfo')
    portal_setup.runImportStepFromProfile("profile-hive.symptom:default", 'typeinfo')
    logger.info(u'Upgrade complete')
