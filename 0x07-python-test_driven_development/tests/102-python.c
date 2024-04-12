#include <Python.h>
#include <object.h>
#include <unicodeobject.h>
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    wchar_t *value;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else if (PyUnicode_IS_COMPACT(p))
        printf("  type: compact unicode object\n");
    else
        printf("  type: string object\n");

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsWideCharString(p, &length);
    printf("  length: %zd\n", length);
    printf("  value: %ls\n", value);
    PyMem_Free(value);
}
