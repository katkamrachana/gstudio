"""GStudio osid metadata configurations for Catalog service."""

from .. import types
from ..primitives import Type
DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data("DEFAULT"))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data("DEFAULT"))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data("DEFAULT"))
DEFAULT_GENUS_TYPE = Type(**types.Genus().get_type_data("DEFAULT"))
from gnowsys_ndf.settings import GSTUDIO_DEFAULT_LICENSE

def get_catalog_mdata():
    """Return default mdata map for Catalog"""
    return {
    }
