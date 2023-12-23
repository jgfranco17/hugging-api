from dataclasses import dataclass


@dataclass(frozen=True)
class MessageStatus:
    PENDING: int = 0
    RESOLVED: int = 1
    REJECTED: int = 2


@dataclass(frozen=True)
class MessageType:
    FINAL: str = "finalAnswer"
    STREAM: str = "stream"
    WEB: str = "webSearch"
    STATUS: str = "status"