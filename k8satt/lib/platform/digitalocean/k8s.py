"""
k8s.py - DigitalOcean k8s provisioning library
"""
import logging

LOG = logging.getLogger(__name__)

def create_cluster():
    LOG.info("creating cluster for DigitalOcean")
