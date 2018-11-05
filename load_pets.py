#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""IS211_Assibngment10: A simple script to load data."""


import sqlite3 as sql


people = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
    )

pets = (
    (1, 'Rusty', 'Dalmatian', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
    )

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
    )


con =sql.connect('pets.db')

with con:
    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS person")
    cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY"
                ",first_name TEXT"
                ",last_name TEXT"
                ",age INTEGER)")
    cur.executemany("INSERT INTO person VALUES(?, ?, ?, ?,)", people)
    
    cur.execute("DROP TABLE IF EXISTS pet")
    cur,execute("CREATE TABLE pet(id INTTEGER PRIMARY KEY"
                ",name TEXT"
                ",breed TEXT"
                ",age INTEGER"
                ",dead INTEGER)")
    cur.executemany("INSERT INTO pet VALUES(?, ?, ?, ?, ?)", pets)

    cur.execute("DROP TABLE IF EXISTS person_pet")
    cur.execute("CREATE TABLE person_pet(person_id INTEGER"
                ",pet_id INTEGER)")
    cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)
