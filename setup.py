#!/usr/bin/env python3

from model import db, Message 

db.connect()
db.create_tables([Message])
