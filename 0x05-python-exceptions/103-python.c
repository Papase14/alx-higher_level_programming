#include <Python.h>
#include <floatobject.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[*] Python object is not a list\n");
        return;
    }
    
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);
    
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *typeName = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, typeName);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object is not valid\n");
        return;
    }
    
    Py_ssize_t size = PyBytes_Size(p);
    const char *bytes = PyBytes_AsString(p);
    
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes);
    
    if (size > 10)
        size = 10;
    
    printf("  first %ld bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x", (unsigned char)bytes[i]);
        if (i != size - 1)
            printf(" ");
    }
    
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object is not valid\n");
        return;
    }
    
    PyFloatObject *f = (PyFloatObject *)p;
    
    printf("[.] float object info\n");
    printf("  value: %f\n", f->ob_fval);
}
