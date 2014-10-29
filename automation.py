__author__ = 'junojunho / wnsgh611@gmail.com'

# This file is for openstack automation project
# Total procedure is divided into 2 parts, keystone auth part, and swift access part.
# Required Module : python-swift, python-keystoneclient

from keystoneclient.v2_0 import client

# First big step is Keystone auth part
# Keystone auth part is for get token from openstack - keystone for swift auth id & password
# In keystone, we will create a user & tenant, we will set role for swift each user & tenant
# We will use bypassing method with os_auth_url(auth_url), os_service_token(token), os_service_endpoint(endpoint)

keystone = client.Client(auth_url='http://localhost:5000/v2.0', token='0120b90111df48feb5c727081afb859f',
                         endpoint='http://localhost:35357/v2.0')

#if authentication is done, for testing, we will list tenant-list

keystone.tenants.list()

# Second big step is Swift auth part
# This is for docker-registry, so, using user created by keystone service, we will create a container

# Further step is grant access control (ACL in swift) to user
# only this user can access created container