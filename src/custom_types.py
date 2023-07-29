from enum import Enum
from typing import List, cast
from dataclasses import dataclass


class SourceType(str, Enum):
    Youtube = "Youtube"
    Blog = "Blog"
    Website = "Website"
    Official = "Official"


@dataclass
class Metadata:
    source_type: SourceType


@dataclass
class Source:
    url: str
    content: str
    metadata: Metadata
