import importlib
import pkgutil

from qagen.qagen import QAGen
import math_taxonomy

MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

package = math_taxonomy
prefix = package.__name__ + "."

if __name__ == '__main__':
    bad_modules = []
    good_modules = []
    for importer, modname, ispkg in pkgutil.walk_packages(math_taxonomy.__path__, prefix):
        try:
            importlib.import_module(modname, )
            good_modules.append(modname)
        except SyntaxError:
            bad_modules.append(modname)
            print("Module %s has syntax errors" % modname)
    print("Number of modules with syntax errors: %s" % len(bad_modules))
    print("Number of QA instances: %s" % len(vars()["QAGen"].__subclasses__()))
