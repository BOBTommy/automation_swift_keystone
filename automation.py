__author__ = 'junojunho / wnsgh611@gmail.com'

# This file is for openstack automation project
# Total procedure is divided into 2 parts, keystone auth part, and swift access part.

# First big step is Keystone auth part
# Keystone auth part is for get token from openstack - keystone for swift auth id & password
# In keystone, we will create a user & tenant, we will set role for swift each user & tenant


# Second big step is Swift auth part
# This is for docker-registry, so, using user created by keystone service, we will create a container

# Further step is grant access control (ACL in swift) to user
# only this user can access created container