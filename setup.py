from setuptools import setup, find_packages
 
setup (
  name='pygments-cellscriptlexer',
  version = '0.1.0',
  license = 'Apache 2.0 License',
  author = 'Hugh Sorby',
  author_email = 'h.sorby@auckland.ac.nz',
  description = 'Pygments is a syntax highlighting package for cell script.',
  packages=find_packages(exclude=['tests']),
  entry_points =
  """
  [pygments.lexers]
  cellscriptlexer = lexers.cellscript:CellScriptLexer
  """,
)

