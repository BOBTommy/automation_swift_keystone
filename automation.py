__author__ = 'junojunho / wnsgh611@gmail.com'

# This file is for openstack automation project
# Total procedure is divided into 2 parts, keystone auth part, and swift access part.
# Required Module : python-swift, python-keystoneclient

from keystoneclient.v2_0 import client

# First big step is Keystone auth part
# Keystone auth part is for get token from openstack - keystone for swift auth id & password.
# In keystone, we will create a 2 tenant for each project,
# one for docker-registry images, and the other for archiving user docker images file.
# We will use bypassing method with os_auth_url(auth_url), os_service_token(token), os_service_endpoint(endpoint)

keystone = client.Client(auth_url='http://localhost:5000/v2.0', token='0120b90111df48feb5c727081afb859f',
                         endpoint='http://localhost:35357/v2.0')

#if authentication is done, for testing, we will list tenant-list

print(keystone.tenants.list())

# for user custom object tenant, some steps maybe need
# 1. create tenant.
# 2. user role add to this tenant. this tenant will be used for uploading user custom files

tenant_name = raw_input('Insert tenant name : ')
# this will be replaced using django app.
# name will be formatted with team_name + / + tenant_name

tenant = keystone.tenants.create(tenant_name=tenant_name, description=tenant_name + "team name is buildbuild", enabled=True)
tenant_id = tenant.id

# Second big step is Swift auth part
# This is for docker-registry, so, using user created by keystone service, we will create a container

# Further step is grant access control (ACL in swift) to user
# only this user can access created container