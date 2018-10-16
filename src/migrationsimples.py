import sys

sys.path.extend(['/home/carlos/PycharmProjects/conecturma_pn', '/home/carlos/PycharmProjects/conecturma_pn/src',
                 '/home/carlos/PycharmProjects/conecturma_pn/src/migration',
                 '/home/carlos/PycharmProjects/conecturma_pn/src/migration/code'])

exec(open("migration.py").read())