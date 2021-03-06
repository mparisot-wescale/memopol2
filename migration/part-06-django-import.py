#!/usr/bin/env python

import sys, os

# This is not needed anymore
print "part-06-django-import.py is not needed at this time"
sys.exit(0)



import couchdb

from memopol2.main.models import Mep, Position

print "Deleting existing django meps"
Mep.objects.all().delete()

#django_meps = Mep.objects.all()
#print "Existing meps in django db:", len(django_meps)
#existing_id_set = set([x.couchid for x in django_meps])
existing_id_set = set()

server = couchdb.Server(os.getenv("COUCH_URL_ROOT"))
meps = server["meps"]

print "Meps in couch db:", len(meps)

for mepid in meps:
    if mepid not in existing_id_set:
        newmep = Mep(couchid=mepid)
        newmep.save()

