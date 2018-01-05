# uncompyle6 version 2.14.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.6 (default, Oct 26 2016, 20:30:19) 
# [GCC 4.8.4]
# Embedded file name: /home/docker/code/gstudio/gnowsys-ndf/gnowsys_ndf/ndf/management/commands/group_import.py
# Compiled at: 2018-01-04 18:06:23
"""
Import can also be called using command line args as following:
    python manage.py group_import <dump_path> <md5-check> <group-availability> <user-objs-restoration>
    like:
        python manage.py group_import <dump_path> y y y
"""
import os, json, imp, subprocess
from bson import json_util
import pathlib2
try:
    from bson import ObjectId
except ImportError:
    from pymongo.objectid import ObjectId

import time, datetime
from django.core.management.base import BaseCommand, CommandError
from gnowsys_ndf.ndf.models import node_collection, triple_collection, filehive_collection, counter_collection
from gnowsys_ndf.ndf.models import HistoryManager, RCS
from gnowsys_ndf.settings import GSTUDIO_DATA_ROOT, GSTUDIO_LOGS_DIR_PATH, MEDIA_ROOT, GSTUDIO_INSTITUTE_ID, RCS_REPO_DIR
from users_dump_restore import load_users_dump
from import_logic import *
from gnowsys_ndf.settings import RCS_REPO_DIR_HASH_LEVEL
from schema_mapping import update_factory_schema_mapper
from gnowsys_ndf.ndf.views.utils import replace_in_list, merge_lists_and_maintain_unique_ele
DATA_RESTORE_PATH = None
DATA_DUMP_PATH = None
DEFAULT_USER_ID = 1
DEFAULT_USER_SET = False
USER_ID_MAP = {}
SCHEMA_ID_MAP = {}
log_file = None
CONFIG_VARIABLES = None
DATE_AT_IDS = []
GROUP_CONTAINERS = ['Module']
date_related_at_cur = node_collection.find({'_type': 'AttributeType','name': {'$in': ['start_time', 'end_time', 'start_enroll', 'end_enroll']}})
for each_date_related_at in date_related_at_cur:
    DATE_AT_IDS.append(each_date_related_at._id)

history_manager = HistoryManager()
rcs = RCS()

def call_exit():
    print '\n Exiting...'
    os._exit(0)


def check_group_availability(*args):
    global DATA_RESTORE_PATH
    global log_file
    global CONFIG_VARIABLES
    global DEFAULT_USER_ID
    global DATA_DUMP_PATH
    group_node = node_collection.one({'_id': ObjectId(CONFIG_VARIABLES.GROUP_ID)})
    print '\n\n Restoring Group'
    log_file.write('\n Restoring Group')
    if group_node:
        print '\n Group with restoration ID already exists.'
        confirm_grp_data_merge = ''
        if args and len(args) == 4:
            confirm_grp_data_merge = args[2]
        else:
            confirm_grp_data_merge = raw_input('Dump Group already exists here. Would you like to merge the data ?')
        if confirm_grp_data_merge not in ('y', 'Y'):
            log_file.write('\n Group with Restore Group ID is FOUND on Target system.')
            call_exit()
        else:
            fp = get_file_path_with_id(CONFIG_VARIABLES.GROUP_ID, DATA_DUMP_PATH)
            if fp:
                if not fp.endswith(',v'):
                    fp = fp + ',v'
                log_file.write('\n Restoring Group: ' + str(fp))
                restore_node(fp, None, DATA_RESTORE_PATH, log_file_path)
            group_node = node_collection.one({'_id': ObjectId(CONFIG_VARIABLES.GROUP_ID)})
            group_node.group_admin = [DEFAULT_USER_ID]
            group_node.save()
            log_file.write('\n Group Merge confirmed.')
            print ' Proceeding to restore.'
    else:
        print '\n Group with restoration ID DOES NOT exists.'
        confirm_grp_data_restore = ''
        if args and len(args) == 4:
            confirm_grp_data_restore = args[2]
        else:
            confirm_grp_data_restore = raw_input('Proceed to restore ?')
        if confirm_grp_data_restore not in ('y', 'Y'):
            log_file.write('\n Group with Restore Group ID is NOT FOUND on Target system.')
            print ' Cancelling to restore.'
            call_exit()
        else:
            fp = get_file_path_with_id(CONFIG_VARIABLES.GROUP_ID, DATA_DUMP_PATH)
            if fp:
                if not fp.endswith(',v'):
                    fp = fp + ',v'
                log_file.write('\n Restoring Group: ' + str(fp))
                restore_node(fp, None, DATA_RESTORE_PATH, log_file_path)
            group_node = node_collection.one({'_id': ObjectId(CONFIG_VARIABLES.GROUP_ID)})
            group_node.group_admin = [DEFAULT_USER_ID]
            group_node.save()
            log_file.write('\n Group Merge confirmed.')
            print ' Proceeding to restore.'
    return


def update_group_set(document_json):
    if 'group_set' in document_json:
        if ObjectId(CONFIG_VARIABLES.GROUP_ID) not in document_json['group_set']:
            document_json['group_set'].append(ObjectId(CONFIG_VARIABLES.GROUP_ID))
    return document_json


def core_import(non_grp_root_node=None, *args):
    global log_file
    global log_file_path
    datetimestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file_name = 'artifacts_restore_' + str(GSTUDIO_INSTITUTE_ID) + '_' + str(datetimestamp)
    log_file_path = create_log_file(log_file_name)
    log_file = open(log_file_path, 'w+')
    log_file.write('\n######### Script ran on : ' + str(datetime.datetime.now()) + ' #########\n\n')
    log_file.write('\nUpdated CONFIG_VARIABLES: ' + str(CONFIG_VARIABLES))
    print '\n Validating the data-dump'
    print '\nDATA_DUMP_PATH: ', DATA_DUMP_PATH
    validate_data_dump(DATA_DUMP_PATH, CONFIG_VARIABLES.MD5, *args)
    print '\n Checking the dump Group-id availability.'
    check_group_availability(*args)
    print '\n User Restoration.'
    user_json_file_path = os.path.join(DATA_DUMP_PATH, 'users_dump.json')
    log_stmt = user_objs_restoration(CONFIG_VARIABLES.RESTORE_USER_DATA, user_json_file_path, DATA_DUMP_PATH, *args)
    log_file.write(log_stmt)
    print '\n Factory Schema Restoration. Please wait..'
    call_group_import(os.path.join(DATA_DUMP_PATH, 'data', 'rcs-repo'), log_file_path, DATA_RESTORE_PATH, non_grp_root_node)
    copy_media_data(os.path.join(DATA_DUMP_PATH, 'media_files', 'data', 'media'))


class Command(BaseCommand):

    def handle(self, *args, **options):
        global SCHEMA_ID_MAP
        global DATA_RESTORE_PATH
        global GROUP_CONTAINERS
        global DATA_DUMP_PATH
        global CONFIG_VARIABLES
        if args and len(args) == 4:
            DATA_RESTORE_PATH = args[0]
        else:
            DATA_RESTORE_PATH = raw_input('\n\tEnter absolute path of data-dump folder to restore:')
        print '\nDATA_RESTORE_PATH: ', DATA_RESTORE_PATH
        if os.path.exists(DATA_RESTORE_PATH):
            if os.path.exists(os.path.join(DATA_RESTORE_PATH, 'dump')):
                DATA_DUMP_PATH = os.path.join(DATA_RESTORE_PATH, 'dump')
                SCHEMA_ID_MAP = update_factory_schema_mapper(DATA_RESTORE_PATH)
                CONFIG_VARIABLES = read_config_file(DATA_RESTORE_PATH)
                core_import(None, *args)
            else:
                print '\n***** NON Group Dump found. *****\n'
                GRP_CONTAINERS_CUR = node_collection.find({'name': {'$in': GROUP_CONTAINERS},'_type': 'GSystemType'
                   })
                GRP_CONTAINERS_IDS = [ cont._id for cont in GRP_CONTAINERS_CUR ]
                SCHEMA_ID_MAP = update_factory_schema_mapper(DATA_RESTORE_PATH)
                dump_dir = [ os.path.join(DATA_RESTORE_PATH, gd) for gd in os.listdir(DATA_RESTORE_PATH) if os.path.isdir(os.path.join(DATA_RESTORE_PATH, gd)) ]
                print '\n Total Groups to be Restored: ', len(dump_dir)
                for each_gd_abs_path in dump_dir:
                    DATA_DUMP_PATH = os.path.join(each_gd_abs_path, 'dump')
                    DATA_RESTORE_PATH = each_gd_abs_path
                    CONFIG_VARIABLES = read_config_file(DATA_RESTORE_PATH)
                    non_grp_root_node_obj = node_collection.one({'_id': ObjectId(CONFIG_VARIABLES.ROOT_DUMP_NODE_ID)
                       })
                    if non_grp_root_node_obj:
                        core_import((CONFIG_VARIABLES.ROOT_DUMP_NODE_ID, CONFIG_VARIABLES.ROOT_DUMP_NODE_NAME), *args)
                    else:
                        non_grp_root_node_obj = node_collection.one({'name': CONFIG_VARIABLES.ROOT_DUMP_NODE_NAME,
                           'member_of': {'$in': GRP_CONTAINERS_IDS}})
                        if non_grp_root_node_obj:
                            core_import((CONFIG_VARIABLES.ROOT_DUMP_NODE_ID, CONFIG_VARIABLES.ROOT_DUMP_NODE_NAME), *args)
                        else:
                            core_import(None, *args)

            print '*' * 70
            print '\n Log will be found at: ', log_file_path
            print '*' * 70
        else:
            print '\n No dump found at entered path.'
            call_exit()
        return