#!/usr/bin/env python
import tempfile
import os
import sys
import re
import random

from rosetta import HiggsBasis as HB
from rosetta import WarsawBasis as WB
from rosetta import SILHBasis as SB
from rosetta import BSMCharacterisation as MB
from rosetta import TemplateBasis as TB
from rosetta import HISZ as HZ
from rosetta.internal import SLHA, session

from rosetta.interfaces.Lilith import Lilith

# instance = HB.HiggsBasis(flavor='universal', param_card = '../HiggsBasis_universal_1e-3.dat', translate=False)
# instance = HZ.HISZ(flavor='universal', param_card = '../HISZ_universal_1e-3.dat', translate=False)
instance = HZ.HISZ(flavor='universal', param_card = 'Cards/HISZ_universal.dat')

lik = Lilith.compute_likelihood(instance)

session.log('Lilith Likelihood: '+str(lik))
session.log('#############################')
session.log('')