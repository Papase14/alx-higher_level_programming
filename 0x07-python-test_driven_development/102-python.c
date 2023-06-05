#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_string(PyObject *p);

/**
 * print_python_string - prints a Python string
 * @p: pointer to a Python object
 */
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        printf("[.] string object info\n");
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");
    Py_ssize_t size = PyUnicode_GET_LENGTH(p);
    const char *str = PyUnicode_AsUTF8(p);
    int is_ascii = PyUnicode_IS_ASCII(p);

    if (is_ascii)
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    printf("  length: %ld\n", size);
    printf("  value: %s\n", str);
}

