void print_python_dict(PyObject *p){
    PyObject *key, *value;
    Py_ssize_t pos = 0;
    while (PyDict_Next(p, &pos, &key, &value)) {
        print_python_object(key);
        print_python_object(value);
        printf("\n");
    }
}