import logging

LOG = logging.getLogger(__name__)

def create_cluster():
    LOG.info("creating cluster for GCP")
    LOG.debug('Only shown in debug mode')
    hank_test()

def hank_test():
    LOG.error("oh shit")
