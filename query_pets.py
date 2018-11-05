#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""IS211_Assignment10: A simple query for the pet database."""

import sqlite3 as sql

con = sql.connect('pets.db')

with con:
    cur = con.cursor()

    while True:
        id_num = raw_input("Please enter pet owner ID or enter -1 to exit: ")
        if id_num == '-1':
            print 'Exit search.'
            raise SystemExit

        cur.execute("SELECT first_name"
                    ",last_name"
                    ",person.age"
                    ",name"
                    ",breed"
                    ",pet.age"
                    ",dead"
                    "FROM person, pet, person_pet"
                    "WHERE person.id = person_pet.person_id"
                    "AND pet.id = person_pet.pet_id AND person.id=(?)", (id_num))
        person = cur.fetchall()

        if len(person) == 0:
            print "Invalid ID. Please enter valid owner ID."
            continue

        for r in person:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            pet_name = row[3]
            pet_type = row[4]
            pet_age= row[5]
            living = row[6]
            if living == 1:
                print ('{} {}, age {}, owned a {} named {}, '
                       'who was {} years old.').format(firstname,
                                                      last_name,
                                                      age,
                                                      pet_type,
                                                      pet_name,
                                                      pet_age)
            else:
                print ('{} {}, age {}, owns a {} named {}, '
                       'whois {} years old.').format(firstname,
                                                      last_name,
                                                      age,
                                                      pet_type,
                                                      pet_name,
                                                      pet_age)
