import sys, logging
from render import Render

logging.basicConfig(level=logging.INFO, format="[%(levelname)s](%(module)s->%(funcName)s): %(message)s")

renderer = Render(sys.argv)
renderer.start()