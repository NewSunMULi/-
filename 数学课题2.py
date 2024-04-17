from dataclasses import dataclass
from typing import List, Optional


@dataclass
class DeprecatedFile:
    md5: str
    name: str


@dataclass
class DeprecatedPackage:
    md5: str
    name: str


@dataclass
class PurpleVoicePack:
    language: str
    md5: str
    name: str
    package_size: str
    path: str
    size: str


@dataclass
class GameDiff:
    is_recommended_update: bool
    md5: str
    name: str
    package_size: str
    path: str
    size: str
    version: str
    voice_packs: List[PurpleVoicePack]


@dataclass
class PurpleSegment:
    md5: str
    path: str


@dataclass
class FluffyVoicePack:
    language: str
    md5: str
    name: str
    package_size: str
    path: str
    size: str


@dataclass
class GameLatest:
    decompressed_path: str
    entry: str
    md5: str
    name: str
    package_size: str
    path: str
    segments: List[PurpleSegment]
    size: str
    version: str
    voice_packs: List[FluffyVoicePack]


@dataclass
class Game:
    diffs: List[GameDiff]
    latest: GameLatest


@dataclass
class PluginElement:
    entry: Optional[str] = None
    md5: Optional[str] = None
    name: Optional[str] = None
    path: Optional[str] = None
    size: Optional[str] = None
    version: Optional[str] = None


@dataclass
class DataPlugin:
    plugins: List[PluginElement]
    version: str


@dataclass
class TentacledVoicePack:
    language: str
    md5: str
    name: str
    package_size: str
    path: str
    size: str


@dataclass
class PreDownloadGameDiff:
    is_recommended_update: bool
    md5: str
    name: str
    package_size: str
    path: str
    size: str
    version: str
    voice_packs: List[TentacledVoicePack]


@dataclass
class FluffySegment:
    md5: str
    path: str


@dataclass
class StickyVoicePack:
    language: str
    md5: str
    name: str
    package_size: str
    path: str
    size: str


@dataclass
class PreDownloadGameLatest:
    decompressed_path: str
    entry: str
    md5: str
    name: str
    package_size: str
    path: str
    segments: List[FluffySegment]
    size: str
    version: str
    voice_packs: List[StickyVoicePack]


@dataclass
class PreDownloadGame:
    diffs: List[PreDownloadGameDiff]
    latest: PreDownloadGameLatest


@dataclass
class SDK:
    channel_id: str
    desc: str
    md5: str
    package_size: str
    path: str
    pkg_version: str
    size: str
    sub_channel_id: str
    version: str


@dataclass
class Data:
    deprecated_files: List[DeprecatedFile]
    deprecated_packages: List[DeprecatedPackage]
    force_update: None
    game: Game
    plugin: DataPlugin
    pre_download_game: PreDownloadGame
    sdk: SDK
    web_url: str


@dataclass
class ApifoxModel:
    data: Data
    message: str
    retcode: int