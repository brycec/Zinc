from boto.s3.connection import S3Connection
from utils import canonical_path
from shutil import copyfile
import io
import os

class Backend(object):

    def write_path_from_path(dst_path, src_path):
        pass

class FileSystemBackend(object):

    def __init__(self, path):
        self.path = canonical_path(path)

    def _relative_path(self, path):
        return os.path.join(self.path, path)
   
    def write_path_from_path(self, dst_path, src_path):
        copyfile(src_path, dst_path)

    def write_path_from_stream(self, dst_path, fp):
        file = open(self._relative_path(dst_path) , 'w')
        fp.write(io.BufferedWriter(file))
        file.close()

    def write_path_from_string(self, dst_path, s):
        file = open(self._relative_path(dst_path) , 'w')
        file.write(s)
        file.close()


class S3Backend(Backend):

    def __init__(self, bucket, access_key, access_secret):
        self.bucket = bucket
        self.connection = S3Connection(access_key, access_secret)






