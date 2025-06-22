from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests  # O corrige según tu clase real
from searchtests import SearchTests     # O corrige según tu clase real

# Cargar pruebas desde cada clase
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# Crear una suite con ambas
smoke_test = TestSuite([assertions_test, search_test])

# Ejecutar y generar reporte
kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
