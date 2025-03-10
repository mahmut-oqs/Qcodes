"""
The extensions module contains smaller modules that extend the functionality of QCoDeS.
These modules may import from all of QCoDeS but do not themselves get imported into QCoDeS.
"""

from ._driver_test_case import DriverTestCase
from ._log_export_info import log_dataset_export_info
from .infer import (
    InferAttrs,
    InferError,
    get_chain_links_of_type,
    get_instrument_from_param,
    get_parameter_chain,
    get_parent_instruments_from_chain_of_type,
    get_root_parameter,
    get_sole_chain_link_of_type,
    get_sole_parent_instrument_from_chain_of_type,
    infer_channel,
    infer_instrument,
    infer_instrument_module,
)
from .installation import register_station_schema_with_vscode

__all__ = [
    "DriverTestCase",
    "InferAttrs",
    "InferError",
    "get_chain_links_of_type",
    "get_instrument_from_param",
    "get_parameter_chain",
    "get_parent_instruments_from_chain_of_type",
    "get_root_parameter",
    "get_sole_chain_link_of_type",
    "get_sole_parent_instrument_from_chain_of_type",
    "infer_channel",
    "infer_instrument",
    "infer_instrument_module",
    "log_dataset_export_info",
    "register_station_schema_with_vscode",
]
