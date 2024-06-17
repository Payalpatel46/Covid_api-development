"""
FILE: base_model.py
DESCRIPTION: Models for General Usage
AUTHOR: Payal Patel
DATE: 01-March-2021
"""
# Import libraries
from typing import Any, Dict, List

from pydantic import BaseModel # type: ignore


#######################################
# ResponseModel
#######################################
class ResponseModel(BaseModel):
    data: Any
    dt: str
    ts: int
