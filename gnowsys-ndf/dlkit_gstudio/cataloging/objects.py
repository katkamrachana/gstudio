"""GStudio implementations of Catalog objects."""

"""Implementations of cataloging abstract base class objects."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import importlib
# import gridfs
from bson import ObjectId


from . import default_mdata
from .. import utilities
from dlkit.abstract_osid.cataloging import objects as abc_cataloging_objects
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects
from ..osid.metadata import Metadata
from ..primitives import Id
from ..utilities import get_registry
from ..utilities import update_display_text_defaults
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id
from ..utilities import get_display_text_map
from gnowsys_ndf.ndf.models import Node, node_collection, triple_collection

#=================
# for multi-language
from ..types import Language, Script, Format
from ..primitives import Type, DisplayText
DEFAULT_LANGUAGE_TYPE = Type(**Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**Format().get_type_data('DEFAULT'))


class Catalog(abc_cataloging_objects.Catalog, osid_objects.OsidCatalog):
    """A ``Catalog`` represents a collection of entries.

    Like all OSID objects, a ``Catalog`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    ``get_catalog_record()`` should be used to retrieve any record
    corresponding to arecord ``Type``. The existence of the record must
    not be assumed until requested at which point it is safe to cast
    into the record indicated by the type.

    """
    _namespace = 'cataloging.Catalog'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalog.__init__(self, object_name='CATALOG', **kwargs)
        # self._record_type_data_sets = get_registry('REPOSITORY_RECORD_TYPES', runtime)

    # __metaclass__ = abc.ABCMeta

    # @abc.abstractmethod
    def get_catalog_record(self, catalog_record_type):
        """Gets the catalog record corresponding to the given ``Catalog`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``catalog_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(catalog_record_type)`` is ``true`` .

        :param catalog_record_type: a type of the record to retrieve
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog record
        :rtype: ``osid.cataloging.records.CatalogRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        # return  # osid.cataloging.records.CatalogRecord
        raise errors.Unimplemented()

    def get_object_map(self):
        """Returns object map dictionary"""
        obj_map = dict()
        super(Repository, self).get_object_map(obj_map)
        obj_map['type'] = 'Catalog'
        return obj_map


class CatalogForm(abc_cataloging_objects.CatalogForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Catalogs``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CatalogAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    # __metaclass__ = abc.ABCMeta
    _namespace = 'cataloging.Catalog'

    def __init__(self, **kwargs):
        osid_objects.OsidCatalogForm.__init__(self, object_name='CATALOG', **kwargs)
        self._mdata = default_mdata.get_catalog_mdata()
        self._init_metadata(**kwargs)
        # if not self.is_for_update():
        #     self._init_form(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)
            self._init_gstudio_map(**kwargs)


    def _init_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm._init_map(self, record_types, **kwargs)

    def _init_gstudio_map(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm._init_gstudio_map(self, record_types, **kwargs)


    def _init_form(self, record_types=None, **kwargs):
        """Initialize form map"""
        osid_objects.OsidCatalogForm.__init__(self, **kwargs)


    # @abc.abstractmethod
    def get_catalog_form_record(self, catalog_record_type):
        """Gets the ``CatalogFormRecord`` corresponding to the given catalog record ``Type``.

        :param catalog_record_type: a catalog record type
        :type catalog_record_type: ``osid.type.Type``
        :return: the catalog form record
        :rtype: ``osid.cataloging.records.CatalogFormRecord``
        :raise: ``NullArgument`` -- ``catalog_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(catalog_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.records.CatalogFormRecord


class CatalogList(abc_cataloging_objects.CatalogList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CatalogList`` provides a means for accessing ``Catalog`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Catalog catalog =
    cl.getNextCatalog(); }

    or
      while (cl.hasNext()) {
           Catalog[] catalogs = cl.getNextCatalogs(cl.available());
      }

    """
    # __metaclass__ = abc.ABCMeta

    # @abc.abstractmethod
    def get_next_catalog(self):
        """Gets the next ``Catalog`` in this list.

        :return: the next ``Catalog`` in this list. The ``has_next()`` method should be used to test that a next ``Catalog`` is available before calling this method.
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        # return  # osid.cataloging.Catalog
        return self.next()

    next_catalog = property(fget=get_next_catalog)

    # @abc.abstractmethod
    def get_next_catalogs(self, n):
        """Gets the next set of ``Catalog`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Catalog`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Catalog`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.cataloging.Catalog``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        # return  # osid.cataloging.Catalog
        return self._get_next_n(n)



class CatalogNode(abc_cataloging_objects.CatalogNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``CatalogHierarchySession``.

    """
    # __metaclass__ = abc.ABCMeta

    def get_object_node_map(self):
        node_map = dict(self.get_catalog().get_object_map())
        node_map['type'] = 'CatalogNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for catalog_node in self.get_parent_catalog_nodes():
            node_map['parentNodes'].append(catalog_node.get_object_node_map())
        for catalog_node in self.get_child_catalog_nodes():
            node_map['childNodes'].append(catalog_node.get_object_node_map())
        return node_map



    # @abc.abstractmethod
    def get_catalog(self):
        """Gets the ``Catalog`` at this node.

        :return: the catalog represented by this node
        :rtype: ``osid.cataloging.Catalog``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.Catalog

    catalog = property(fget=get_catalog)

    # @abc.abstractmethod
    def get_parent_catalog_nodes(self):
        """Gets the parents of this catalog.

        :return: the parents of the ``id``
        :rtype: ``osid.cataloging.CatalogNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNodeList

    parent_catalog_nodes = property(fget=get_parent_catalog_nodes)

    # @abc.abstractmethod
    def get_child_catalog_nodes(self):
        """Gets the children of this catalog.

        :return: the children of this catalog
        :rtype: ``osid.cataloging.CatalogNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.cataloging.CatalogNodeList

    child_catalog_nodes = property(fget=get_child_catalog_nodes)


class CatalogNodeList(abc_cataloging_objects.CatalogNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CatalogNodeList`` provides a means for accessing ``CatalogNode`` elements sequentially either one at a time or many at a time.

    Examples: while (cnl.hasNext()) { CatalogNode node =
    cnl.getNextCatalogNode(); }

    or
      while (cnl.hasNext()) {
           CatalogNode[] nodes = cnl.getNextCatalogNodes(cnl.available());
      }

    """
    # __metaclass__ = abc.ABCMeta

    # @abc.abstractmethod
    def get_next_catalog_node(self):
        """Gets the next ``CatalogNode`` in this list.

        :return: the next ``CatalogNode`` in this list. The ``has_next()`` method should be used to test that a next ``CatalogNode`` is available before calling this method.
        :rtype: ``osid.cataloging.CatalogNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        # return  # osid.cataloging.CatalogNode
        return self.next()

    next_catalog_node = property(fget=get_next_catalog_node)

    # @abc.abstractmethod
    def get_next_catalog_nodes(self, n):
        """Gets the next set of ``CatalogNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``CatalogNode`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``CatalogNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.cataloging.CatalogNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        # return  # osid.cataloging.CatalogNode
        return self._get_next_n(n)


