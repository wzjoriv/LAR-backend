import sys
import os
sys.path.append(os.path.abspath('..'))
from lar.utils import prune_str, prune_str_list

## Author: Josue N Rivera


def test_prune_str():
    assert prune_str("h_llo woRld") == "HLLOWORLD"

def test_prune_str_list():
    assert sorted(["_hospitals_", "Fire StationS", "PUbliC_SCHooLS"]) \
            == sorted("HOSPITALS", "FIRESTATIONS", "PUBLICSCHOOLS")
