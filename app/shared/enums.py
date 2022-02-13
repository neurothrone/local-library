from enum import Enum


class BookStatus(str, Enum):
    IS_READING = "is_reading"
    HAVE_READ = "have_read"
    WILL_READ = "will_read"
