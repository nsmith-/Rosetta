from . import BSMCharacterisation
from . import HiggsBasis
from . import HiggsCharacterisation
from . import HiggsPO
from . import HISZ
from . import SILHBasis
from . import TemplateBasis
from . import WarsawBasis

__all__ = [
    "BSMCharacterisation",
    "HiggsBasis",
    "HiggsCharacterisation",
    "HiggsPO",
    "HISZ",
    "SILHBasis",
    "TemplateBasis",
    "WarsawBasis",
]

_all_bases = {k: getattr(globals()[k], k) for k in __all__}
