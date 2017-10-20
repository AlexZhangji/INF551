import sys

import mysql.connector


def search_query(term, cnx):
    cursor = cnx.cursor()

    cursor.execute("SELECT " \
                   "COUNT( film_category.category_id ) AS category_count " \
                   "FROM " \
                   "film_category " \
                   "JOIN category ON category.category_id = film_category.category_id " \
                   "WHERE LOWER(category.NAME) LIKE LOWER(%s);", (term,))

    for name in cursor:
        print name[0]

    cursor.close()
    cnx.close()


if sys.argv[1:]:
    term = sys.argv[1:][0]
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='sakila')
    search_query(term, cnx)
