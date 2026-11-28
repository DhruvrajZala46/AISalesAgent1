import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import edit, scenes
n0, n1, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
scenes.render(edit.build(), n0, n1, out)
