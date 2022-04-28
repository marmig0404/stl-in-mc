import unittest
from stlinmc import voxel


class TestMain(unittest.TestCase):
    def test_voxel(self):
        # https://commons.wikimedia.org/wiki/File:Stanford_Bunny.stl
        voxel.import_stl_as_voxels('data/Stanford_Bunny.stl')
        # https://reprap.org/forum/read.php?88,6830
        voxel.import_stl_as_voxels('data/HalfDonut.stl')