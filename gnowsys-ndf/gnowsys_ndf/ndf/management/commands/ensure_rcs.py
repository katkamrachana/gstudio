import os
import time
import subprocess
from django.core.management.base import BaseCommand, CommandError
from gnowsys_ndf.ndf.models import *
from gnowsys_ndf.settings import *
historyMgr = HistoryManager()


class Command(BaseCommand):
    def handle(self, *args, **options):
        nodes_coll = node_collection.find({'_type': {'$nin': ['ToReduceDocs', 'ReducedDocs', 'node_holder']}})
        triples_coll = triple_collection.find()
        filehives_coll = filehive_collection.find()

        print "\n Total nodes found: ", nodes_coll.count() + triples_coll.count() + filehives_coll.count()
        ensure_rcs(nodes_coll)
        ensure_rcs(triples_coll)
        ensure_rcs(filehives_coll)

def ensure_rcs(coll_cur):
    for each_doc in coll_cur:
        path = historyMgr.get_file_path(each_doc)
        path = path + ",v"
        if not os.path.exists(path):
            each_doc.save()
