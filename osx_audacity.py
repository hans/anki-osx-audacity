# -*- coding: utf-8 -*-

from os import path, system
import re

from anki.hooks import addHook
from anki.sound import _soundReg
from aqt import mw
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QAction, QMenu, QMessageBox


def open_in_audacity():
    if mw.reviewer.card is None:
        return

    card = mw.reviewer.card
    media_path = re.sub("(?i)\.anki2?$", ".media", mw.col.path)

    for m in re.findall(_soundReg, card.q() + card.a()):
        sound_path = path.join(media_path, m)
        system('open -a Audacity "{}"'.format(sound_path))


def init():
    action = QAction("Open audio in Audacity", mw)
    action.setShortcut('Ctrl+Shift+A')
    action.setEnabled(True)

    mw.connect(action, SIGNAL('triggered()'), open_in_audacity)
    mw.form.menuTools.addAction(action)


init()
