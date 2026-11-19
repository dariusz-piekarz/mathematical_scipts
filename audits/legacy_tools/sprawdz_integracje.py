#!/usr/bin/env python3
"""Punkt wejściowy aktualnego audytu integralności; skrypt ogólny narasta wraz z iteracjami."""
from pathlib import Path
import subprocess,sys
script=Path(__file__).with_name('sprawdz_integracje_3.py')
sys.exit(subprocess.call([sys.executable,str(script),*sys.argv[1:]]))
