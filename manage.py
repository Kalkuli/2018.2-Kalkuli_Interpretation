from flask.cli	import	FlaskGroup
from project	import	create_app
import unittest


app = create_app()

cli = FlaskGroup(create_app=create_app)

@cli.command()
def test():
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if	__name__	==	'__main__':
    cli()
